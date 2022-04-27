-- Table: public.ServiceCategory

-- DROP TABLE public."ServiceCategory";

CREATE TABLE public."ServiceCategory"
(
    "ServiceCategoryId" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    "ServiceCategoryName" text COLLATE pg_catalog."default",
    CONSTRAINT "ServiceCategory_pkey" PRIMARY KEY ("ServiceCategoryId")
)

TABLESPACE pg_default;

ALTER TABLE public."ServiceCategory"
    OWNER to postgres;