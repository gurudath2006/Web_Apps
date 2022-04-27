-- Table: public.PatientBooking

-- DROP TABLE public."PatientBooking";

CREATE TABLE public."PatientBooking"
(
    "PatientBookingId" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    "PatientId" bigint,
    "ProviderId" bigint,
    "BookingDate" timestamp without time zone,
    CONSTRAINT "PatientBooking_pkey" PRIMARY KEY ("PatientBookingId"),
    CONSTRAINT fk_patientbooking_patientid FOREIGN KEY ("PatientId")
        REFERENCES public."Patient" ("PatientId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public."PatientBooking"
    OWNER to postgres;