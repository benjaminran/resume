OUTPUT = output # Output directory

all : resume.tex
	mkdir -p ${OUTPUT}
	lualatex --output-directory=${OUTPUT} resume.tex

clean :
	rm -r ${OUTPUT}

commit :
	git add --all
	git commit
	git push origin master
