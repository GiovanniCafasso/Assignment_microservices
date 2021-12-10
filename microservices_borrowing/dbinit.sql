CREATE DATABASE "borrowing" OWNER postgres;
\connect borrowing
ALTER DATABASE "borrowing" SET TIMEZONE TO 'Europe/Rome';
SET TIMEZONE TO 'Europe/Rome';

CREATE TABLE "borrowing"
(
    id integer,
    id_book integer,
    id_cutomer character
) TABLESPACE pg_default;

ALTER TABLE "borrowing"
    OWNER to postgres;