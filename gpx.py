import sys
if sys.version_info[0] < 3:
     print ("Please run again using Python 3")
     exit()
try:
    import gpxpy
    import gpxpy.gpx
except:
    print ("Please install gpxpy library")
    print ("  pip3 install gpxpy")
    print ("https://github.com/tkrajina/gpxpy")
    exit()
import time
from datetime import datetime
import pytz
try:
    from influxdb import InfluxDBClient, SeriesHelper
except:
    print ("Please install influxdb library")
    print ("  pip3 install influxdb")
    exit()  

def gpx2i(filename):
    influxdbname = "SMT"
    influxdbip = "localhost"
    influxdbport = 8086
    influxdbuser = ""
    influxdbpass = ""

    iclient = InfluxDBClient(influxdbip, influxdbport, influxdbuser, influxdbpass, influxdbname)


    gpx_file = open(filename, 'r')

    gpx = gpxpy.parse(gpx_file)

    


    for track in gpx.tracks:
        for segment in track.segments:
            string = ""
            for point in segment.points:
                dt = int((point.time - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds()) * 1000
                string += "track lat={},lon={},ele={} {}\n".format(point.latitude, point.longitude, point.elevation, dt)
            httpheaders = { 'Content-type': 'application/octet-stream', 'Accept': 'text/plain' }
            response = iclient.request("write",'POST', {'db':influxdbname, 'precision':'ms'}, string.encode('utf-8'), 204, httpheaders)
            print (response)
   

if __name__ == "__main__":
    gpx2i(sys.argv[1])