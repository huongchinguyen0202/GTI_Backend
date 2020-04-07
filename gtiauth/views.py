from authy.api import AuthyApiClient
from django.conf import settings
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from gtiauth.models import User
import requests
import json

authy_api = AuthyApiClient(settings.ACCOUNT_SECURITY_API_KEY)

class GtiAuth(View):

    parser_classes = [JSONParser]

    @api_view(["POST"])
    def api_login(request):
        """
        post:
        This view is called through API POST with a json body like so:

        {
            "username": "admin",
            "password": "admin"
        }

        :param request:
        :return:
        """

        response_login = requests.post(
            request.build_absolute_uri(reverse('obtain_jwt_token')),
            data=request.data
        )
        response_login_dict = json.loads(response_login.content)
        
        if response_login.ok:
            user = authenticate(username=request.data['username'], password=request.data['password'])
            authy_api.phones.verification_start(user.phone, '+84', via='sms', code_length=6)

        return Response(response_login_dict, response_login.status_code)