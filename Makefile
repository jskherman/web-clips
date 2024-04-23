setup:
	echo "@@@@@@ Setting up environment... @@@@@@"
	bun install
	bun build-css
	bundle install
html:
	echo "@@@@@ Downloading HTML files... @@@@@"
build:
	make setup
	make html
	echo "@@@@@ Building site... @@@@@"
	bundle exec jekyll build
