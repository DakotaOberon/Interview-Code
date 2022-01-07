#!/bin/bash

# Report occurances of a status code at a specific time by ip

# Grab contents on log file
content=$(<log_file)

# Create an empty array
declare -A report

# Grab aguments from command
date_search=$1
hour_search=$2
code_search=$3

# Separate content by newline and loop
IFS=$'\n'
for line in $content;
do
    # Set seperator to spaces
    IFS=' '

    # Create an associative array for items in line
    read -r -a items <<< $line

    # Set values to readable variables
    date=${items[0]}
    ip=${items[1]}
    code=${items[2]}

    # Check if timestamp and code match
    if [[ $date =~ $date_searchT$hour_search ]] && [[ $code =~ $code_search ]]
    then
        # Check if ip has an entry in report array
        if [[ ${report[$ip]} ]]
        then
            # Increment value of ip in report by 1
            ((report[$ip]++))
        else
            # Create entry for ip in report array and set it to 1
            report[$ip]=1
        fi
    fi
done

# Loop over each key in array
for i in "${!report[@]}"
do
    # echo data
    echo "$i : ${report[$i]}"
done
