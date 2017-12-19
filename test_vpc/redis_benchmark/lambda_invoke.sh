#!/bin/bash -e

aws lambda invoke \
--invocation-type RequestResponse \
--function-name hello \
--region us-west-2 \
--log-type Tail \
--payload '{"ip":"54.153.96.14"}' \
outputfile.txt &> logs.txt 



