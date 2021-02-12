# Unit Test
* Steps:
  1. Adjust the `compile.bat` file under the plugin.
  2. Run `compile.bat` from your command window.
  3. Set the Python path: `set "PYTHONPATH=C:\OSGeo4W64\apps\qgis\python;%PYTHONPATH%"`
  4. Set the Qt Path: `set "QT_QPA_PLATFORM_PLUGIN_PATH=C:\OSGeo4W64\apps\Qt5\plugins"`
  4. QGIS has the nose module. Run `python -m nose2 -v`.
* Important: Understand the difference between **error** and **failure**.


## References
* [Unit Tests in Python](https://youtu.be/6tNS--WetLI)
* [Writing unit tests for QGIS Python plugins](https://snorfalorpagus.net/blog/2014/01/04/writing-unit-tests-for-qgis-python-plugins/)
