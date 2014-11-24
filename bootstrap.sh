#! /usr/bin/ENV bash


# produce the venv with access to system packages
python .wto_scraper_bootstrap.py . --system-site-packages -p python2.7

# activate venv
source ./venv/bin/activate

# install requirements via pip.
pip install -r requirements.txt