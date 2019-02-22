
-- Create the PostGIS extension
create extension postgis

-- Import the polygons shapefile

-- Creating the centroid & edges tables & populating them 

--Centroid

-- NODES - City Centroids
	-- Create the table of centroids 
	drop table public.centroids
	CREATE TABLE public.centroids (
	    gid         integer CONSTRAINT firstkey PRIMARY KEY,
	    name   varchar(40) NOT NULL,
	    geom	geometry(point,3857)
	);

	-- Insert the centroids to the new table
	insert into public.centroids
		(select gid, name_2, st_setSRID(st_centroid(geom),3857) 
		from p_ilceler)

-- EDGES - Lines between adjacent polygons

	-- Create the table of lines
	drop table public.edges
	CREATE TABLE public.edges (
	    gid         serial PRIMARY KEY,
	    origin        varchar(40) NOT NULL,
	    destination   varchar(40) NOT NULL,
	    weight	 double precision,  
	    geom	geometry(LineString,3857),
	    origin_gid integer,
	    destination_gid integer
	);

	-- Insert the edges to the new table 
	insert into public.edges(origin, destination, weight, geom, origin_gid, destination_gid)
		(select a.name_2, b.name_2,  
			(st_length(st_makeline(st_centroid(a.geom), st_centroid(b.geom)))),
			st_makeline(st_setSRID(st_centroid(a.geom),3857), st_setSRID(st_centroid(b.geom),3857)), a.gid, b.gid
		from p_ilceler a, p_ilceler b
		where st_intersects(a.geom, b.geom) and a.gid != b.gid
		)
	-- LIMITATION: This generates the same edge twice! Do NOT consider the symmetric relation between the polygons
	-- How it would be possible to half the size of the table???


-- Obtain the edges present in MST (in QGIS)
-- Display the edges
select e.*
from results r, edges e
where r.origin = e.origin_gid and r.destination = e.destination_gid
