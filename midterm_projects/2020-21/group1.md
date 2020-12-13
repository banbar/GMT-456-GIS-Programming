#  QGIS Plugin Development Group 1 Document
---
### Members involved in the development phase

* Berkay İbiş  
Mail address: 

* Berk Kıvılcım  
Mail address: brkkvlcm@gmail.com

---
### Graphical User Interface of the Plugin
#### Parts of the GUI (Graphical User Interface)
**1 - Line Label:** Line Labels just some string that give us information about other parts of the gui which is means line label does not run any function.

**2 - Line Edit:** Line Edits show us the directory and name of the files which is selected by Push and Tool Buttons.

**3 - Push Button:** Push buttons run the functions and algorithms when it clicked.

**4 - Combo Box:** Combo boxes work for selecting correct options. This correct options like 'only point layer' listed in combo boxes and we can select the which layer we want to use.

**5 - Layout:** Layout limit to frame of the gui so we can't make gui page smaller then selected layout frame.

<p align="center"><img src="https://github.com/axecasper/GMT-456-GIS-Programming/blob/patch-1/midterm_projects/2020-21/img/group1-images/group_1_3.jpg" width="100%"></p>

---
### Functions and details About Plugin
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

