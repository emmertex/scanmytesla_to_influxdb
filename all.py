import os
from smt import smt2i
from gpx import gpx2i
import shutil
import config

for file in os.listdir("./logs"):

    if file.endswith(".gpx"):
        index = 0
        while index < config.influxdbnumber:
            filename = os.path.join("./logs", file)
            print ("Running {} into DB {}".format(filename, config.influxdbip[index]))
            gpx2i(filename, index)
            index += 1
        print ("Moving {} to completed folder".format(filename))
        shutil.move(filename, os.path.join("./imported", file))

    if file.endswith(".csv"):
        index = 0
        while index < config.influxdbnumber:
            filename = os.path.join("./logs", file)
            print ("Running {} into DB {}".format(filename, config.influxdbip[index]))
            smt2i(filename, index)
            index += 1
        print ("Moving {} to completed folder".format(filename))
        shutil.move(filename, os.path.join("./imported", file))