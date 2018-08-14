-- Check the ids of the initial concepts since they could change following an update
select * from avocado_dataconcept where name ilike '%sibling%';   -- 70, 71, 72

update avocado_dataconcept set name='Sibling 1' where id = 70;
update avocado_dataconcept set name='Sibling 2' where id = 71;
update avocado_dataconcept set name='Sibling 3' where id = 72;
