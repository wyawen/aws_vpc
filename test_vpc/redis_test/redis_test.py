import redis
import boto3
from rediscluster import StrictRedisCluster


def lambda_handler(event, context):
        # single redis node
        # redis_client = redis.Redis(host="clusterforlambdatest.a9ith3.0001.usw2.cache.amazonaws.com", port=6379)


        # redis cluster 
        startup_nodes = [{"host": "rediscluster-0001-001.a9ith3.0001.usw2.cache.amazonaws.com", "port": "6379"}]
        redis_client = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)


        redis_client.set("foo", "a")
	r = redis_client.get("foo")
        if (r is None):
		print "no such key"
		return -1
	if r == "a":
		print "success!"

	print str(r)

	s3_client = boto3.client('s3')
	bucket_name = 'yawen-tmp'
	s3_key = "bar"
	s3_value = "b"
	result = s3_client.put_object(
        	Bucket = bucket_name,
        	Body = s3_value, 
        	Key = s3_key
    	)
	
	body = s3_client.get_object(Bucket=bucket_name, Key=s3_key)['Body'].read()
	if body == s3_value:
		print "s3 success!"
	print body
	
	return r

