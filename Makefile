### Output directories and pdf output file
OUTPUT = output
PDF = ${OUTPUT}/resume.pdf
ARCHIVE = archive

### Deploy target directory
EC2_USER = ubuntu
EC2_IP = 52.35.114.95
EC2_WEB_ROOT = /home/ubuntu/public_html
EC2_WEB_PATH = resume
EC2_FULL_PATH = ${EC2_WEB_ROOT}/${EC2_WEB_PATH}
EC2_SSH_URL = ${EC2_USER}@${EC2_IP}

### Conditional Inclusion
objective?=
build_systems_included?=false
vcs_included?=false

### Temporary and other files
FILENAME_TMP = resume-filename.tmp
URL_TMP = bitly-url.tmp

### Write resume to pdf
open : ${PDF}
	open -g ${PDF}

${PDF} : clean resume.tex cv.xml cv.py sub
	cp cv.xml cv.py ${OUTPUT}
	lualatex -shell-escape --output-directory=${OUTPUT} ${OUTPUT}/resume.tex
	pythontex ${OUTPUT}/resume
	lualatex -shell-escape --output-directory=${OUTPUT} ${OUTPUT}/resume.tex

sub : resume.tex ${OUTPUT}
	util/tex-sub.py --objective="${objective}" --buildsystems=${build_systems_included} --vcs=${vcs_included} cv.xml resume.tex ${OUTPUT}/resume.tex

${OUTPUT} :
	mkdir -p ${OUTPUT}

clean :
	rm -r ${OUTPUT}

commit :
	git add --all
	git commit
	git push origin master

### Upload pdf to public server and shorten url
publish : ${PDF}
	util/get-next-url.sh ${EC2_SSH_URL} ${EC2_FULL_PATH} >${FILENAME_TMP}
	util/upload.sh ${PDF} ${EC2_SSH_URL} ${EC2_FULL_PATH} `cat ${FILENAME_TMP}`
	@printf "Deployed resume as %s\n" `cat ${FILENAME_TMP}`
	curl -G https://api-ssl.bitly.com/v3/shorten --data-urlencode access_token@util/bitly-oauth --data-urlencode format=txt --data-urlencode longUrl=http://${EC2_IP}/${EC2_WEB_PATH}/`cat ${FILENAME_TMP}` >${URL_TMP}
	@printf "Shortened url to %s\n" `cat ${URL_TMP}`
#	util/deploy.py `cat ${URL_TMP}`
	rm ${FILENAME_TMP} ${URL_TMP}

### Copy pdf to archive
archive : ${PDF}
	echo "Enter tag (to be appended to filename):"; \
	read tag; \
	archfile=`util/get-archive-path.sh ${PDF} ${ARCHIVE} $${tag}`; \
	mkdir -p `dirname $${archfile}`; \
	cp ${PDF} $${archfile}; \
	echo Wrote $${archfile}
