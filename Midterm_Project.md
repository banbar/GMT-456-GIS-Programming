# Midterm Project Guidelines 
# Due: 3 December


Fork the course’s [**GitHub page**](https://github.com/banbar/GMT-456-GIS-Programming). You may start investigating the QGIS plugin under the `save_attributes/` folder.

The GUI of the plugin is as follows:
![](file://E:/Google Drive/GMT_456_GIS Programming/GitHub_Page/img/gui_save_attributes.png)

At the moment, this plugin adds two attributes (X and Y) to a point shp file and populates them by inserting the relevant values corresponding to each feature. 

The objective of the midterm project is to update the plugin such that the following requirements are satisfied:

* If a ***point*** shp file file is provided, it will identify the distances between all features (points). 
* The plugin will then ***create a new line shp file***, which provides the details of the **two special lines** (i.e. the min/max distance between the two closest/distant points, where the distance is calculated as the shortest distance between two points).  
   * Template of the resulting line shp file looks like:
      
| optional            |                   |                                                |
|---------------------|-------------------|------------------------------------------------|
| poi\_id\_start      | po\_id\_end       | length                                         |
|     shortest\_start |     shortest\_end |     distance between two closest pairs         |
|     longest\_start  |     longest\_end  |     distance between two most distant pairs    |