**GMT 456 – GIS Programming**

**2020 – 21 Fall**

**Midterm Project Guidelines**

Fork the course&#39;s [GitHub page](https://github.com/banbar/GMT-456-GIS-Programming). You may start investigating the QGIS plugin under the save\_attributes/ folder.

The GUI of the plugin is as follows:

![](RackMultipart20201109-4-o2mjhs_html_929128409445cf17.png)

At the moment, this plugin adds two attributes (X and Y) to a point shp file and populates them by inserting the relevant values corresponding to each feature.

The objective of the midterm project is to update the plugin such that the following requirements are satisfied:

- If a _ **point** _ shp file file is provided, it will identify the distances between all features (points). The plugin will then create a _ **new line shp file** _, which provides the details of the two special lines (i.e. the min/max distance between the two closest/distant points, where the distance is calculated as the shortest distance between two points).
  - Template of the resulting line shape file looks like:

| _Optional_ |
 |
| --- | --- |
| **id\_start** | **id\_end** | **Length** |
| id1\_shortest | id2\_shortest | distance between two closest pairs |
| id2\_longest | id2\_longest | distance between two most distant pairs |

  - If the user provided an id field corresponding to each point feature, then the start and end points of these two special lines are recorded as shown in the first two columns.
  - If there is no such id field, the user will check the box &#39;No ID&#39;, and then only the length of the lines are recorded. That&#39;s why the first two fields (id\_start and id\_end) are optional.
- If a _ **polyline** _ shapefile is provided, it will add two attributes (fields) to the shp file.
  - The first attribute is _ **length** _, which records the length of the polyline.
  - The second attribute is _ **shortest\_length** _, which first identifies the start and end points of a polyline, and records the shortest distance between these two points.
- If a _ **polygon** _ shapefile is provided, provide a gentle warning to the user stating that the plugin cannot operate on polygons.

You need to consider the following adjustments to increase the quality of your plugin:

1) Add a control statement that checks whether a new field that you define is already present? If the new field(s) are present, there is no need to add once more. This will be useful when debugging the code multiple times, and prevent situations like this in which we add the same attributes (i.e. x and y) multiple times:

![](RackMultipart20201109-4-o2mjhs_html_9b9b6c534c879f6c.png)

2) At the moment, the plugin adds the X and Y fields regardless of the input geometry. Make sure that the new fields that you will be adding are specific to the input geometry.

3) Investigate ways in which to increase the quality of the GUI layout. At the moment, the _ **horizontal layout** _ is not correctly structured, so that the &quot;browse&quot; button takes more space than it should. Can you also identify other aspects which increases the quality of the GUI?

![](RackMultipart20201109-4-o2mjhs_html_25258d5a006e21ad.png)
