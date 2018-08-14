-- select s.id, s.field_name from fieldstats as s;

with mapping as (
SELECT C.id as concept_id, C.name as concept_name, F.model_name, F.field_name, coalesce(S.field_name, S2.field_name) as redcap_element
FROM avocado_dataconcept AS C
INNER JOIN avocado_dataconceptfield AS CF
     ON C.id = CF.concept_id
INNER JOIN avocado_datafield AS F
      ON CF.field_id = F.id
LEFT OUTER JOIN fieldstats AS S
     ON F.field_name = S.field_name
LEFT OUTER JOIN fieldstats AS S2
     ON F.model_name = REPLACE(S2.field_name, '_', '')
WHERE F.field_name not like '%summary'
)
select * into sma_r_conceptredcap from mapping where redcap_element is not null
order by concept_id;

