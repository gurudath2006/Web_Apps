-- Table: public.Role

-- DROP TABLE public."Role";

CREATE TABLE public."Role"
(
    "RoleId" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    "RoleName" text COLLATE pg_catalog."default",
    CONSTRAINT "Role_pkey" PRIMARY KEY ("RoleId")
)

TABLESPACE pg_default;

ALTER TABLE public."Role"
    OWNER to postgres;