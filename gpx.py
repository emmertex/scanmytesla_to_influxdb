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
import config

def gpx2i(filename, cid):

    iclient = InfluxDBClient(config.influxdbip[cid], config.influxdbport[cid], config.influxdbuser[cid], config.influxdbpass[cid], config.influxdbname[cid])


    gpx_file = open(filename, 'r')

    gpx = gpxpy.parse(gpx_file)

    


    for track in gpx.tracks:
        for segment in track.segments:
            string = ""
            for point in segment.points:
                dt = int((point.time - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds()) * 1000
                string += "track lat={},lon={},ele={} {}\n".format(point.latitude, point.longitude, point.elevation, dt)
            httpheaders = { 'Content-type': 'application/octet-stream', 'Accept': 'text/plain' }
            response = iclient.request("write",'POST', {'db':config.influxdbname[cid], 'precision':'ms'}, string.encode('utf-8'), expected_response_code=204, headers=httpheaders)
            print (response)
   

if __name__ == "__main__":
    if len(sys.argv) > 2:
        gpx2i(sys.argv[1], int(sys.argv[2]))
    else:
        print ("Database not selected, using index 0")
        gpx2i(sys.argv[1], 0)
