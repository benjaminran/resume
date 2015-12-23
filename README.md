# resume
Dynamic resume publishing system


# Overview
This project contains the source files for my resumes and some associated utilities, like fully automated publishing and dynamic value insertion.


# Usage
The resume build and publishing process is controlled by make.

### Examples
_Generate a pdf from resume.tex into output/resume.pdf:_
```
$ make
```

_Upload resume.pdf to remote web server and shorten link with bitly:_
```
$ make publish
```

_Specify the objective to be included:_
```
$ make objective="Foo bar baz"
```

_Specify that an optional section should or shouldn't be included in the resume output:_
```
$ make vcs_included=false
```

_Save resume.pdf in the local archive:_
```
$ make archive
```

### Defaults
- "Education", "Professional Experience", "Private Projects", "Skills", "Languages", "Build Systems", "VCS", and "Interests" sections are included by default. "Objective" is left out unless specified.


# Dynamic Value Insertion
The Makefile uses the `sub` target to generate _output/gen/resume.tex_, which contains dynamically inserted values. This is done by running _util/tex-sub.py_ a Python script that replaces pragmas like `%%@sub{FOO}%%` from the source latex with their corresponding dynamic values. For example, all occurrences of `%%@sub{GIT_COORDINATES}%%` are replaced by the abbreviated SHA-1 hash of the latest git commit (as returned by _util/git-coordinates.sh_). This is used to generate a link to the latest possible version of the source that was used to generate any particular pdf. `%%@sub{LAST_UPDATED}%%` is replaced with the date on which the pdf was generated.


# Publishing
The first step of the publishing process is to upload _resume.pdf_ to a public directory on my webserver. The pdf name is mangled with the date and a number (e.g. _resume-12.17.2015-1.pdf_) to keep filenames distinct. 

Next, the _latest_ symlilnk in the web server directory is updated to point to the new file. 

Finally, the Bitly REST API is used to shorten the url. Previously this was then used by a Python script (_util/deploy.py_) that automates the browser with Selenium to update my LinkedIn profile with the new link. While _deploy.py_ is no longer used, the link shortening has been kept because it may be useful for later developments.


# Archive
The archive is a local backup of pdfs that have been generated. They are organized by the date they were generated, then are saved with the date as well as a user-inputted tag (short reminder of the resume content or purpose) in the filename.
