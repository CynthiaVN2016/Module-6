#!/bin/sh

kill $(ps -u | grep omxplayer | awk '{print $2}')
