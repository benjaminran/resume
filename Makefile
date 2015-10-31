### Output directory and pdf output file
OUTPUT = output
PDF = ${OUTPUT}/resume.pdf

### Deploy target directory
EC2_USER = ubuntu
EC2_IP = 52.11.81.109
EC2_WEB_ROOT = /home/ubuntu/public_html
EC2_WEB_PATH = resume
EC2_FULL_PATH = ${EC2_WEB_ROOT}/${EC2_WEB_PATH}
EC2_SSH_URL = ${EC2_USER}@${EC2_IP}

### Temporary files
FILENAME_TMP = resume-filename.tmp
URL_TMP = bitly-url.tmp

### Write resume to pdf
all : ${PDF}

${PDF} : resume.tex ${OUTPUT}
	lualatex --output-directory=${OUTPUT} resume.tex
	open -g ${PDF}

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
	scp ${PDF} ${EC2_SSH_URL}:${EC2_WEB_ROOT}/${EC2_WEB_PATH}/`cat ${FILENAME_TMP}`;
	@printf "Deploying resume as %s\n" `cat ${FILENAME_TMP}`
	curl -G https://api-ssl.bitly.com/v3/shorten --data-urlencode access_token@util/bitly-oauth --data-urlencode format=txt --data-urlencode longUrl=http://${EC2_IP}/${EC2_WEB_PATH}/`cat ${FILENAME_TMP}` >${URL_TMP}
	@printf "Shortened url to %s\n" `cat ${URL_TMP}`
	util/deploy.py `cat ${URL_TMP}`
	rm ${FILENAME_TMP} ${URL_TMP}
