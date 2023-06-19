#!/bin/bash

quiet=false

while getopts q flag
do
    case "${flag}" in
        q) quiet=true;;
    esac
done

export LD_LIBRARY_PATH="/opt/amazon/efa/lib:/opt/amazon/openmpi/lib:/usr/local/cuda/efa/lib:/usr/local/cuda/lib:/usr/local/cuda/lib64:/usr/local/cuda:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda/targets/x86_64-linux/lib:/usr/local/lib:/usr/lib"

source venv/bin/activate

ISO_DATE=$(date -Iseconds -u)

if [[ $quiet = true ]]
then
    python3 ./falcon_peft.py  -save_steps 500 </dev/null >"$ISO_DATE.log" 2>"$ISO_DATE.err"
else
    python3 ./falcon_peft.py  </dev/null
fi
