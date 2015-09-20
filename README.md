# Kaloix Sensor System
> **Notice:** This project was made with only personal use by me in mind. Code
> is not commentated, maybe bad structured and the user interface is in German
> language.

## Client
### Features
* Import relevant sensors from `sensor.json`
* Collect and parse sensor data using a file system interface
* Export data as CSV files to folder `csv/`
* Copy these files to the server, when new data is available

### Installation
1. The base platform is  **Debian Jessie** with **Python 3.4**. Install German
   locale by uncommenting `de_DE.UTF-8 UTF-8` in `/etc/locale.gen` and run
   `sudo locale-gen`.

2. 1-Wire temperature sensor:

		modprobe w1-gpio
		modprobe w1-therm

3. Optical character recognition of seven segment display with [ssocr](https://www.unix-ag.uni-kl.de/~auerswal/ssocr/):

		sudo apt-get install fswebcam libimlib2 libimlib2-dev python3-numpy
			python3-scipy python3-pil
		wget "https://www.unix-ag.uni-kl.de/~auerswal/ssocr/ssocr-2.16.3.tar.
			bz2"
		bzip2 --decompress ssocr-2.16.3.tar.bz2
		tar --extract --file ssocr-2.16.3.tar
		rm ssocr-2.16.3.tar
		make --directory ssocr-2.16.3/ ssocr
		ln --symbolic ssocr-2.16.3/ssocr

4. Usage:

		./client.py <station>

	The *station* parameter corresponds with the same field in the sensor list
	of `sensor.json`.

## Server
### Features
* Import sensor list from `sensor.json`
* Monitor directory `csv/` for new sensor data
* Send admin email on missing sensor updates and crash
* Send user email on out of range sensor values
* Generate `index.html` document with sensor values from `template.md` and `template.html`
* Generate `plot.png` with sensor history
* Copy these files in webserver directory

### Usage
	cp static/* <web_dir>
	pip install virtualenv
	virtualenv --python=python3 ve/
	source ve/bin/activate
	pip install markdown matplotlib pytz
	./server.py
	deactivate

## Acknowledgements
* File `static/favicon.png` from
  [VeryIcon.com](http://www.veryicon.com/icons/system/icons8-metro-style/measurement-units-temperature.html)
  with license *Free for non-commercial use*

## Copyright
Copyright © 2015 Stefan Schindler  
Licensed under the GNU General Public License v3
