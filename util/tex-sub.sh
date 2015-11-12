#!/bin/bash

#
#   A substitution utility used to replace pragmas in a tex file with dynamically determined values
#
#   Usage: tex-sub.sh inputfile.tex outputfile.tex tag newtext
#   All occurences of the pragma "%%@sub{tag}" in the input tex source will be replaced.
#

sed "s|%%@sub{${3}}|${4}|" ${1} >${2}
