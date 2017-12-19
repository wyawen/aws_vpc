#!/bin/bash -e

zip -r deploy.zip redis_benchmark.py redis redis-2.10.6.dist-info
sh lambda_create.sh
