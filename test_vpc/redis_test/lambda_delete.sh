#!/bin/bash -e

aws lambda delete-function \
--function-name redis_test \
--region us-west-2 \

