# resume
My resume

# Overview
This project contains the source files for my resumes and some associated utilities. This is used as a submodule in my personal website.

# Usage
The resume build process is controlled by `bin/build`. Content from _cv.xml_ is injected into different Jinja templates (_templates/resume.*.jinja_) and the results written/compiled into _output_.

# What You'll Need
- Python3 with:
  - Jinja2
  - Pypandoc
- The Adobe Garamond Pro font
- A latex distribution with luatex

### Examples
Generate a pdf and md from _content/cv.xml_ and _templates/resume.{tex|md}.jinja_ into _output/_:
```
$ bin/build
```

See [benjaminran.com/resume](http://benjaminran.com/resume).
