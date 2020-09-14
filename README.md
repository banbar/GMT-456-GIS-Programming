# GMT 456 GIS Programming
This repository contains sample data, information and code about the "GMT 456 GIS Programming" course offered at the Geomatics Engineering Dept. of Hacettepe University, Turkey.

The aim of this course is to teach students how to collaborate on a software project involving spatial analysis by using git.   

The successful students would: 
* Describe the Software Design Life Cycle (SDLC) phases,
* Document the design and requirements of the software project that s/he worked on, 
developed software starting from requirements analysis to Write the requirement analysis report for the software project involving spatial analysis,
* Demonstrate the ability to work as a team for the purpose of developing a new or updating an existing QGIS plugin.


## Contents:
* Object oriented programming - A Recap
   * Function Calls – pass by reference vs pass by value
   * Signal- Slot
* Graph Data Structure
   * Adjacency Matrix
   * Disjoint Sets
   * Minimum Spanning Tree (MST)
      * Kruskal's Algorithm
      * Prim's Algorithm
* Building a QGIS Plugin

## PostGIS - SQL
1. Import the polygon shapefile into PostGIS
2. Create the *centroids* table
   1. gid (geometry_id) - serial
   2. name - varchar(40)
   3. geom (geometry) - geometry(point,*SRID*)
3. Populate the centroids table (st_centroid)
4. Create the *edges* table
    1. gid (geometry_id) - serial
    2. origin - text
    3. destination - text
    4. cost (weight) - float
    5. geom (geometry) - geometry(LineString, *SRID*)
    6. origin_gid - integer
    7. destination_gid - integer
5. Populate the edges table (st_intersects) 

- - - -
The MST of Turkish cities and districts are found by using the Kruskal's algorithm which is implemented in Python (previously shared on [Twitter](https://twitter.com/B_Anbar/status/1087787095748423687)):

*The aim of this project is to integrate all the process into a QGIS plugin such that whenever the user inputs a shp file, the MST is provided back.*

![MST of Turkish Cities](https://pbs.twimg.com/media/DxiXP_WX0AEZrHp.jpg)


![MST of districts](https://pbs.twimg.com/media/Dz--HO9X0AEYTZn.jpg:large)



