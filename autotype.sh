#!/usr/bin/env bash
python3 autotype $1 $2

FILE=${1?Error: no file given}
SPEED=${2:-'--0.04'}
