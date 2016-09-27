### Output directories and pdf output file
OUTPUT = output
PDF = ${OUTPUT}/resume.pdf
ARCHIVE = archive

### Deploy target directory
EC2_USER = ubuntu
EC2_IP = benjaminran.com
EC2_WEB_ROOT = /home/ubuntu/public_html
EC2_WEB_PATH = resume
EC2_FULL_PATH = ${EC2_WEB_ROOT}/${EC2_WEB_PATH}
EC2_SSH_URL = ${EC2_USER}@${EC2_IP}

### Temporary and other files
FILENAME_TMP = resume-filename.tmp
URL_TMP = bitly-url.tmp

### Write resume to pdf
open : resume
	open -g ${PDF}

resume : clean output templates/resume.tex.jinja cv.xml cv.py build.py
	cp cv.xml cv.py ${OUTPUT}
	python build.py resume > ${OUTPUT}/resume.tex
	lualatex -shell-escape --output-directory=${OUTPUT} ${OUTPUT}/resume.tex

${OUTPUT} :
	- mkdir -p ${OUTPUT}

clean :
	- rm -r ${OUTPUT}

commit :
	git add --all
	git commit
	git push origin master

### Upload pdf to public server and shorten url
publish : resume
	util/get-next-url.sh ${EC2_SSH_URL} ${EC2_FULL_PATH} >${FILENAME_TMP}
	util/upload.sh ${PDF} ${EC2_SSH_URL} ${EC2_FULL_PATH} `cat ${FILENAME_TMP}`
	@printf "Deployed resume as %s\n" `cat ${FILENAME_TMP}`
	curl -G https://api-ssl.bitly.com/v3/shorten --data-urlencode access_token@util/bitly-oauth --data-urlencode format=txt --data-urlencode longUrl=http://${EC2_IP}/${EC2_WEB_PATH}/`cat ${FILENAME_TMP}` >${URL_TMP}
	@printf "Shortened url to %s\n" `cat ${URL_TMP}`
	rm ${FILENAME_TMP} ${URL_TMP}

### Copy pdf to archive
archive : ${PDF}
	echo "Enter tag (to be appended to filename):"; \
	read tag; \
	archfile=`util/get-archive-path.sh ${PDF} ${ARCHIVE} $${tag}`; \
	mkdir -p `dirname $${archfile}`; \
	cp ${PDF} $${archfile}; \
	echo Wrote $${archfile}
