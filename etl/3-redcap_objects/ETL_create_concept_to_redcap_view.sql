-- This links the **current** concept to the redcapt definition
create or replace view sma_r_dataconceptredcap as
       select C.id, C.name as concept_name, C.category_id, CAT.name as category_name, PAT.name as parent_cat, CR.redcap_element, DD."Form Name"
       from avocado_dataconcept as C
       left outer join sma_r_conceptredcap AS CR
            on C.id = CR.concept_id
	inner join  sma_r_datadictionary as DD
	      on CR.redcap_element = DD."Variable / Field Name"
	 left outer join avocado_datacategory as CAT
	      on C.category_id = CAT.id
	   left outer join avocado_datacategory as PAT
	   	ON CAT.parent_id = PAT.id
