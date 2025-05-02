#!/bin/bash


git config --global user.email "thealldedfred@gmail.com"                                      
git config --global user.name "Fred-ITUX"


find ~/phoneScripts -type f -name "*.sh" -exec chmod +x {} +


cp ~/phoneScripts/Utilities/profile.sh     ~/.profile

