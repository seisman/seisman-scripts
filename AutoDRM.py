#!/usr/bin/env python
#
# Reference:
# http://www.earthquakescanada.nrcan.gc.ca/stndon/autodrm/autodrm_guide-en.php
#
# email address to receive notification
email = "username@mail.ustc.edu.cn"
# unique user ID to avoid data naming conflicts
user_id = "TDD"
# data format: SEED|CSS|GSE2.0|IMS1.0|CA|INT
data_format = 'SEED'
# get email reply or not
notify = True
# title of replied emails
title = "DATA REQUEST via AutoDRM"
# station list
stations = ['YKB0', 'YKB1']
# channel list
channels = '*HZ'

starttime = "20120713080356"
duration = 120

print("BEGIN")
print("EMAIL {}".format(email))
print("TITLE {}".format(title))
print("OUT_FILE {}.{}.{}".format(user_id, starttime, data_format))
print("START_TIME {}".format(starttime))
if not notify:
    print("NONOTIFY")
print("DURATION {}".format(duration))
print("STA_LIST {}".format(','.join(stations)))
print("CHAN_LIST {}".format(channels))
print("FORMAT {}".format(data_format))
print("WAVEFORM")
print("STOP")
