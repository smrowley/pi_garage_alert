#!/bin/bash
if [[ $# -eq 0 ]] ; then
    echo 'please pass your username'
    exit 0
fi

cp bin/pi_garage_alert.py /usr/local/sbin/
cp etc/pi_garage_alert_config.py /usr/local/etc/
cp init.d/pi_garage_alert /etc/init.d/
chown $1 /usr/local/etc/pi_garage_alert_config.py:q
