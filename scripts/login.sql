-- Table: public.Login

-- DROP TABLE public."Login";

CREATE TABLE public."Login"
(
    "LoginId" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    "RoleId" integer,
    "Username" text COLLATE pg_catalog."default",
    "Password" text COLLATE pg_catalog."default",
    CONSTRAINT "User_pkey" PRIMARY KEY ("LoginId"),
    CONSTRAINT fk_login_roleid FOREIGN KEY ("RoleId")
        REFERENCES public."Role" ("RoleId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public."Login"
    OWNER to postgres;