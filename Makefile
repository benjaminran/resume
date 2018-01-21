FILES := content/cv.xml templates/resume.md.jinja templates/resume.tex.jinja templates/resume.txt.jinja

develop:
	fswatch $(FILES) | while read l; do echo ">>> $$l" && resume build; done
