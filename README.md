# GIS-Programming
This repository contains the data, information and code about the content of the "GMT 456 GIS Programming" course offered at the Geomatics Engineering Dept. of Hacettepe University, Turkey.

The developed code is based on Python as it allows to further extend into a QGIS plugin.

## Contents:
* Object oriented programming - A Recap
   * Function Calls – pass by reference vs pass by value
   * Signal- Slot
* Graph Data Structure
   * Adjacency Matrix
   * Disjoint Sets
   * Minimum Spanning Tree
      * Kruskal's Algorithm
      * Prim's Algorithm
* Building a QGIS Plugin

## Methodology
1. Import the polygon shapefile into PostGIS.
2. Create the *centroids* table. 
     1. geometry_id
     2. name
     3. geometry
3. Populate the centroids table: 
    `		insert into public.centroids 
           (select gid, name_2, st_centroid(geom) 
           from ilceler)`
     
