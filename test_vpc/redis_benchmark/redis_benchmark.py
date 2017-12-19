import os
import time
import boto3
import redis

def read_throughput_test(redis_client, runs):
    key = "foo" 
    value = "a" * 1024 * 1024 # 1MB 

    read_start = time.time()
    for i in xrange(runs):
        redis_client.get(str(i))
    read_end = time.time()

    read = 8*runs/(read_end-read_start) 
    print "read throughput = " + str(read) + " Mb/s"
    print "read time = " + str(read_end-read_start) + " s"
    print str(runs) + " iterations" 

def write_throughput_test(redis_client, runs):
    key = "foo" 
    value = "a" * 1024 * 1024 # 1MB 

    write_start = time.time()
    for i in xrange(runs):
        redis_client.set(str(i), value)
    write_end = time.time()

    write = 8*runs/(write_end-write_start)     
    print "write throughput = " + str(write) + " Mb/s"
    print "write time = " + str(write_end-write_start) + " s" 
    print str(runs) + " iterations" 

def read_latency_test(redis_client, runs):
    times = []
    key = "foo" 
    value = "a" * 1024 * 1024 # 1MB 

    for i in xrange(runs):
        start = time.time()
        redis_client.get(str(i))
        end = time.time()
        times.append(end - start)

    read = sum(times) / len(times)
    print "read latency = " + str(read) + " s"
    print str(runs) + " iterations"     

def write_latency_test(redis_client, runs):
    times = []
    key = "foo" 
    value = "a" * 1024 * 1024 # 1MB 

    for i in xrange(runs):
        start = time.time()
        redis_client.set(str(i), value)
        end = time.time()
        times.append(end - start)

    write = sum(times) / len(times)
    print "write latency = " + str(write) + " s"
    print str(runs) + " iterations" 

def lambda_handler(event, context):
    redis_client = redis.Redis(host="clusterforlambdatest.a9ith3.0001.usw2.cache.amazonaws.com", port=6379)
    runs = 10000

    #write_throughput_test(redis_client, runs)
    #read_throughput_test(redis_client, runs)

    #write_latency_test(redis_client, runs)
    #read_latency_test(redis_client, runs)

    return str(runs) + " iterations" 


