# resume
Dynamic resume publishing system

# Overview
This project contains the source files for my resumes and some associated utilities, like fully automated publishing and dynamic value insertion. 

# Usage
The resume build and publishing process is controlled by make. Content from _cv.xml_ is made available to a Jinja template (_templates/resume.tex.jinja_) via _cv.py_ and the result, _output/resume.tex_ is compiled into a pdf which can then be automatically published.

# What You'll Need
- Python3 with:
  - Jinja2
  - Pypandoc
- The Adobe Garamond Pro font
- A latex distribution with luatex

### Examples
Generate a pdf from _content/cv.xml_ and _templates/resume.tex.jinja_ into _output/resume.pdf_:
```
$ bin/build
```

Upload _output/resume.pdf_ to remote web server:
```
$ bin/publish
```

# Publishing
The publishing process uploads _output/resume.pdf_ to a public directory on my webserver. The pdf name is mangled with the date and a number (e.g. _resume-12.17.2015-1.pdf_) to keep filenames distinct. 

Next, the _benjaminran-latest.pdf_ symlink in the web server directory is updated to point to the new file.

See [http://benjaminran.com/resume/benjaminran-latest.pdf](http://benjaminran.com/resume/benjaminran-latest.pdf).
