### Overview
This was written to do 1 thing, import Scan My Tesla log files, to InfluxDB
https://sites.google.com/view/scanmytesla/home

Support csv only

### Usage
# Single Files
Run parse.py with the first argument the file to be imported
*python3 parse.py filename.csv*

# All Files
Place all csv logs into the 'logs' folder.
Running all.py will import all csv logs in the logs folder.
After a file has been imported, it is moved to the imported folder.
*python3 all.py*

### Notes
Filename must be unaltered

Influx Server is assumed to be on the same machine (localhost)
No Username or Passwork, Default port, and database name of SMT

If you want custom influx server settings they are set at the top of the script.

Only tested on linux.