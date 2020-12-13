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
