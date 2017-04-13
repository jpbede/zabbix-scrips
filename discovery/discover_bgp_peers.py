#!/usr/bin/env python

from pybird import PyBird
import argparse

parser = argparse.ArgumentParser(description='Discover bgp peers')
parser.add_argument('--inet', nargs='?', const="all", type=str, default="all", help='4, 6, all - which peers do you want')
args = parser.parse_args()

peergroup = {}

if args.inet == "4" or args.inet == "all":
    pybird4 = PyBird(socket_file='/var/run/bird/bird.ctl')
    peergroup["4"] = pybird4.get_peer_status()


if args.inet == "6" or args.inet == "all":
    pybird6 = PyBird(socket_file='/var/run/bird/bird6.ctl')
    peergroup["6"] = pybird6.get_peer_status()

first = True

print "{\t\"data\":[" 

for inet, peers in peergroup.iteritems():
    peeriterator = iter(peers)
    
    for peer in peeriterator:
       if "description" in peer:
           if not first:
	      print ","

           print "\t\t{\"{#PEERNAME}\":\"%s\", \"{#PROTONAME}\":\"%s\", \"{#INET}\":\"%s\" }" % (peer["description"], peer["name"], inet)
           first = False

print "\t]}"
