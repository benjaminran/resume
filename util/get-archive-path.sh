#!/bin/bash

#
# Usage: get-archive-path.sh resume.pdf archive [tag]
#

RESUME=${1}
ARCHIVE=${2}
TAG=${3}

if [ ${#TAG} -ne 0 ]; then TAG="-${TAG}"; fi
date=`date +%m.%d.%Y`
name="`basename -s .pdf ${RESUME}`-${date}${TAG}"
suffix=1

while true; do
    if stat ${ARCHIVE}/${date}/${name}-${suffix}.pdf >/dev/null 2>&1
    then
        let suffix++
    else
        break
    fi
done
echo ${ARCHIVE}/${date}/${name}-${suffix}.pdf
