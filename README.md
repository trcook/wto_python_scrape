wto_python_scrape
=================

A basic python scraper that will be aimed at WTO disputes, but is intended to be general enough for use as a template for other, similar scraping projects.

Requirements:
=============
python =>2.6
(stock installation of OSX will satisfy this requirement)

Installation
============

1. clone repo with the following command in a shell (i.e. from the terminal):  `git clone https://github.com/trcook/wto_python_scrape.git`. By default this will create a directory called `./wto_python_scrape`

2. run local environment installer by executing `./bootstrap.sh` from the root of the cloned repository (i.e. `cd wto_python_scrape` first). 
  - This will install localized python environment and required dependencies. If you want to install these globally, just run `pip install -r requirements.txt` from the repository root. This may or may not work correctly, I haven't tested it and it will depend on your system setup. 
  - The reason we are using a localized environment is that it ensures some freedom from dependency problems. The localized python environment (i.e. a virtual environment) will create a directory called `venv` in the repo directory (i.e. `wto_python_scrape/venv`), into which a local version of `python 2.7.6` will be installed, with dependency versions installed as specified in `requirements.txt` The total install footprint is, at the moment, only about 10 megabytes or so. 

3. activate environment -- from shell (at root of the git repo), type: `source ./venv/bin/activate`. This step will need to be done every time we run the scrpits provided in this repo. The first two steps only need to occur on the initial install.

  - note that at this point your shell prompt will probably change and you will be running out python from a different path than normal (i.e. your session will point your shell's search path to the `venv` directory). This change is temporary and limited to the current shell session. Further, if you want to completely remove the version of python that we just installed, you can just delete the venv directory and it will be gone. 
  - Everything is, essentially, sandboxed in the repo, so you can make like this project was never on your system by removing the repo folder. 


NOTES: 
======
This is going to be a pain through scrapy, but that's ok. 
It turns out we need to have a library installed called libffi. This is easily done through homebrew, but this breaks plans on portability since it means that every system that runs this will need to already have this library installed. THe following steps get us a working install:  (these run after the venv is setup and activated)

1. `brew install pkg-config libffi`
	- You may alraedy have this installed and Brew will tell you as much
2. `export PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.0.13/lib/pkgconfig/`
3. `pip install cryptography`
	- this is a library that we need to use secure socket layer comms with websites. It's basically like openssl
4. we need to install libxml -- which is used for reading xml and parsing. to do this we run `STATIC_DEPS=true pip install lxml`
4. `pip install scrapy`
	- It's possible that we need to to `easy_install scrapy` instead. 

TODO 11/24/2014 03:43:02 PICKUPHERE revise .wto_bootstrap_script_maker to either incorporate the above steps, or so that the bootstrapper doesn't launch pip right away. Instead, put bootstrap.sh to activate in venv and then run the steps above. Option 2 may be the more appealing as it exposes necessary machinery that may need tinkering with on a case-by-case basis. 

Usage
=====
I'll fill this in when we actually have some scripts to run.


