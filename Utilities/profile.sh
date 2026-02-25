#!/bin/bash


#### Path
# HOME="~"
scriptsPath="~/phoneScripts/Scripts"
utilitiesPath="~/phoneScripts/Utilities"



#### Quality of life
alias addx='chmod +x'
alias profile='nano ~/.profile'
alias welcome='nano /etc/motd'
alias c='clear'
alias e='exit'


#### Github repo update
alias repoUPD="cd $utilitiesPath/ && $utilitiesPath/repo_update.sh"
alias setup="$utilitiesPath/setup.sh"


#### Python scripts
alias convMetric="python3 $scriptsPath/measure_unit_converter.py"
alias pswd="python3 $scriptsPath/passwd_gen.py"
alias percentage="python3 $scriptsPath/perc_calc.py"
alias random="python3 $scriptsPath/randomChoose.py"
alias tableStyle="python3 $scriptsPath/tableStyle.py"
alias math="python3 $scriptsPath/Games/math_calc.py"


#### Linux scripts
alias loop="$utilitiesPath/loop.sh &"
alias weather="$scriptsPath/weather.sh"