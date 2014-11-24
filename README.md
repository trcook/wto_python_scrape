wto_python_scrape
=================

A basic python scraper that will be aimed at WTO disputes, but is intended to be general enough for use as a template for other, similar scraping projects.

Requirements:
=============
python =>2.6
(stock installation of OSX will satisfy this requirement)

Installation
============

1. clone repo using:  `git clone https://github.com/trcook/wto_python_scrape.git`. By default this will create a directory called `./wto_python_scrape`

2. run local environment installer by executing `./bootstrap.sh` from the root of the cloned repository. 
  - This will install localized python environment and required dependencies. If you want to install these globally, just run `pip install -r requirements.txt` from the repository root. This may or may not work correctly, I haven't tested it and it will depend on your system setup. 
  - The reason we are using a localized environment is that it ensures some freedom from dependency problems. The localized python environment (i.e. a virtual environment) will create a directory called `venv`, into which a local version of `python 2.7.6` will be installed, with dependency versions installed as specified in `requirements.txt` The total install footprint is, at the moment, only about 10 megabytes or so. 

3. activate environment -- from shell (at root of the git repo), type: `source ./venv/bin/activate`. This step will need to be done every time we run the scrpits provided in this repo. The first two steps only need to occur on the initial install.

  - note that at this point your shell prompt will probably change and you will be running out python from a different path than normal (i.e. your session will point your shell's search path to the `venv` directory). This change is temporary and limited to the current shell session. Further, if you want to completely remove the version of python that we just installed, you can just delete the venv directory and it will be gone. 
  - Everything is, essentially, sandboxed in the repo, so you can make like this project was never on your system by removing the repo folder. 

Usage
=====
I'll fill this in when we actually have some scripts to run.


