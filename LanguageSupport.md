<h1> Language Support (Internationalization) For Plugins </h1>
This markdown file shows how to internationalize your plugin with other languages. 
First of all we need to download qt and qtlinguist for using lupdate and lrelease functions. 

After that create new .pro file in our plugin`s i18n folder. 

<img src = "https://github.com/Afacaann/GIS-Programming/blob/main/1.PNG" width ="500" />
Our .pro file need to be like that. Sources shows our main .py file , forms shows our user interface file , translations shows which language our plugin language support. 
Languages part needs to be with .ts format because qt linguist is working with .ts file format. 
After that we open qt shell and define our i18n file path.

**Be sure to name the ts file like your_plugin_ + language + .ts otherwise the language loading will fail! Use 2 letters shortcut for the language (it for Italian, de for German, etc...)**

<img src = "https://github.com/Afacaann/GIS-Programming/blob/main/2.PNG" />
Write command like "lupdate saveattributes.pro".  You need to write your .pro file name that you choose.
<img src = "https://github.com/Afacaann/GIS-Programming/blob/main/3.PNG" width ="500" />
After we run this command our .ts file has created in our i18n folder. 
We need to open this .ts file in qt linguist and make translations. 
<img src = "https://github.com/Afacaann/GIS-Programming/blob/main/4.PNG" width ="500" />
After we translate our text we save .ts file in qt linguist and we run command like "lrelease saveattributes.pro" in qt shell and this fuction create .qm file of our translation. 

This .qm file is the only file that QGIS need for language support. 

So you have the language support for language that you choose.

<h1> References </h1>

You can download qt from https://www.qt.io/download .
You can download qt linguist from https://github.com/lelegard/qtlinguist-installers/releases .


# LANGUAGE SUPPORT
  
In order to add Language Support feature in the plugin (The name of the plugin we created is **FinalProject** ), the following steps are done:
  
  - A .pro file to be managed by [QT Linguist](https://github.com/thurask/Qt-Linguist/releases/tag/20211214) is in the i18n folder in the plugin directory where Translation related files will be found.
should be created. The contents of the FinalProject.pro file should be as follows:
  
```
FORMS = C:\Users\kfyka\OneDrive\Belgeler\finalproject\FinalProject_dialog_base.ui
SOURCES = C:\Users\kfyka\OneDrive\Belgeler\finalproject\FinalProject.py
TRANSLATIONS = FinalProject_tr.ts
```   
<p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_1.png"/>
</p>  
  
  
 - After creating the **FinalProject.pro** file, the .ts file should be created. The file to be created must be located in the i18n folder. The point to be considered while creating the **.ts file** is that it should be created as **your_plugin_language.ts**. The language to be translated should be written as an abbreviation to the place specified as language here. The .ts file to be created for the Turkish language in the FinalProject plugin is **FinalProject_tr.ts**. To create the **FinalProject_tr.ts** file, the following command should be run by going to the i18n folder in the plugin directory in the terminal:
  
```
pylupdate5 your_plugin.pro
```  
<p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_2.png"/>
</p>   

After running this command, the .ts file will appear in the i18n folder.
  
- The application called **QT Linguist** is used to create the content of the .ts file. With this application, the translation of the parameters in the plugin interface with the specified language is performed.
  
- Run the **QT Linguist** and **"File"** ----> **"Open..."**
  
  <p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_3.png"/>
</p> 
  
- Choose the **FinalProject_tr.ts** file and **"Open"**
  
  <p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_4.png"/>
</p> 
  
- Choose the target language.
  
  <p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_5.png"/>
</p> 
  
 - Choose the Sting from the **"Strings"** label and write the **"Translation to Türkçe (Türkiye)"**
  
  <p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_6.png"/>
</p> 
  
 - After all the words are translated, the **"Strings"** menu should look like this.
  
  <p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_7.png"/>
</p> 
  
- After the conversion process is completed, we save the file. **"File"** -----> **"Save"**
  
<p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_8.png"/>
</p> 
    
- Another file to be created is the .qm file. To create this file, select the **"Release"** option from the **"File"** menu in the **QT Linguist** application.
  
<p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_9.png"/>
</p> 
  
- Process completed. If your language is Turkish you will see this screen.
  
 <p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/Language_10.png"/>
</p> 
  
- If your language is English you will see this screen.
  
 <p align="center">
  <img src="https://github.com/GMT-456-GIS-Programming/qgis-plugin-2/blob/main/qgis_plugin_ss/interface.jpg"/>
</p>

## REFERENCES
[QGIS Documentation for Language Support in Plugins](https://docs.qgis.org/3.16/tr/docs/pyqgis_developer_cookbook/plugins/plugins.html#translation)
You can download qt from https://www.qt.io/download .
You can download qt linguist from https://github.com/thurask/Qt-Linguist/releases/tag/20211214.
