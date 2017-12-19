#!/bin/bash -e

aws lambda create-function \
--function-name redis_benchmark \
--region us-west-2 \
--zip-file fileb://deploy.zip \
--role arn:aws:iam::562930434285:role/lambda-vpc-execution-role \
--handler redis_benchmark.lambda_handler \
--runtime python2.7 \
--timeout 30 \
--vpc-config SubnetIds=subnet-b182b0ea,SecurityGroupIds=sg-755b0508 
