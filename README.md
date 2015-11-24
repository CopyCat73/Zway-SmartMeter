# Zway SmartMeter

Zway Automation module for energy devices based on smart meter input
Gauge icons (c) Rich Dellinger http://richd.com

# Configuration

Add a device for each value from the smart meter you want to display, e.g. "Current usage,"
"Total usage", "Current return", etc. Make a note of the ID for these devices, e.g. SmartMeter_14.

Put the python script in a directory on the machine that logs your smart meter via the USB smart
meter cable. Set zwayserver, username and password variables to your own specifications in the
smartmeter.py file. Near the end of the file the values for current usage and return are uploaded
to devices SmartMeter_23 and SmartMeter_24. Change these devices to your own device ID's and copy the
upload lines to the other smart meter readouts if needed.

Add the script to your crontab (type "crontab -e") for the interval you want to run it, e.g.:
 "*/1 * * * * python /home/youruser/smartmeter.py" (without the quotes)
 This example runs the script every minute and uploads the data to the zway device(s).
 
 The icon shows three different states; green, yellow and red. In the module preferences the
 threshold for medium and high can be set; if set to 200 and 500, a readout smaller than 200
 will display green, 200-500 yellow, above 500 red. 



# License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any 
later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
