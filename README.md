# py_interpol_demo

Collection of scripts to compute basic spatial interpolation such as Inverse Distance Weighting (IDW) in Python

Example notebooks load current weather data fro mthe Estonian Weather Service, interpolate onto Estonia and export as tif-raster:

For air temperature:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/allixender/py_interpol_demo/master?filepath=interpol_temperature.ipynb)

For precipitation:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/allixender/py_interpol_demo/master?filepath=interpol_precip.ipynb)

Most important Python packages: `numpy`, `scipy`, and `gdal` (see examplary `conda`-based `environment.yml` file)
