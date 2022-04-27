-- Table: public.Location

-- DROP TABLE public."Location";

CREATE TABLE public."Location"
(
    "LocationId" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    "LocationName" text COLLATE pg_catalog."default",
    CONSTRAINT "Location_pkey" PRIMARY KEY ("LocationId")
)

TABLESPACE pg_default;

ALTER TABLE public."Location"
    OWNER to postgres;