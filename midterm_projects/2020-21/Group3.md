# QGIS Plugin Group 3 
<h1> Authors </h1>
Fatih Afacan <br>
Abdülkadir Çakır

<h1> Our plugin`s User Interface </h1>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/XpgJ5S5/1.png" alt="1" border="0" /></a>

## How did we manage to do No ID panel:
```
if useID:
	lineLayer.dataProvider().addAttributes([QgsField('id_start', QVariant.Double),QgsField('id_end', QVariant.Double),QgsField('length', QVariant.Double)])
  else:
  	lineLayer.dataProvider().addAttributes([QgsField('length', QVariant.Double)]) 
```		
There is an output for No ID attribute table:<br>
<a href="https://ibb.co/zZ2gh15"><img src="https://i.ibb.co/Rc6Kp1S/2.png" alt="2" border="0" /></a>


<h1> Algorithm </h1>
Our algorithm able to classify the points with K means algorithm. So you can use this tool for classify the points for any case. For example If are the cargo manager and you want to make a save for fuel prices. This algorithm can save you. You can upload the data of customers location and you can select the how many cluster you wanted for. So you can make classification with them to your profit. You can open the department in the middle of the cluster or you can seperate the clusters and send the cargo cars to every cluster.
<br>
As you can see the clusters and points. You can manage anything you want with this data according to your imagination. <br>
<a href="https://ibb.co/vkHh3GM"><img src="https://i.ibb.co/SBPct8Z/3.png" alt="3" border="0" /></a>

<h1> Min Max distance calculator </h1>
Our plugin also able to calculate the minimum and maximum distance from the points that in uploaded data. <br>
<a href="https://ibb.co/Wn2B0r8"><img src="https://i.ibb.co/kKSqJLb/Ekran-Al-nt-s.png" alt="Ekran-Al-nt-s" border="0" /></a> <br>
You can see the visualized lines that the maximum distance of the points. <br>
<a href="https://ibb.co/NLhrNRX"><img src="https://i.ibb.co/7GcQphH/5.png" alt="5" border="0" /></a> <br>
And you can check the points and distances in the attribute table.
