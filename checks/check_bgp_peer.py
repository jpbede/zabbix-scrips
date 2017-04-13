#!/usr/bin/env python

from pybird import PyBird
import argparse

parser = argparse.ArgumentParser(description='Discover bgp peers')
parser.add_argument('peername', help='4, 6, all - which peers do you want')
parser.add_argument('inet', help='4 or 6 - which peers do you want')
parser.add_argument('key', help='data')
args = parser.parse_args()

peer = {}

if args.inet == "4":
    pybird4 = PyBird(socket_file='/var/run/bird/bird.ctl')
    peer = pybird4.get_peer_status(args.peername)

if args.inet == "6" or args.inet == "all":
    pybird6 = PyBird(socket_file='/var/run/bird/bird6.ctl')
    peer = pybird6.get_peer_status(args.peername)

if 'state' in peer:
   print peer[args.key]
