#!/bin/bash -eu

spawn-fcgi -u nginx -g nginx -s /var/run/fcgiwrap.socket -M 766 -- /usr/sbin/fcgiwrap -f
nginx -g 'daemon off;'
