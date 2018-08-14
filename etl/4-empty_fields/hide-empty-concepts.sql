
-- select id from avocado_datacategory where name = 'Empty Fields'; 1

update avocado_dataconcept
set category_id = 1
where id in (
select concept_id from sma_r_conceptredcap where redcap_element in (select field_name from fieldstats where ep=0 and np=0)
);

