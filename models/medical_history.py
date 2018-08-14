from django.db import models
from .subjects import *
from harvest_inc.core import CharField
#from django.db.models import CharField



class MedicalHistory(models.Model):
    weight_lbs = CharField(help_text=u'lbs', null=True, max_length=2000, verbose_name=u'Birth weight (lbs.)', blank=True)
    weight_oz = CharField(help_text=u'oz', null=True, max_length=2000, verbose_name=u'Birth weight (oz.)', blank=True)
    weight_g = CharField(help_text=u'grams', null=True, max_length=2000, verbose_name=u'Birth Weight (grams)', blank=True)
    deliv_term = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Delivery term:', choices=[(1, u'Pre-term'), (2, u'Full-term'), (3, u'Post-term')])
    mh_sibidnumber = CharField(help_text=u'', null=True, verbose_name=u'Siblings SMA ID Number(s)', blank=True)
    affected_sibs_2 = CharField(help_text=u'', null=True, verbose_name=u'if applicable, ID of another sibling', blank=True)
    affected_sibs_3 = CharField(help_text=u'', null=True, verbose_name=u'if applicable, ID of another sibling', blank=True)
    mh_classify = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Patient Classification: (Current)', choices=[(1, u'Affected (Confirmed SMA)'), (2, u'Control'), (3, u'Disease Control'), (4, u'SMARD'), (5, u'Presymptomatic'), (6, u'Unknown'), (888, u'Other (Specify)')])
    mh_classify_oth = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Patient Classification - Other (Specify)', blank=True)
    mh_smadx_type = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'SMA Type', choices=[(0, u'0/1a'), (1, u'1'), (2, u'2'), (3, u'3a'), (4, u'3b'), (5, u'3 (unknown subtype)'), (6, u'4'), (7, u'Presymptomatic'), (8, u'Disease Control'), (9, u'Normal Control'), (888, u'Unknown')])
    mh_smadx_smndel = models.NullBooleanField(help_text=u'only available in SPOT SMA', verbose_name=u'SMN1 deletion homozygous:', blank=True)
    smn_deletion = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'If homozygous SMN1 deletion:', choices=[(1, u'exon 7'), (2, u'exon 7 & 8'), (3, u'whole gene deletion'), (999, u'unknown')])
    smn_heterzygous_point = models.NullBooleanField(help_text=u'', verbose_name=u'If heterozygous SMN1 deletion, was there a point mutation on the other allele?', blank=True)
    smn_heter_poin_mut = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'If there is a point mutation, what is the mutation?', blank=True)
    smn_copy_num = models.IntegerField(help_text=u'', null=True, verbose_name=u'SMN 2 copy #:', blank=True, choices=[(0, u'0'), (1, u'1'), (2, u'2'), (3, u'3'), (4, u'4'), (5, u'5'), (6, u'Unknown / Not tested')]) # This field type is a guess
    mh_sma_smn2_modifier = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'SMN modifier mutation present: SMN2 c.859G>C:', choices=[(1, u'Yes'), (0, u'No'), (999, u'Not Tested')])
    onset_age = models.IntegerField(help_text=u'', null=True, verbose_name=u"Initial age of onset SMA symptoms, to the best of parents' recollection:", blank=True, choices=[(1, u'0-2 months'), (2, u'3-6 months'), (3, u'7-11 months'), (4, u'12-16 months'), (5, u'17-23 months'), (6, u'24-35 months'), (7, u'24-35 months'), (8, u'6-12 years'), (9, u'13-17 years'), (10, u'>18 years')]) # This field type is a guess
    rolled_completely = models.NullBooleanField(help_text=u'', verbose_name=u'Rolled Completely', blank=True)
    rolled_completely_age = CharField(help_text=u'Months', null=True, max_length=2000, verbose_name=u'Age Rolled Completely', blank=True)
    sat_unsupported = models.NullBooleanField(help_text=u'', verbose_name=u'Sat Unsupported', blank=True)
    sat_unsupported_age = CharField(help_text=u'Months', null=True, max_length=2000, verbose_name=u'Age Sat unsupported', blank=True)
    walk_independent = models.NullBooleanField(help_text=u'', verbose_name=u'Walked independently', blank=True)
    walk_independent_age = CharField(help_text=u'Months', null=True, max_length=2000, verbose_name=u'Age Walked independently (without braces)', blank=True)
    mh_smadx_presymp = models.NullBooleanField(help_text=u'', verbose_name=u'Presymptomatic at enrollment?', blank=True)
    age_achieved_max_gr = models.IntegerField(help_text=u'', null=True, verbose_name=u"Age of achieved maximum gross motor function (to best of parents' recollection)", blank=True, choices=[(1, u'0-2 months'), (2, u'3-6 months'), (3, u'7-11 months'), (4, u'12-16 months'), (5, u'17-23 months'), (6, u'24-35 months'), (7, u'36 mos - 5 yrs'), (8, u'6 - 12 years'), (9, u'13-16 years'), (10, u'> 18 years'), (11, u'Still gaining motor skills')]) # This field type is a guess
    bipap_medhx = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Bipap or CPAP or other ventilator support', choices=[(1, u'Daily use'), (2, u'Occasional use'), (3, u'Use when ill only'), (4, u'Never use')])
    daily_medhx = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'If daily:', choices=[(0, u'N/A'), (5, u'< 6 hours / day'), (1, u'6-12 hours'), (2, u'13-16 hours'), (3, u'17-19 hours'), (4, u'>20 hours')])
    level_of_func_summary = CharField(help_text=u'1, Head control | 2, Raise Arms above head | 2a, Raise Arms above head lying in bed | 2b, Raise Arms above head sitting | 3, Roll Completely | 3a, Roll back to front | 3b, Roll front to back | 4, Sit supported | 5, Sit unsupported | 6, Crawl - Combat | 7, Crawl - Four point | 8, Stand with support | 9, Cruise along furniture | 10, Stand without support | 11, Walk with support (hand, braces, etc.) | 12, Walk independently without braces | 13, Climb stairs', null=True, max_length=2000, verbose_name=u'Current level of function : (Check all that Apply)', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'sma_f_medicalhistory'
         app_label = 'sma'


class leveloffunc(models.Model):
    label = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Current level of function : (Check all that Apply)', blank=True)
    value = CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Current level of function : (Check all that Apply)', blank=True)
    medicalhistory = models.ForeignKey(MedicalHistory)

    class Meta:
	 db_table = 'sma_mh_leveloffunc'
         app_label = 'sma'
