# Software Documentation
Documentation of a developed software is of critical importance in terms of its outreach. The users will keep on using the sofware as long as they can follow a well-structured text.

These markdown files are good way to start documenting our software. However, they are not suitable once we want to provide the documentation in multiple languages and also include the function descriptions in an automatic way.

The Pythonic way of documenting software is to use [Sphinx](https://www.sphinx-doc.org/en/1.8/index.html).


## Why Sphinx?
* One of the state-of-the-practice tools to document software.
* [Variety of projects](https://www.sphinx-doc.org/en/1.8/examples.html) have already been relying on Sphinx for documentation. Some notable examples include [**QGIS**](https://qgis.org/en/docs/index.html), [**NetworkX**](https://networkx.org/) and [**Flask**](https://flask.palletsprojects.com/en/1.1.x/). Even books were written using Sphinx, such as [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/). Maybe we would better understand the importance of 42. :)

## How to document our code?

1. Install Sphinx
   * `pip install sphinx`. If you are using Anaconda: `conda install sphinx`.
2. Go to your project folder and create a `sources` subfolder and add your **.py** files under this folder.
3. In the Command Line Interface (CLI), write `sphinx-quickstart` while you are under your project folder.
4. Provide the details regarding your project. The default values are labelled as within square brackets.
5. Update the `conf.py`.
  * Uncomment:
      * `import os`
		  * `import sys`
		  * `sys.path.insert(0, os.path.abspath('.'))`
  * Add the folder that contains the **.py** files (i.e. ***sources***) to the sys.path:
     * `sys.path.append('sources') under sys.path`
  * Update the **extensions** list to:
     * `extensions = ['sphinx.ext.autodoc']`
  * Under **index.rst**:
     * Add `docs/save_attributes`
  * At CLI type:
     * `mkdir docs`
     * `sphinx-apidoc -o docs sources`
     * `make html`
6. [optional] - Autobuilding (simultaneous update of the documentation as you update the software):
   * Install the **sphinx-autobuild** package: `pip install sphinx-autobuild`.
   * At CLI, type:
      * `sphinx-autobuild . _build/html`
      * ???: https://pypi.org/project/sphinx-autobuild/ (to see changes in google) or just type http://127.0.0.1:8000
   * To shut down the server (???: when did we start it?): **Ctrl + C**.

* Sphinx provides beautiful themes. These themes could be [browsed](https://sphinx-themes.org/).
* You can also install, for example the [Read the Docs (rtd)](https://github.com/readthedocs/sphinx_rtd_theme), theme, by `pip install sphinx-rtd-theme`.
* To enable a theme, under the **conf.py**, update the `html_theme` accordingly (e.g. `html_theme = 'sphinx_rtd_theme'`).

## References

* https://www.youtube.com/watch?v=LQ6pFgQXQ0Q&ab_channel=EngineeringAnywhere
* https://www.youtube.com/watch?v=d_XeV6oyNvI&ab_channel=%7BLP%7DWITHRAHMAT
