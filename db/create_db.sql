CREATE TABLE IF NOT EXISTS public.users
(
    "Guid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "idDevice" character varying(100) COLLATE pg_catalog."default",
    name character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY ("Guid")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;
	
CREATE TABLE IF NOT EXISTS public.images
(
    "Guid" uuid NOT NULL DEFAULT gen_random_uuid(),
    image_path character varying(500) COLLATE pg_catalog."default" NOT NULL,
    "user" uuid NOT NULL,
    CONSTRAINT images_pkey PRIMARY KEY ("Guid"),
    CONSTRAINT fk_users_images FOREIGN KEY ("user")
        REFERENCES public.users ("Guid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.images
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.point_types
(
    "Guid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "name" character varying(100) COLLATE pg_catalog."default",
    description character varying(1000) COLLATE pg_catalog."default",
    CONSTRAINT point_types_pkey PRIMARY KEY ("Guid")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.point_types
    OWNER to postgres;
	
CREATE TABLE IF NOT EXISTS public.line_types
(
    "Guid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "name" character varying(100) COLLATE pg_catalog."default",
    description character varying(1000) COLLATE pg_catalog."default",
    CONSTRAINT line_types_pkey PRIMARY KEY ("Guid")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.line_types
    OWNER to postgres;
	
CREATE TABLE IF NOT EXISTS public.param_types
(
    "Guid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "name" character varying(100) COLLATE pg_catalog."default",
    description character varying(1000) COLLATE pg_catalog."default",
	"min" float,
	"max" float,
    CONSTRAINT param_types_pkey PRIMARY KEY ("Guid")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.param_types
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.points
(
    "Guid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "image" uuid NOT NULL,
    X int NOT NULL,
	Y int NOT NULL,
	"point_type" uuid NOT NULL,
    CONSTRAINT points_pkey PRIMARY KEY ("Guid"),
    CONSTRAINT fk_images_points FOREIGN KEY ("image")
        REFERENCES public.images ("Guid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
	CONSTRAINT fk_point_types_points FOREIGN KEY ("point_type")
        REFERENCES public.point_types ("Guid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.points
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.lines
(
    "Guid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "image" uuid NOT NULL,
    X int NOT NULL,
	Y int NOT NULL,
	"line_type" uuid NOT NULL,
	"start_point" uuid NOT NULL,
	"end_point" uuid NOT NULL,
    CONSTRAINT lines_pkey PRIMARY KEY ("Guid"),
    CONSTRAINT fk_images_lines FOREIGN KEY ("image")
        REFERENCES public.images ("Guid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
	CONSTRAINT fk_line_types_lines FOREIGN KEY ("line_type")
        REFERENCES public.line_types ("Guid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
	CONSTRAINT fk_start_points_lines FOREIGN KEY ("start_point")
        REFERENCES public.points ("Guid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
	CONSTRAINT fk_end_points_lines FOREIGN KEY ("end_point")
        REFERENCES public.points ("Guid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.lines
    OWNER to postgres;
	
CREATE TABLE IF NOT EXISTS public.params
(
    "Guid" uuid NOT NULL DEFAULT gen_random_uuid(),
    "image" uuid NOT NULL,
	"param_type" uuid NOT NULL,
	"value" float not NULL,
    CONSTRAINT params_pkey PRIMARY KEY ("Guid"),
    CONSTRAINT fk_images_lines FOREIGN KEY ("image")
        REFERENCES public.images ("Guid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
	CONSTRAINT fk_param_types_params FOREIGN KEY ("param_type")
        REFERENCES public.param_types ("Guid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.lines
    OWNER to postgres;