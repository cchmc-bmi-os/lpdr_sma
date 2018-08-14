-- To be defined

with D as (
select mh.record_id, mh.mh_smadx_type, r.subject_id
from sma_f_medicalhistory mh
inner join sma_s_record r
      on mh.record_id = r.id
where mh.mh_smadx_type is not null
order by r.id),
U as (
select distinct on (record_id) record_id, mh_smadx_type, subject_id from D
)
update sma_s_subject
set mh_smadx_type = U.mh_smadx_type
from U
where sma_s_subject.id = U.subject_id;
