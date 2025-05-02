#!/bin/bash

#### Phone scripts for iSH
#### git clone https://github.com/Fred-ITUX/phoneScripts.git

#scriptsPath="$HOME/phoneScripts"


echo -e "\n Discarding local changes"
git reset --hard HEAD


echo -e "Pulling from origin\n"

cd "$scriptsPath"

# git pull origin master
git pull origin

echo -e "\n Updating profile"

cp profile.sh ~/.profile.sh

find ~/ -type f -name "*.sh" -exec chmod +x {} +