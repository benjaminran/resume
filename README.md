#resume

# Overview
This project contains the source files for my resumes and some associated utilities, like fully automated publishing and dynamic value insertion.

# Make
The resume build and publishing process is controlled by make.

### Examples
`make` _generate a pdf from resume.tex into output/resume.pdf_
`make publish` _upload resume.pdf to remote web server, shorten link with bitly, then edit LinkedIn with new link_
`make objective="Obtain a position as an underwater basket weaver"` _specify the objective to be included_
`make vcs=false` _specify that an optional section should or shouldn't be included in the resume output_

### Defaults
- Sections "Education", "Professional Experience", "Private Projects", "Skills", "Languages", "Build Systems", "VCS", "Interests" are included by default. "Objective" is left out unless specified.
