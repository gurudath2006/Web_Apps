-- Table: public.Provider

-- DROP TABLE public."Provider";

CREATE TABLE public."Provider"
(
    "FirstName" text COLLATE pg_catalog."default",
    "LastName" text COLLATE pg_catalog."default",
    "ServiceCategoryId" integer,
    "Address" text COLLATE pg_catalog."default",
    "Email" text COLLATE pg_catalog."default",
    "ProviderId" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    "Phone" text COLLATE pg_catalog."default",
    "LocationId" bigint,
    CONSTRAINT "Provider_pkey" PRIMARY KEY ("ProviderId"),
    CONSTRAINT fk_provider_servciecategoryid FOREIGN KEY ("ServiceCategoryId")
        REFERENCES public."ServiceCategory" ("ServiceCategoryId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public."Provider"
    OWNER to postgres;