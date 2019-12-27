# Enter number of databases to push data to  
# If this is less than the length of the list, it will stop at this index -1
# If it is greather than list length, you break things!
influxdbnumber = 1

# Enter database details, as a list, example

#influxdbnumber = 2
#influxdbname = ["tesla", "SMT"]
#influxdbip = ["192.168.0.100", "127.0.0.1"]
#influxdbport = [8086, 8086]
#influxdbuser = ["tesla", ""]
#influxdbpass = ["password", ""]

# Default for 1 database
influxdbname = ["SMT"]
influxdbip = ["127.0.0.1"]
influxdbport = [8086]
influxdbuser = [""]
influxdbpass = [""]