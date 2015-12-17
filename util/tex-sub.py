#!/Users/benjaminran/Documents/resume/venv/bin/python

"""
A python script that dynamically generates some latex source based on xml content then inserts additional values into the latex source where indicated by %%@sub{TAG}%% pragmas
"""
from optparse import OptionParser
from bs4 import BeautifulSoup
import subprocess
import datetime
import os
import sys
import re


""" Return the substitution string for a given term """
def substring(term):
    return "%%@sub{"+term+"}%%"

""" Return the formatted date """
def formatdate():
    return datetime.date.today().strftime("%m/%d/%Y")

""" Return the current git coordinates """
def getgitcoordinates():
    return subprocess.Popen(["util/git-coordinates.sh", ""], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode("utf-8").strip()


""" Main Routine """
# Parse command line input
usage = "tex-sub.py [options] cv.xml inputfile.tex outputfile.tex"
parser = OptionParser(usage=usage)
parser.add_option("-o", "--objective", dest="objective", help="Include objective obj in resume", metavar="obj")
parser.add_option("-b", "--buildsystems", dest="buildsystemsincluded", help="Include the build systems section")
parser.add_option("-v", "--vcs", dest="vcsincluded", help="Include the version control systems section")
(options, args) = parser.parse_args()
if(len(args)!=3):
    parser.print_help()
    sys.exit()

#with open(args[0], 'r') as cvfile:
#    xml=cvfile.read()
    
    
# Do substitutions
with open(args[1], 'r') as file:
    tex=file.read()
    # Objective
    tex =re.sub(substring("OBJECTIVE_INCLUDED"), "true" if options.objective is not "" else "false", tex)
    tex = re.sub(substring("OBJECTIVE"), options.objective, tex)
    # Build Systems
    tex = re.sub(substring("BUILD_SYSTEMS_INCLUDED"), options.buildsystemsincluded, tex)
    # VCS
    tex = re.sub(substring("VCS_INCLUDED"), options.vcsincluded, tex)
    # Last Updated
    tex = re.sub(substring("LAST_UPDATED"), formatdate(), tex)
    # Git Coordinates
    tex = re.sub(substring("GIT_COORDINATES"), getgitcoordinates(), tex)
    # Check for unmatched pragmas
    unmatched = re.findall(substring(".*"), tex)
    if(len(unmatched)>0): sys.stderr.write("Unmatched pragmas found: "+str(unmatched)+"\n")

# Output results
with open(args[2], 'w') as outfile:
    outfile.write(tex)
