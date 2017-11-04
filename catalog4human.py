#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Convert catalog of different formats to human-friendly format
#
# Author: Dongdong Tian @ USTC
# Date: 2017-07-15
# Revisions:
#   2017-11-04  Dongdong Tian  Initial coding.
#

import sys


class Event(object):
    """Class for Event."""
    def __init__(self, origin, latitude, longitude, depth, magnitude):
        self.origin = origin
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.depth = float(depth)
        self.magnitude = float(magnitude)

    def __str__(self):
        """
        Human-friendly format: origin latitude longitude depth magnitude
        """
        str = "{} {:8.4f} {:9.4f} {:>5} {}".format(self.origin,
                                                   self.latitude,
                                                   self.longitude,
                                                   self.depth,
                                                   self.magnitude)
        return str


def _read_iris(f):
    # IRIS Event web service in txt format
    # http://service.iris.edu/fdsnws/event/docs/1/builder/
    events = []
    for line in f:
        origin, evla, evlo, evdp = line.split('|')[1:5]
        mag = line.split('|')[10]
        events.append(Event(origin, evla, evlo, evdp, mag))
    return events


def _read_sod(f):
    # SOD generated csv format
    events = []
    for line in f:
        origin, evla, evlo, evdp, unit, mag = map(str.strip, line.split(',')[0:6])
        origin = origin[:-1]
        if unit.lower() == 'meter':
            evdp = float(evdp)/1000
        events.append(Event(origin, evla, evlo, evdp, mag))
    return events


def read_catalog(catalog):
    """ Read catalog in IRIS or SOD format. """
    with open(catalog, "r") as f:
        header = f.readline()
        if header.startswith('#EventID | Time | Latitude | Longitude | Depth/km'):
            catalog = _read_iris(f)
        elif header.startswith('time, latitude, longitude, depth, depthUnits, magnitude'):
            catalog = _read_sod(f)
        else:
            sys.exit("Unknown catalog format")
    return catalog


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s catalog.txt > newcatalog.txt" % sys.argv[0])
        sys.exit()

    for event in read_catalog(sys.argv[1]):
        print(event)
