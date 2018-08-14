from django.db import models
from harvest_inc.core import CharField
#from django.db.models import CharField


class Subject(models.Model):
    study_id = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Study ID', blank=True)
    study_id_anonymous = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Patient Number', blank=True)
    nb_visits = models.IntegerField(blank=True, null=True, verbose_name='Number of record')
    nb_complete_visits = models.IntegerField(blank=True, null=True, verbose_name='Number of complete visits')
    nb_valid_visits = models.IntegerField(blank=True, null=True, verbose_name='Number of valid visits')
    mh_smadx_type = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'SMA Type', choices=[(0, u'0/1a'), (1, u'1'), (2, u'2'), (3, u'3a'), (4, u'3b'), (5, u'3 (unknown subtype)'), (6, u'4'), (7, u'Presymptomatic'), (8, u'Disease Control'), (9, u'Normal Control'), (888, u'Unknown')])

    class Meta:
        app_label = 'sma'
        db_table = 'sma_s_subject'


class Record(models.Model):
    study_id = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Study ID', blank=True)
    redcap_event_name = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Redcap Event Name', blank=True)
    event_type = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Event type', blank=True)

    medical_history_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Medical History Complete")
    medical_history_followup_complete = models.IntegerField(help_text=u"", null=True, blank=True, verbose_name=u"Medical History Followup Complete")

    subject = models.ForeignKey(Subject, blank=True, null=True, related_name='record')

    class Meta:
        app_label='sma'
        db_table = 'sma_s_record'
