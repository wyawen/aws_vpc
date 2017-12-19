#!/bin/bash -e

zip -r deploy.zip redis_test.py ../rediscluster ../redis_py_cluster-1.3.4.dist-info ../redis ../redis-2.10.6.dist-info
sh lambda_create.sh
