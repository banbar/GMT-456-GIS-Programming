<h1> Language Support (Internationalization) For Plugins </h1>
This markdown file shows how to internationalize your plugin with other languages. 
First of all we need to download qt and qtlinguist for using lupdate and lrelease functions. 

After that create new .pro file in our plugin`s i18n folder. 

<img src = "https://github.com/Afacaann/GIS-Programming/blob/main/1.PNG" width ="500" />
Our .pro file need to be like that. Sources shows our main .py file , forms shows our user interface file , translations shows which language our plugin language support. 
Languages part needs to be with .ts format because qt linguist is working with .ts file format. 
After that we open qt shell and define our i18n file path.
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
