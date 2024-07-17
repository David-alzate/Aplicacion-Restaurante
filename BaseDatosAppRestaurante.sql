--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

-- Started on 2024-07-09 18:26:14

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
-- TOC entry 219 (class 1259 OID 17229)
-- Name: facturacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.facturacion (
    id_facturacion integer NOT NULL,
    nombre_pedido character varying(255),
    nombre_mesero character varying(255),
    fecha_emision character varying(255),
    precio integer,
    id_local integer,
    id_pedido integer
);


ALTER TABLE public.facturacion OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 17228)
-- Name: facturacion_id_facturacion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.facturacion_id_facturacion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.facturacion_id_facturacion_seq OWNER TO postgres;

--
-- TOC entry 3382 (class 0 OID 0)
-- Dependencies: 218
-- Name: facturacion_id_facturacion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.facturacion_id_facturacion_seq OWNED BY public.facturacion.id_facturacion;


--
-- TOC entry 223 (class 1259 OID 17257)
-- Name: facturacion_reporte; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.facturacion_reporte (
    id_reportefactura integer NOT NULL,
    id_facturacion integer,
    id_reporte integer
);


ALTER TABLE public.facturacion_reporte OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 17256)
-- Name: facturacion_reporte_id_reportefactura_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.facturacion_reporte_id_reportefactura_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.facturacion_reporte_id_reportefactura_seq OWNER TO postgres;

--
-- TOC entry 3383 (class 0 OID 0)
-- Dependencies: 222
-- Name: facturacion_reporte_id_reportefactura_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.facturacion_reporte_id_reportefactura_seq OWNED BY public.facturacion_reporte.id_reportefactura;


--
-- TOC entry 215 (class 1259 OID 17184)
-- Name: local; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.local (
    id_local integer NOT NULL,
    nombre_establecimiento character varying(255)
);


ALTER TABLE public.local OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 17183)
-- Name: local_id_local_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.local_id_local_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.local_id_local_seq OWNER TO postgres;

--
-- TOC entry 3384 (class 0 OID 0)
-- Dependencies: 214
-- Name: local_id_local_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.local_id_local_seq OWNED BY public.local.id_local;


--
-- TOC entry 217 (class 1259 OID 17191)
-- Name: pedido; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedido (
    id_pedido integer NOT NULL,
    deseoscliente character varying(255),
    fechaemision date,
    nombremesero character varying(255),
    estado boolean,
    numeromesa integer
);


ALTER TABLE public.pedido OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17190)
-- Name: pedido_id_pedido_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pedido_id_pedido_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pedido_id_pedido_seq OWNER TO postgres;

--
-- TOC entry 3385 (class 0 OID 0)
-- Dependencies: 216
-- Name: pedido_id_pedido_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pedido_id_pedido_seq OWNED BY public.pedido.id_pedido;


--
-- TOC entry 226 (class 1259 OID 17284)
-- Name: producto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producto (
    nombreproducto character varying(255) NOT NULL,
    precio integer,
    nombreestablecimiento character varying(255)
);


ALTER TABLE public.producto OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 17292)
-- Name: producto_pedido; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producto_pedido (
    id_producto_pedido integer NOT NULL,
    nombreproducto character varying(255),
    cantidad integer,
    id_pedido integer,
    estado boolean
);


ALTER TABLE public.producto_pedido OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 17291)
-- Name: producto_pedido_idpedidoproducto_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.producto_pedido_idpedidoproducto_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producto_pedido_idpedidoproducto_seq OWNER TO postgres;

--
-- TOC entry 3386 (class 0 OID 0)
-- Dependencies: 227
-- Name: producto_pedido_idpedidoproducto_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.producto_pedido_idpedidoproducto_seq OWNED BY public.producto_pedido.id_producto_pedido;


--
-- TOC entry 221 (class 1259 OID 17248)
-- Name: reporte_ventas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reporte_ventas (
    id_reporte integer NOT NULL,
    id_pedido integer,
    fechaemision date,
    nombremesero character varying,
    numeromesa integer,
    valortotal double precision
);


ALTER TABLE public.reporte_ventas OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 17247)
-- Name: reporte_ventas_id_reporte_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reporte_ventas_id_reporte_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reporte_ventas_id_reporte_seq OWNER TO postgres;

--
-- TOC entry 3387 (class 0 OID 0)
-- Dependencies: 220
-- Name: reporte_ventas_id_reporte_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reporte_ventas_id_reporte_seq OWNED BY public.reporte_ventas.id_reporte;


--
-- TOC entry 225 (class 1259 OID 17274)
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    nombre character varying(255),
    apellido character varying(255),
    correo character varying(255),
    telefono character varying(20),
    direccion character varying(255),
    id integer NOT NULL,
    password character varying(255),
    rol character varying(50)
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 17273)
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuarios_id_seq OWNER TO postgres;

