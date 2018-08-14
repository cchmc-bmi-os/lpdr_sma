from django.db import models
from .subjects import *
from harvest_inc.core import CharField
#from django.db.models import CharField



class PatientInformation(models.Model):
    study_id = models.IntegerField(help_text=u'', null=True, verbose_name=u'Study ID', blank=True)
    age_death = models.FloatField(help_text=u'', null=True, verbose_name=u'Age when patient died: (year)', blank=True)
    end_stage_age_month = models.FloatField(help_text=u'', null=True, verbose_name=u'Age when patient reached 16 hr or greater daily ventilation support: ', blank=True)
    sex = models.IntegerField(help_text=u'', null=True, verbose_name=u'Gender', blank=True, choices=[(1, u'Male'), (2, u'Female')]) # This field type is a guess
    ethnic = models.IntegerField(help_text=u'', null=True, verbose_name=u'Ethnic Category', blank=True, choices=[(1, u'Hispanic or Latino'), (2, u'Not Hispanic or Latino'), (3, u'Unknown or Not Reported')]) # This field type is a guess
    race = models.IntegerField(help_text=u'', null=True, verbose_name=u'Racial Category', blank=True, choices=[(1, u'American Indian / Alaskan Native'), (2, u'Asian'), (3, u'Black or African American'), (4, u'Native Hawaiian or Other Pacific Islander'), (5, u'White'), (6, u'Unknown or Not Reported')]) # This field type is a guess
    record = models.IntegerField()
    subject = models.ForeignKey(Subject, blank=True, null=True)

    class Meta:
	 db_table = 'sma_f_patientinformation'
         app_label = 'sma'
