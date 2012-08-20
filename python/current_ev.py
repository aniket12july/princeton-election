#!/usr/bin/env python

############################################################################
#
# This script produces the display at the top of the blog of the current
# median electoral votes for each candidate. It also generates the text for
# an email message which the cron daemon sends out.
#
# Author: Andrew Ferguson <adferguson@alumni.princeton.edu>
#
# Script written for election.princeton.edu run by Samuel S.-H. Wang under
# noncommercial-use-only license:
# You may use or modify this software, but only for noncommericial purposes.
# To seek a commercial-use license, contact sswang@princeton.edu
#
# Update History:
#    Jul 7, 2012 -- Initial port from 2008 version
#
############################################################################

import time

efile = open("../matlab/EV_estimates.csv")
values = efile.read()[:-1].split(",")
efile.close()

time_str = "%s %s, %s:%s" % (time.strftime("%B"), int(time.localtime()[2]),
		int(time.strftime("%I")), time.strftime("%M%p %Z"))

dem_ev = values[0]
gop_ev = values[1]
metamargin = float(values[12])

evdisplay = open("current_ev.html", "w")

evdisplay.write('\t<li>As of %s:</li>\n' % time_str)
evdisplay.write('\t<li style="color: blue">Obama: %s</li>\n' % dem_ev)
evdisplay.write('\t<li style="color: red">Romney: %s</li>\n' % gop_ev)

evdisplay.write('\t<li><a href="/faq/#metamargin">Meta-margin</a>: ')

if metamargin > 0:
	evdisplay.write('Obama +%s%%</li>\n' % metamargin)
elif metamargin < 0:
	evdisplay.write('Romney +%s%%</li>\n' % -metamargin)
else:
	evdisplay.write('Tied</li>\n')

evdisplay.close()

############################################################################

email_update = \
"""Today's update of the Meta-Analysis of State Polls at Princeton University
gives a median EV expectation of

Obama %s, Romney %s.

This update is effective as of %s.

From
The Princeton Election Consortium
"""

email = open("email_update.txt", "w")
email.write(email_update % (dem_ev, gop_ev, time_str))
email.close()
