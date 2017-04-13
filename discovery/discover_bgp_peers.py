#!/usr/bin/env python

from pybird import PyBird
from pprint import pprint

pybird = PyBird(socket_file='/var/run/bird/bird.ctl')

peers = pybird.get_peer_status()
lineiterator = iter(peers)

first = True

print "{\t\"data\":[" 

for peer in lineiterator:

    if "description" in peer:
       if not first:
	  print ","

       print "\t\t{\"{#PEERNAME}\":\"%s\", \"{#PROTONAME}\":\"%s\" }" % (peer["description"], peer["name"])
       first = False

print "\t]}"
