CREATE DATABASE "book" OWNER postgres;
\connect book
ALTER DATABASE "book" SET TIMEZONE TO 'Europe/Rome';
SET TIMEZONE TO 'Europe/Rome';

CREATE TABLE "books"
(
    id integer,
    title character varying,
    author character varying
) TABLESPACE pg_default;

ALTER TABLE "books"
    OWNER to postgres;