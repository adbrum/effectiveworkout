#!/usr/bin/env bash
# Usage: source setup.sh

# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}>>> Cloning repo...${reset}"
git clone https://github.com/adbrum/effectiveworkout.git effectiveworkout

echo "${green}>>> Enter in effectiveworkout directory.${reset}"
cd effectiveworkout

echo "${green}>>> Creating virtualenv...${reset}"
python -m venv .workout
echo "${green}>>> venv is created.${reset}"

sleep 2
echo "${green}>>> activate the venv.${reset}"
source .workout/bin/activate

echo "${green}>>> Short the prompt path.${reset}"
PS1="(`basename \"$VIRTUAL_ENV\"`)\e[1;34m:/\W\e[00m$ "
sleep 2

echo "${green}>>> Installing dependencies...${reset}"
pip install -r requirements-dev.txt

echo "${green}>>> Creating .env${reset}"
cp contrib/env-sample .env

echo "${green}>>> Running migration database...${reset}"
python manage.py migrate

echo "${green}>>> Running loaddata...${reset}"
python manage.py loaddata */config/fixtures/*.json

echo "${green}>>> Create superuser...${reset}"
python manage.py createsuperuser --email=''

echo "${green}>>> Running tests...${reset}"
python manage.py test

echo "${green}>>> Running loaddata...${reset}"
python manage.py runserver

echo "${green}>>> Done.${reset}"