--
-- TOC entry 3388 (class 0 OID 0)
-- Dependencies: 224
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- TOC entry 3209 (class 2604 OID 17232)
-- Name: facturacion id_facturacion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion ALTER COLUMN id_facturacion SET DEFAULT nextval('public.facturacion_id_facturacion_seq'::regclass);


--
-- TOC entry 3211 (class 2604 OID 17260)
-- Name: facturacion_reporte id_reportefactura; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion_reporte ALTER COLUMN id_reportefactura SET DEFAULT nextval('public.facturacion_reporte_id_reportefactura_seq'::regclass);


--
-- TOC entry 3207 (class 2604 OID 17187)
-- Name: local id_local; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.local ALTER COLUMN id_local SET DEFAULT nextval('public.local_id_local_seq'::regclass);


--
-- TOC entry 3208 (class 2604 OID 17194)
-- Name: pedido id_pedido; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido ALTER COLUMN id_pedido SET DEFAULT nextval('public.pedido_id_pedido_seq'::regclass);


--
-- TOC entry 3213 (class 2604 OID 17295)
-- Name: producto_pedido id_producto_pedido; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto_pedido ALTER COLUMN id_producto_pedido SET DEFAULT nextval('public.producto_pedido_idpedidoproducto_seq'::regclass);


--
-- TOC entry 3210 (class 2604 OID 17251)
-- Name: reporte_ventas id_reporte; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reporte_ventas ALTER COLUMN id_reporte SET DEFAULT nextval('public.reporte_ventas_id_reporte_seq'::regclass);


--
-- TOC entry 3212 (class 2604 OID 17277)
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- TOC entry 3219 (class 2606 OID 17236)
-- Name: facturacion facturacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion
    ADD CONSTRAINT facturacion_pkey PRIMARY KEY (id_facturacion);


--
-- TOC entry 3223 (class 2606 OID 17262)
-- Name: facturacion_reporte facturacion_reporte_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion_reporte
    ADD CONSTRAINT facturacion_reporte_pkey PRIMARY KEY (id_reportefactura);


--
-- TOC entry 3215 (class 2606 OID 17189)
-- Name: local local_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.local
    ADD CONSTRAINT local_pkey PRIMARY KEY (id_local);


--
-- TOC entry 3217 (class 2606 OID 17198)
-- Name: pedido pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_pkey PRIMARY KEY (id_pedido);


--
-- TOC entry 3229 (class 2606 OID 17297)
-- Name: producto_pedido producto_pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto_pedido
    ADD CONSTRAINT producto_pedido_pkey PRIMARY KEY (id_producto_pedido);


--
-- TOC entry 3227 (class 2606 OID 17290)
-- Name: producto producto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto
    ADD CONSTRAINT producto_pkey PRIMARY KEY (nombreproducto);


--
-- TOC entry 3221 (class 2606 OID 17255)
-- Name: reporte_ventas reporte_ventas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reporte_ventas
    ADD CONSTRAINT reporte_ventas_pkey PRIMARY KEY (id_reporte);


--
-- TOC entry 3225 (class 2606 OID 17281)
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- TOC entry 3230 (class 2606 OID 17237)
-- Name: facturacion facturacion_id_local_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion
    ADD CONSTRAINT facturacion_id_local_fkey FOREIGN KEY (id_local) REFERENCES public.local(id_local);


--
-- TOC entry 3231 (class 2606 OID 17242)
-- Name: facturacion facturacion_id_pedido_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion
    ADD CONSTRAINT facturacion_id_pedido_fkey FOREIGN KEY (id_pedido) REFERENCES public.pedido(id_pedido);


--
-- TOC entry 3232 (class 2606 OID 17263)
-- Name: facturacion_reporte facturacion_reporte_id_facturacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion_reporte
    ADD CONSTRAINT facturacion_reporte_id_facturacion_fkey FOREIGN KEY (id_facturacion) REFERENCES public.facturacion(id_facturacion);


--
-- TOC entry 3233 (class 2606 OID 17268)
-- Name: facturacion_reporte facturacion_reporte_id_reporte_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facturacion_reporte
    ADD CONSTRAINT facturacion_reporte_id_reporte_fkey FOREIGN KEY (id_reporte) REFERENCES public.reporte_ventas(id_reporte);


--
-- TOC entry 3234 (class 2606 OID 17298)
-- Name: producto_pedido producto_pedido_id_pedido_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto_pedido
    ADD CONSTRAINT producto_pedido_id_pedido_fkey FOREIGN KEY (id_pedido) REFERENCES public.pedido(id_pedido);


-- Completed on 2024-07-09 18:26:14

--
-- PostgreSQL database dump complete
--

