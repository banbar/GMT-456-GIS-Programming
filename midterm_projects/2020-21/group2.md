# Group 2
***Authors***   
Ahmet Fırat Karaoğlu : karaoglu@email.com  
Metehan Ergen : metehan.ergenn@gmail.com  

Hello everyone ! we have contributed new features to a QGIS plugin called "save_attributes". You may find a brief information about the plugin below,  

***Interface***   
<img src = "https://github.com/afkHub/GMT-456-GIS-Programming/blob/master/midterm_projects/2020-21/img/group2-images/GUI.png" width ="500" />  

You could select the shapefile from the interface (Input layer part). And there will be 3 main cases,

***Case 1*** <br/>If the input layer geometry is line; the plugin will compute the shortest and real distance among features, azimuth and reverse azimuth between lines' start points and end points. And also draw the shortest line with its length. See below,  

<img src = "https://github.com/afkHub/GMT-456-GIS-Programming/blob/master/midterm_projects/2020-21/img/group2-images/line_1feat.JPG" width ="500" /><br/><img src = "https://github.com/afkHub/GMT-456-GIS-Programming/blob/master/midterm_projects/2020-21/img/group2-images/lines_attr.JPG" width ="350" />         

If there is more than one feature on layer. It will also show the features which could possibly be a polygon.    
<img src = "https://github.com/afkHub/GMT-456-GIS-Programming/blob/master/midterm_projects/2020-21/img/group2-images/line_mult.JPG" width ="450" /><br/><img src = "https://github.com/afkHub/GMT-456-GIS-Programming/blob/master/midterm_projects/2020-21/img/group2-images/azimuth.png" width ="450" />  

***Case 2*** <br/>If the input layer is point. It will check whether feature number is greater than 2. If it is the case, it  will calculate the minimum and maxiumum distannce among all points and draw the lines related to them. See below,      

<img src = "https://github.com/afkHub/GMT-456-GIS-Programming/blob/master/midterm_projects/2020-21/img/group2-images/minmax.JPG" width ="500" /><br/><img src = "https://github.com/afkHub/GMT-456-GIS-Programming/blob/master/midterm_projects/2020-21/img/group2-images/point_attr.JPG" width ="430" />

***Case 3*** <br/>If the input layer is polygon, the plugin computes the area and perimeter of the poligons and show in the table with inserting.
![Image](https://github.com/afkHub/GMT-456-GIS-Programming/blob/master/midterm_projects/2020-21/img/group2-images/area-peri.png)


<br/><br/><br/>Note: We used this to be able to add our university logo to the GUI: https://gis.stackexchange.com/questions/381661/image-adding-problem-to-qgis-plugin-gui-with-qt-designer (You may need to run the "compile.bat" file in the folder according to you for the logo.)











