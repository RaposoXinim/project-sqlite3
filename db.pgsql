--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Alunos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Alunos" (
    "ID" integer NOT NULL,
    "Nome" text
);


ALTER TABLE public."Alunos" OWNER TO postgres;

--
-- Name: Professores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Professores" (
    "ID" integer NOT NULL,
    "Nome" text,
    "Materia" text
);


ALTER TABLE public."Professores" OWNER TO postgres;

--
-- Name: Salas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Salas" (
    "IDPROFESSOR" integer NOT NULL,
    "Materia" text,
    "Horario" text,
    "Alunos" text,
    CONSTRAINT check_alunos_format CHECK (("Alunos" ~ '^(\s\d+\s){0,11}$'::text)),
    CONSTRAINT check_horario CHECK (("Horario" = ANY (ARRAY['manha'::text, 'tarde'::text])))
);


ALTER TABLE public."Salas" OWNER TO postgres;

--
-- Name: Usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Usuarios" (
    "Login" text NOT NULL,
    "Senha" text NOT NULL
);


ALTER TABLE public."Usuarios" OWNER TO postgres;

--
-- Data for Name: Alunos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Alunos" ("ID", "Nome") FROM stdin;
1	CARLINHOS
\.


--
-- Data for Name: Professores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Professores" ("ID", "Nome", "Materia") FROM stdin;
1	gamer	historia
67	jorge	matematica
6	roberto	fis
453	sdfds	dfssdf
45	poggerino	historia dos games
\.


--
-- Data for Name: Salas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Salas" ("IDPROFESSOR", "Materia", "Horario", "Alunos") FROM stdin;
1	matematica	manha	 0  1  1  1  1  1  1  1  1  1  1 
\.


--
-- Data for Name: Usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Usuarios" ("Login", "Senha") FROM stdin;
\.


--
-- Name: Alunos IDALUNO; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Alunos"
    ADD CONSTRAINT "IDALUNO" PRIMARY KEY ("ID");


--
-- Name: Professores IDPROFESSOR; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Professores"
    ADD CONSTRAINT "IDPROFESSOR" PRIMARY KEY ("ID");


--
-- Name: Usuarios Usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "Usuarios_pkey" PRIMARY KEY ("Login");


--
-- Name: Salas horario_unico_por_professor; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Salas"
    ADD CONSTRAINT horario_unico_por_professor UNIQUE ("IDPROFESSOR", "Horario");


--
-- Name: fki_i; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_i ON public."Salas" USING btree ("IDPROFESSOR");


--
-- Name: Salas IDPROFESSOR; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Salas"
    ADD CONSTRAINT "IDPROFESSOR" FOREIGN KEY ("IDPROFESSOR") REFERENCES public."Professores"("ID") NOT VALID;


--
-- PostgreSQL database dump complete
--

