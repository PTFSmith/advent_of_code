#/bin/bash

url="${1}"
dir=$(pwd)

if [[ ! -f "${dir}/input_file" ]]; then
  echo "INFO: Getting input file"
  curl  -s -H "Cookie: $AOC" ${url}  > $dir/input_file
fi
