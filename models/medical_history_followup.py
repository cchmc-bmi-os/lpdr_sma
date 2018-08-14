from .subjects import *
from django.db import models
from harvest_inc.core import CharField
#from django.db.models import CharField


class MedicalHistoryFollowUp(models.Model):
    medhxfollow_age_month = models.FloatField(help_text=u'Months', null=True, verbose_name=u'Age at visit', blank=True)
    bipap_cpap = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Bipap or CPAP', choices=[(1, u'Daily use'), (2, u'Occasional use'), (3, u'Use when ill only'), (4, u'Never use')])
    level_of_function_summary = CharField(help_text=u'1, Head control | 2, Raise arms above head | 3, Roll completely | 4, Sit supported | 5, Sit unsupported | 6, Crawl - Combat | 7, Crawl - Four point | 8, Stand with support | 9, Cruise along furniture | 10, Stand without support | 11, Walk with support (hand, braces, etc.) | 12, Walk independently without braces | 13, Climb Stairs', null=True, max_length=2000, verbose_name=u'Current level of function : (Check All that Apply)', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'sma_f_medicalhistoryfollowup'
         app_label = 'sma'


class leveloffunction(models.Model):
    label = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Current level of function : (Check All that Apply)', blank=True)
    value = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Current level of function : (Check All that Apply)', blank=True)
    medicalhistoryfollowup = models.ForeignKey(MedicalHistoryFollowUp)

    class Meta:
	 db_table = 'sma_mhf_leveloffunction'
         app_label = 'sma'
