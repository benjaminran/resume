### Output directory and pdf output file
OUTPUT = output
PDF = ${OUTPUT}/resume.pdf

### Deploy target directory
EC2_USER = ubuntu
EC2_HOST = 52.11.81.109
EC2_WEB_ROOT = /home/ubuntu/public_html
EC2_WEB_PATH = resume


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
deploy : ${PDF}
	@read -p "Enter resume name: " resumename; \
	scp ${PDF} ${EC2_USER}@${EC2_HOST}:${EC2_WEB_ROOT}/${EC2_WEB_PATH}/$${resumename}.pdf; \
	curl -G https://api-ssl.bitly.com/v3/shorten --data-urlencode access_token@util/bitly-oauth --data-urlencode format=txt --data-urlencode longUrl=http://${EC2_HOST}/${EC2_WEB_PATH}/$${resumename}.pdf
