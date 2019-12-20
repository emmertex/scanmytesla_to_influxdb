import os
import time
import sys
import csv
from datetime import datetime
from influxdb import InfluxDBClient, SeriesHelper

def smt2i(filename):
    influxdbname = "SMT"
    influxdbip = "localhost"
    influxdbport = 8086
    influxdbuser = ""
    influxdbpass = ""

    iclient = InfluxDBClient(influxdbip, influxdbport, influxdbuser, influxdbpass, influxdbname)

    processed = 0

    name = filename.split(" ")
    named = name[1]
    name = name[2].split(".")
    namet = name[0]
    dt = (datetime.strptime(named + ' ' + namet, '%Y-%m-%d %H-%M-%S'))

    starttime = datetime.timestamp(datetime.now())
    

    with open(filename) as can_log:
        reader = csv.reader(can_log, delimiter=',')
        line = 0
        items = 0
        headers = []
        joinedstring = ""
        for row in reader:
            if line == 0:
                items = len(row) - 1
                headers = row[:items]
                count = 0
                for header in headers:
                    headers[count] = header.replace(" ", "_")
                    count += 1
            else:
                string = ""
                itemid = 0
                try:
                    firstitem = True
                    for item in row:
                        if not (item == "") and not (item == "Infinity") and not (item == "NaN"):
                            if firstitem:
                                string += "tesla {}={}".format(headers[itemid], item)
                                firstitem = False
                            else:
                                string += ",{}={}".format(headers[itemid], item)
                        itemid += 1
                except:
                    print("broken row")
                if itemid > 1:
                    string += " {}".format(int((datetime.timestamp(dt) * 1000) + (int(row[0]))))
                    joinedstring += string + "\n"
        
            line += 1
            processed += 1
            if (processed % 1000 == 0):
                #print (joinedstring)
                httpheaders = { 'Content-type': 'application/octet-stream', 'Accept': 'text/plain' }
                response = iclient.request("write",'POST', {'db':influxdbname, 'precision':'ms'}, joinedstring.encode('utf-8'), 204, httpheaders)
                joinedstring = ""
                #print (response)
                print ("Processed {} rows in {} seconds\r".format(processed, datetime.timestamp(datetime.now()) - starttime), end="")
        
        httpheaders = { 'Content-type': 'application/octet-stream', 'Accept': 'text/plain' }
        response = iclient.request("write",'POST', {'db':influxdbname, 'precision':'ms'}, joinedstring.encode('utf-8'), 204, httpheaders)
        print ("\r\nCompleted {} rows in {} seconds".format(processed, datetime.timestamp(datetime.now()) - starttime))

if __name__ == "__main__":
    smt2i(sys.argv[1])


