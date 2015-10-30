OUTPUT = output

all : resume.tex
	mkdir -p ${OUTPUT}
	lualatex --output-directory=${OUTPUT} resume.tex
	open -g ${OUTPUT}/resume.pdf

clean :
	rm -r ${OUTPUT}

commit :
	git add --all
	git commit
	git push origin master
