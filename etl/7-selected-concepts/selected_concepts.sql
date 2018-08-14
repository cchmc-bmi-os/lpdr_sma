-- From  Tyler's email of 10/31/2017

'sex', 'race', 'ethnic', 'age_death', 'end_stage_age_month', 'mh_classify', 'mh_smadx_type', 'smn_copy_num', 'smn_copy_test_site', 'smn_copy_test_site_name', 'smn_copy_test', 'smn1_two_allele_point_mut', 'smn1_two_allele_mut1', 'smn1_two_allele_mut2', 'mh_smadx_smndel', 'smn_deletion', 'smn_heterzygous_point', 'smn_heter_poin_mut', 'onset_age', 'age_achieved_max_gr', 'level_of_func', 'level_of_function'


select concept_id, redcap_element from sma_r_conceptredcap where redcap_element in ('sex', 'race', 'ethnic', 'age_death', 'end_stage_age_month', 'mh_classify', 'mh_smadx_type', 'smn_copy_num', 'smn_copy_test_site', 'smn_copy_test_site_name', 'smn_copy_test', 'smn1_two_allele_point_mut', 'smn1_two_allele_mut1', 'smn1_two_allele_mut2', 'mh_smadx_smndel', 'smn_deletion', 'smn_heterzygous_point', 'smn_heter_poin_mut', 'onset_age', 'age_achieved_max_gr', 'level_of_func', 'level_of_function') group by concept_id, redcap_element order by redcap_element;


select * from sma_r_datadictionary where "Variable / Field Name" in ('age_death', 'end_stage_age_month', 'smn1_two_allele_point_mut', 'smn1_two_allele_mut1', 'smn1_two_allele_mut2', 'smn_heterzygous_point', 'smn_heter_poin_mut');




-- From  Tyler's email of 11/01/2017

select concept_id, redcap_element from sma_r_conceptredcap where redcap_element in ('sex', 'race', 'ethnic', 'age_death', 'end_stage_age_month', 'mh_classify', 'mh_classify_oth', 'mh_smadx_type', 'smn_copy_num', 'mh_sma_smn2_modifier', 'mh_smadx_smndel', 'smn_deletion', 'smn_heterzygous_point', 'smn_heter_poin_mut', 'onset_age', 'age_achieved_max_gr', 'rolled_completely', 'rolled_completely_age', 'sat_unsupported', 'sat_unsupported_age', 'walk_independent', 'walk_independent_age', 'delv_term', 'weight_ibs', 'weight_oz', 'weight_g', 'mh_sibidnumber', 'affected_sibs_2', 'affected_sibs_3', 'bipap_medhx', 'daily_medhx', 'medhxfollow_age_month', 'level_of_func', 'level_of_function', 'bipap_cpap') group by concept_id, redcap_element order by redcap_element;

select * from sma_r_datadictionary where "Variable / Field Name" in ('age_death', 'delv_term', 'end_stage_age_month', 'mh_sma_smn2_modifier', 'smn_heter_poin_mut', 'smn_heterzygous_point', 'walk_independent_age', 'weight_ibs')


