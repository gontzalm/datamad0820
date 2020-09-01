#!/bin/bash

name="Gontzal"
echo $name
mkdir $name
rm -r $name
for i in $(ls lorem); do
    echo $i
    echo $(echo -n "$i" | wc -m)
    echo "$i has $(echo -n "$i" | wc -m) characters long"
done
cat /proc/cpu.info

# CREATE PERMANENT ALIASES
nano ~/.bashrc
#add: alias myalias="command"
source ~/.bashrc

tar -czvf lorem-compressed.tar.gz lorem lorem-copy
tar -xzvf lorem-compressed.tar.gz -C lorem-uncompressed