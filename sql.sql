-- CREATE THE POSTGIS EXTENSION
create extension postgis

-- Import the polygons shapefile

-- CREATING THE NECESSARY TABLES

-- NODES - City Centroids
	-- Create the table of centroids 
	drop table public.centroids
	CREATE TABLE public.centroids (
	    gid         integer CONSTRAINT firstkey PRIMARY KEY,
	    name_polygon   varchar(40) NOT NULL,
	    geom	geometry(point,3857)
	);

	-- Insert the centroids to the new table
	insert into public.centroids
		(select gid, name, st_centroid(geom) 
		from polygons)

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
		(select a.ad, b.ad,  
			(st_length(st_makeline(st_centroid(a.geom), st_centroid(b.geom)))),
			st_makeline(st_centroid(a.geom), st_centroid(b.geom)), a.gid, b.gid
		from polygons a, polygons b
		where st_intersects(a.geom, b.geom) and a.gid != b.gid
		)
	-- LIMITATION: This generates the same edge twice! Do NOT consider the symmetric relation between the polygons
	-- How it would be possible to half the size of the table???