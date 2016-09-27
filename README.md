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
Generate a pdf from _resume.tex_ into _output/resume.pdf_:
```
$ make resume
```

Upload _output/resume.pdf_ to remote web server and shorten link with bitly:
```
$ make publish
```

Specify the objective to be included:
```
$ make objective="Obtain a position as an underwater basketweaver"
```

Specify that an optional section should or shouldn't be included in the resume output:
```
$ make vcs_included=false
```

# Publishing
The publishing process uploads _output/resume.pdf_ to a public directory on my webserver. The pdf name is mangled with the date and a number (e.g. _resume-12.17.2015-1.pdf_) to keep filenames distinct. 

Next, the _latest.pdf_ symlink in the web server directory is updated to point to the new file.

See [benjaminran.com/resume/latest.pdf](http://benjaminran.com/resume/latest.pdf).
