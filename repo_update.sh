#!/bin/bash

#### Phone scripts for iSH
#### git clone https://github.com/Fred-ITUX/phoneScripts.git

#scriptsPath="$HOME/phoneScripts"


echo -e "Pulling from origin\n"

cd "$scriptsPath"

# git pull origin master
git pull origin

echo -e "\n Updating profile"

cp profile.sh ~/.profile.sh
