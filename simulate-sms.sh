#!/bin/bash

if [ -z "$1" ]; then
    MESSAGE="Should I eat Bob's cookie?"
else
    MESSAGE=$1
fi

if [ -z "$2" ]; then
    URL='http://54.248.235.127:8000/sms.php'
else
    URL=$2
fi 

curl                                                                           \
-d AccountSid=AC00000000000000000000000000000000                               \
-d ApiVersion=2010-04-01                                                       \
-d Body="$MESSAGE"                                                             \
-d From=14155551212                                                            \
-d FromCity='SAN FRANCISCO'                                                    \
-d FromCountry=US                                                              \
-d FromState=CA                                                                \
-d FromZip=94114                                                               \
-d SmsMessageSid=SM00000000000000000000000000000000                            \
-d SmsSid=SM00000000000000000000000000000000                                   \
-d SmsStatus=received                                                          \
-d To=14156973339                                                              \
-d ToCity=''                                                                   \
-d ToCountry=US                                                                \
-d ToState=CA                                                                  \
-d ToZip=''                                                                    \
$URL