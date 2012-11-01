#!/bin/sh

############################################################################
#
# This script is run at noon and 5pm each day by the Unix cron daemon to
# update the site during the day. It is a separate script because we want
# to drop results from earlier in the day before generating new ones.
#
# Author: Andrew Ferguson <adferguson@alumni.princeton.edu>
#
# Script written for election.princeton.edu run by Samuel S.-H. Wang under
# noncommercial-use-only license:
# You may use or modify this software, but only for noncommericial purposes.
# To seek a commercial-use license, contact sswang@princeton.edu
#
# Update History:
#      Sep 25, 2008 -- Use awk instead of cut to extract line count from wc
#
############################################################################

HISTORY=EV_estimate_history.csv

#SRC_PATH="/home/election"
SRC_PATH="/home/adf/pec/princeton-election"

cd $SRC_PATH/matlab/

# Delete today's estimate from the end of the history file, since it
# will be regenerated by the nightly script

num_lines=`wc $HISTORY | awk '{ print $1; }'`
num_lines=`expr $num_lines - 1`
head -$num_lines $HISTORY > $HISTORY.new
mv -f $HISTORY.new $HISTORY

cd $SRC_PATH/bin/
./nightly.sh
