#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
from obspy import UTCDateTime
from obspy.clients.fdsn.mass_downloader import RectangularDomain, \
    Restrictions, MassDownloader

network = "ZV"
starttime=UTCDateTime(2008, 1, 1)
endtime=UTCDateTime(2011, 1, 1)
ROOTDIR = "/run/media/seisman/Seagate Expansion Drive/DOWNLOADING/"
DATADIR = ROOTDIR + network

domain = RectangularDomain(minlatitude=18, maxlatitude=54,
                           minlongitude=65, maxlongitude=135)

restrictions = Restrictions(
        starttime=starttime,
        endtime=endtime,
        network=network,
        channel="BH?,SH?,LH?",
        chunklength_in_sec=86400,
        reject_channels_with_gaps=False,
        minimum_length=0.0,
        minimum_interstation_distance_in_m=50.0,
        location_priorities=['', '00', '10', '01', '*'],
        )

def mseed_storage(network, station, location, channel, starttime, endtime):

    path = os.path.join(DATADIR, starttime.strftime("%Y%m%d"),
            "{}.{}.{}.{}.mseed".format(network, station, location, channel))

    if os.path.exists(path):
        return True
    else:
        return path

mdl = MassDownloader(providers=["IRIS"])
mdl.download(domain, restrictions, mseed_storage=mseed_storage,
             stationxml_storage="stations", threads_per_client=15)
