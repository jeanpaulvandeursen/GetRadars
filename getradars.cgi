#!/bin/bash
DATA=`curl https://api.anwb.nl/v2/incidents/desktop-light\?apikey\=QYUEE3fEcFD7SGMJ6E7QBCMzdQGqRkAi | jq -r '.roads[].segments[].radars[]? | .road,.HM'  | awk '{printf $1 "\t\t\t\t\t\t\t"} NR%2==0 {print ""}'`
echo "content-type: text/plain"
echo
echo  "$DATA"
