# resume
My resume

# Overview
This project contains the source files for my resumes. This is used as a submodule in my personal website.

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
