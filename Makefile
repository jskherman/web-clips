setup:
	echo "@@@@@@ Setting up environment... @@@@@@"
	pip install gdown
	bun install
	bun build-css
	bundle install
html:
	echo "@@@@@ Downloading HTML files... @@@@@"
	gdown --folder https://drive.google.com/drive/folders/1D9JkAuAwaZpYdZkAxrv2FPQxXQ90P8Zd
build:
	make setup
	make html
	echo "@@@@@ Building site... @@@@@"
	bundle exec jekyll build --trace
