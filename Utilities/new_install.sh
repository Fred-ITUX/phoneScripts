#!/bin/bash

#### Phone scripts (iSH)

apkAppPackages=(
    jq
)



printf '%s\n\n' "${apkAppPackages[@]}" \
  | xargs -I{} bash -c 'echo -e "\n\n\n\t• Installing {}..." && apk add -y "{}"' \
>> log_install.txt 2>&1