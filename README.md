# resume
My resume (deprecated)

# Overview

This project contained the source files for my resumes. Its outputs were referenced in my personal website.

I no longer use this project; the primary latex format hasn't proved worth the effort to maintain considering I don't regularly use latex for anything else and am not using any distinguishing latex features in my resume. And the markdown/plaintext views have also not provided enough value to justify keeping around. Maybe some day I'll revive it when I need multiple views of the same or overlapping resume content.

# Usage

Install the following fonts:
- https://fontsgeek.com/fonts/Adobe-Garamond-Pro-Regular 
- https://fontsgeek.com/fonts/Adobe-Garamond-Pro-Semibold

Then, assuming macos:
```
brew install pandoc
python3 -m venv venv
source venv/bin/activate
pip install Jinja2
pip install -e .
resume --help
```

The resume build process is controlled by `bin/build`. Content from _cv.xml_ is injected into different Jinja templates (_templates/resume.*.jinja_) and the results written/compiled into _output_.

# Dependencies
- Python3 with:
  - Jinja2
  - Pypandoc
- The Adobe Garamond Pro font
- A latex distribution with luatex

## Outputs
- [output/resume.md](output/resume.md)
- [output/resume.pdf](output/resume.pdf)
- [output/resume.txt](output/resume.txt)

See [benjaminran.com/resume](http://benjaminran.com/resume).
