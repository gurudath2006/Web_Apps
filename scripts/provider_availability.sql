-- Table: public.ProviderAvailability

-- DROP TABLE public."ProviderAvailability";

CREATE TABLE public."ProviderAvailability"
(
    "ProviderAvailabilityId" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    "ProviderId" bigint,
    "AvailableDate" timestamp without time zone,
    CONSTRAINT "ProviderAvailability_pkey" PRIMARY KEY ("ProviderAvailabilityId"),
    CONSTRAINT fk_provideravailability_providerid FOREIGN KEY ("ProviderId")
        REFERENCES public."Provider" ("ProviderId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public."ProviderAvailability"
    OWNER to postgres;