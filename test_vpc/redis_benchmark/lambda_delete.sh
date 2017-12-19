#!/bin/bash -e

aws lambda delete-function \
--function-name hello \
--region us-west-2 \

