#!/bin/bash

#
# Usage: get-next-url.sh <ssh url> <remote directory to search>
#

HOST=${1}
DIR=${2}

name=`date +resume-%m.%d.%Y`
suffix=1

while true; do
    if ssh $HOST stat ${DIR}/${name}-${suffix}.pdf \> /dev/null 2\>\&1
    then
        let suffix++
    else
        break
    fi
done
echo ${name}-${suffix}.pdf
