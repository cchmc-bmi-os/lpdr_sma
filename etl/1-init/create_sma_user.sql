create user srv_sma encrypted password 'xxx';
create schema sma authorization srv_sma;
alter user srv_sma set search_path = sma;

-- other user shouldn't have any permissions on sma
