from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class ProjectType(models.Model):
    type = models.CharField(max_length=100)


class Project(models.Model):
    class Status(models.TextChoices):
        PENDING = '1', _('Pending')
        MATCHED = '2', _('Matched')
        SCOPING = '3', _('Scoping')
        ACTIVATE = '4', _('Project Activated')
        COMPLETED = '5', _('Completed')
        CLOSE = "6", _('Closed')

    id = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.PENDING)
    region = models.ManyToManyField('tags.Tag', related_name='region') #TODO should design to table
    country = models.ManyToManyField('tags.Tag', related_name='country') #TODO should design to table
    professional_background = models.ManyToManyField('tags.Tag', related_name='professional_background')
    relevant_qualification = models.ManyToManyField('tags.Tag', related_name='relevant_qualification')
    professional_service = models.ManyToManyField('tags.Tag', related_name='professional_service')
    specialist_knowledge_sector = models.ManyToManyField('tags.Tag', related_name='specialist_knowledge_sector')
    specialist_knowledge_key_issue_theme = models.ManyToManyField('tags.Tag', related_name='specialist_knowledge_key_issue_theme')
    project_type = models.ForeignKey('Project', on_delete=models.CASCADE)
    request_anonymity = models.BooleanField(default=False)
