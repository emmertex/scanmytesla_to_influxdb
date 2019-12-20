import os
from parse import smt2i
import shutil

for file in os.listdir("./logs"):
    if file.endswith(".csv"):
        filename = os.path.join("./logs", file)
        print ("Running {} ".format(filename))
        smt2i(filename)
        print ("Moving {} to completed folder".format(filename))
        shutil.move(filename, os.path.join("./imported", file))