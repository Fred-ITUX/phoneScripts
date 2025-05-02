#!/bin/bash

#### Phone scripts for iSH
#### git clone https://github.com/Fred-ITUX/phoneScripts.git

#scriptsPath="~/phoneScripts/Scripts/"
utilitiesPath="~/phoneScripts/Utilities/"


echo -e "\n\n Discarding local changes"
git reset --hard HEAD

echo -e "Pulling from origin\n"


# git pull origin master
git pull origin

echo -e "\n Updating profile"


cp ~/phoneScripts/Utilities/profile.sh     ~/.profile

source ~/.profile

find ~/ -type f -name "*.sh" -exec chmod +x {} +
