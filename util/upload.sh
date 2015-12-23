#!/bin/bash

#
# Usage: upload.sh resume.pdf host /remote/dir newresume.pdf
#
# Uploads pdf to web server and updates 'latest' symlink
#

local=$1
host=$2
remote_dir=$3
remote=$4

scp ${local} ${host}:${remote_dir}/${remote}
ssh ${host} ln -f -s ${remote_dir}/${remote} ${remote_dir}/latest
