create table sma_u_form2cat (form_name varchar(1024), category_name varchar(1024), cat_id int);

insert into sma_u_form2cat (form_name) select distinct("Form Name") from sma_r_datadictionary order by "Form Name";

update sma_u_form2cat set category_name = initcap(replace(form_name, '_', ' ')) ;


-- select 'insert into avocado_datacategory (name, archived, published, created, modified) values (''' || category_name || ''', false, true, now(), now());' from sma_u_form2cat order by form_name;

insert into avocado_datacategory (name, archived, published, created, modified) values ('Medical History', false, true, now(), now());
insert into avocado_datacategory (name, archived, published, created, modified) values ('Medical History Follow Up', false, true, now(), now());
insert into avocado_datacategory (name, archived, published, created, modified) values ('Patient Information', false, true, now(), now());




select * into tmp_concepts from avocado_dataconcept;

update avocado_dataconcept
set category_id = c.id
from sma_r_dataconceptredcap as cr
inner join sma_u_form2cat as fc on cr."Form Name" = fc.form_name
inner join avocado_datacategory as c on fc.category_name = c.name
where  cr.id = avocado_dataconcept.id
       and avocado_dataconcept.category_id is null;

