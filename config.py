#Application configuration File
################################

#Secret key that will be used by Flask for securely signing the session cookie
# and can be used for other security related needs
SECRET_KEY = 'SECRET_KEY'

#######################################
#Minimum Number Of Tasks To Generate
MIN_NBR_TASKS = 1

#Maximum Number Of Tasks To Generate
MAX_NBR_TASKS = 100

#Time to wait when producing tasks
WAIT_TIME = 1

#Webhook endpoint Mapping to the listener
WEBHOOK_RECEIVER_URL = 'rediss://:2IHchZ2uPNdNte39p5roLu4Sv2vL59Re9AzCaBOqprM=@POW.redis.cache.windows.net:6380/0?ssl_cert_reqs=required'
#######################################

#Map to the REDIS Server Port
BROKER_URL = 'rediss://:2IHchZ2uPNdNte39p5roLu4Sv2vL59Re9AzCaBOqprM=@POW.redis.cache.windows.net:6380/0?ssl_cert_reqs=required'
#######################################

AZURE_REDIS_CONNECTIONSTRING = "2IHchZ2uPNdNte39p5roLu4Sv2vL59Re9AzCaBOqprM=@POW.redis.cache.windows.net:6380/0?ssl_cert_reqs=required"

#"POW.redis.cache.windows.net"
#myPassword = "2IHchZ2uPNdNte39p5roLu4Sv2vL59Re9AzCaBOqprM="
