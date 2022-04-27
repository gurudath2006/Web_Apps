-- Table: public.Patient

-- DROP TABLE public."Patient";

CREATE TABLE public."Patient"
(
    "PatientId" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    "FirstName" text COLLATE pg_catalog."default",
    "LastName" text COLLATE pg_catalog."default",
    "Email" text COLLATE pg_catalog."default",
    CONSTRAINT "Patient_pkey" PRIMARY KEY ("PatientId")
)

TABLESPACE pg_default;

ALTER TABLE public."Patient"
    OWNER to postgres;