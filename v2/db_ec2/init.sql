CREATE TABLE IF NOT EXISTS public.ecowas (
    id integer NOT NULL DEFAULT nextval('ecowas_id_seq'::regclass),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    population integer NOT NULL,
    gdppc integer NOT NULL,
    hdi numeric NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT ecowas_pkey PRIMARY KEY (id),
    CONSTRAINT ecowas_name_key UNIQUE (name)
)
INSERT INTO public.ecowas (id, name, population, GDPpc, HDI)
VALUES 
(1, 'Benin',            12451031,   1421,   .545), 
(2, 'Burkina Faso',     21497097,   918,    .452),  
(3, 'Cabo Verde',       561901,     3446,   .665), 
(4, 'Côte d’Ivoire',    27053629,   2579,   .538), 
(5, 'The Gambia',       2486937,    836,    .496),  
(6, 'Ghana',            31394000,   2521,   .611),  
(7, 'Guinea',           13497237,   1174,   .477),  
(8, 'Guinea Bissau',    2015490,    813,    .480), 
(9, 'Liberia',          5180208,    673,    .480), 
(10, 'Mali',            20855724,   918,    .434),  
(11, 'Niger',           25130810,   595,    .394),  
(12, 'Nigeria',         211400704,  2085,   .539), 
(13, 'Senegal',         17196308,   1607,   .512),  
(14, 'Sierra Leone',    8141000,    509,    .452),  
(15, 'Togo',            8478242,    992,    .515);