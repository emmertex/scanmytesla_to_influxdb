# Overview
Imports "Scan My Tesla" CSV Logs and GPX Tracks into InfluxDB

https://sites.google.com/view/scanmytesla/home

# Usage

## Configuration
Settings for influxdb are stored in *config.py*
Default is "localhost" for influxdb server, SMT database, no username, and no password

## Scan My Tesla logs
Run smt.py with the first argument the file to be imported
*python3 smt.py filename.csv*

## GPX Track Logs
For GPX Tracks I use OSMAnd+, but it should work with any GPX Track
*python3 gpx.py filename.gpx*

## Batch Import of All Files
Place all csv and gpx logs into the 'logs' folder.
Running all.py will import all logs in the logs folder.
After a file has been imported, it is moved to the imported folder.
*python3 all.py*

### Notes
Scan My Tesla Filename must be unaltered

Only tested on linux, should work on anything.