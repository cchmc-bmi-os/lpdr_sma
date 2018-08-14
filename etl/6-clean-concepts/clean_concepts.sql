-- Remove the html tags

with D1 as (SELECT id, (regexp_matches(name, '[^>]+>([^>]+)>', 'g'))[1] M1 from avocado_dataconcept), D2 as (select * from D1 where M1 not like '<%') select id, (regexp_matches(M1, '([^<]+)'))[1] S into tmp_clean_concept_names from D2;

update avocado_dataconcept set name = u.s from tmp_clean_concept_names u where avocado_dataconcept.id = u.id;

with D1 as (SELECT id, (regexp_matches(name, '<B>([^<]+)</B>', 'g'))[1] s from avocado_dataconcept) select * into tmp_clean_concept_names2 from D1;

update avocado_dataconcept set name = u.s from tmp_clean_concept_names2 u where avocado_dataconcept.id = u.id;
