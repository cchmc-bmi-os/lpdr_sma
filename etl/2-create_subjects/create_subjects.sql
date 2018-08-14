-- Create Subjects
insert into sma_s_subject (study_id)
select study_id 
from sma_s_record
group by study_id
order by study_id;

-- Create Harvest subject id
update sma_s_subject set study_id_anonymous = 'sma_' || id;

-- Link records to subjects
update sma_s_record
set subject_id = sma_s_subject.id from sma_s_subject 
where sma_s_record.study_id=sma_s_subject.study_id;

-- Link sma_f_patientinformation to subjects
update sma_f_patientinformation
set subject_id = sma_s_subject.id from sma_s_subject 
where sma_f_patientinformation.study_id=sma_s_subject.study_id::integer;
