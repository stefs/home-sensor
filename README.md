# Kaloix Sensor System
> This project was made with only personal use by me in mind. Code is not commentated, probably bad structured and containes German language.

## Sensor
### Features
* Import relevant sensors from `config.json`
* Collect and parse sensor data using a file system interface
* Export data as CSV files to folder `csv/`
* Copy these files to the server, when new data is available

### Usage
    ./sensor.py <station>

The *station* parameter corresponds with the same field in the sensor list of `config.json`.

## Server
### Features
* Import sensor list from `config.json`
* Monitor directory `csv/` for new sensor data
* Send admin email on missing sensor updates and crash
* Send user email on out of range sensor values
* Generate `index.html` document with sensor values from `template.md` and `template.html`
* Generate `plot.png` with sensor history
* Copy these files in webserver directory

### Installation
    pip install virtualenv
    virtualenv --python=python3 ve/
    source ve/bin/activate
    pip install matplotlib markdown
    deactivate

### Usage
    source ve/bin/activate
    ./server.py
    deactivate

## Acknowledgements
* Python module [matplotlib](http://matplotlib.org/index.html) for generation of plots
* File `favicon.png` from [VeryIcon.com](http://www.veryicon.com/icons/system/icons8-metro-style/measurement-units-temperature.html) with license *Free for non-commercial use*

## Copyright
Copyright © 2015 Stefan Schindler  
Licensed under GNU GPL v3
