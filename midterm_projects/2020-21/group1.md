#  QGIS Plugin Development Group 1 Document
---
### Members involved in the development phase

* Berkay İbiş  
Mail address: berkayyibis@hotmail.com

* Berk Kıvılcım  
Mail address: brkkvlcm@gmail.com

---
### Graphical User Interface of the Plugin
#### Parts of the GUI (Graphical User Interface)
**1 - Line Label:** Line Labels just some string that give us information about other parts of the gui which is means line label does not run any function.

**2 - Line Edit:** Line Edits show us the directory and name of the files which is selected by Push and Tool Buttons.

**3 - Push Button:** Push buttons run the functions and algorithms when it clicked.

**4 - Combo Box:** Combo boxes work for selecting correct options. This correct options like 'only point layer' listed in combo boxes and we can select the which layer we want to use.

**5 - Layout:** Layout limits frame size of the gui so we can't make gui page smaller then selected layout frame. GUI example below here is the smallest interface according to layout.

<p align="center"><img src="https://github.com/axecasper/GMT-456-GIS-Programming/blob/patch-1/midterm_projects/2020-21/img/group1-images/group_1_3.jpg" width="100%"></p>

---
### Functions and Details About Plugin
#### Inputing Only Line and Point files:

* Code's input_shp_file function upload a shape file into the QGIS but we don't want to upload any polygon type file so we limited it and when we try to upload a polygon file it will give us some error message.

* The code part and the error example is below here.

```python
if(self.layerDef.GetGeomType() == ogr.wkbPolygon):#
  self.error_msj("Sadece çizgi veya nokta katmanı girebilirsiniz !")
  self.dlg.lineEdit.setText("")
  return False
```

<img src="https://github.com/axecasper/GMT-456-GIS-Programming/blob/patch-1/midterm_projects/2020-21/img/group1-images/group_1_4.jpg" width="40%">

---

#### Run Button and Combo Box Relation:

* When we click to Run button plugin will implement some algorithm on the layer which is selected on combo box. We want to implement it on only point layers so combo box must shuw only the point layers.

* The code part and example result below here. Also  in the 'geometryType()== 0' 0(zero) means point type layer. 

```python
try:
  if layer.geometryType() == 0:              
    layersList.append(layer.name())
    layersList_shp.append(layer)
                            
except:
  continue
```

* Combo box not allow to select c_beytepe layer below here because its a line type layer. 
<img src="https://github.com/axecasper/GMT-456-GIS-Programming/blob/patch-1/midterm_projects/2020-21/img/group1-images/group_1_5.jpg" width="60%">

---

#### Drawing New Layer in all type of CRS:
* The Algorithms in the plugin create new layers and drawing some point or lines. In the beginning it only draw on QGIS's default crs. We identify crs as source crs instead of qgis default crs. That means we additionaly add 'crs=self.vlayer.sourceCrs()'. The code example is below here.

```python
lineLayer = QgsVectorLayer("MultiLineString", "lines", "memory", crs=self.vlayer.sourceCrs())
```

---

#### Algorithms:

#### Drawing lines between closest and farthest two points.
* When we select a point layer in combo box and click to run the plugin create a new line layer which is shows distance between closest and farthest two points.

* Visual example and Attribute tables of the new line layer below here. This Attribute table include start and end point's id and distance between them. 

<img src="https://github.com/axecasper/GMT-456-GIS-Programming/blob/patch-1/midterm_projects/2020-21/img/group1-images/group1_7.jpg" width="55%">

<img src="https://github.com/axecasper/GMT-456-GIS-Programming/blob/patch-1/midterm_projects/2020-21/img/group1-images/group1_6.jpg" width="70%">

---

#### Finding and drawing center point between this farthest two points.
* The code calculate it with getting x and y coordinates of the start and end points. Then getting avarage of the x and y. It give us new center point coordinates. Then we add it to created point layer.

```python
baslangicx=lineStart.x()
baslangicy=lineStart.y()
bitisx=lineEnd.x()
bitisy=lineEnd.y()

ortX=(baslangicx+bitisx)/2
ortY=(baslangicy+bitisy)/2

segMid=QgsFeature()
segMid.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(ortX,ortY)))
```

<img src="https://github.com/axecasper/GMT-456-GIS-Programming/blob/patch-1/midterm_projects/2020-21/img/group1-images/group1_8.jpg" width="70%">

---

#### Finding and drawing break points of the Multi Line String:

* When we click to OK button the algorithm starts and draw the break points on the Multi Line Strings. It work in a for loop until the multi line string complate.

```python
vertex=[]
for i in range(len(geom.constGet()[0])):
  pt = geom.constGet()[0][i]
  vertex.append(pt)
  i+=1
                            
print(vertex)

                        
v1= QgsVectorLayer("Point", "point", "memory",crs = self.vlayer.sourceCrs())
                        
for i in range(len(vertex)):
  pr = v1.dataProvider()
  f = QgsFeature()
  f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(vertex[i])))
  pr.addFeatures( [f] )
  v1.updateExtents()
                            
QgsProject.instance().addMapLayers([v1])
v1.commitChanges()                        
```

<img src="https://github.com/axecasper/GMT-456-GIS-Programming/blob/patch-1/midterm_projects/2020-21/img/group1-images/group1_11jpg.jpg" width="100%">

---
