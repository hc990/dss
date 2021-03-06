#grab the current path so we can set some thing automatically
import sys
app_path = sys.path[1]

#the app version. you can use in templates via the Filters.version() helper. 
#good for browser cache busting on js & css 
version = '0.1'

#run mode
mode = "development"

#define a port for testing
port = 8000

#set static resources path
static_path = "%s/static" % app_path

#define a dir for mako to look for templates - relative to the app directory
template_dir = "%s/views" % app_path

#define a dir for mako to cache compiled templates
mako_modules_dir = "%s/tmp/mako_modules" % app_path

#define a log file... optionally just use the string 'db' to log it to mongo
log = "%s/tmp/log/application.log" % app_path

#define a database host
db_host = '127.0.0.1'

#define the database port
db_port = 27017

#define the database name
db_name = 'zongdb'

#uncomment the following if when using redis session middleware

#redis host
redis_host = '127.0.0.1'

#redis port
redis_port = 6379

#redis db name
redis_db = 0

#uncomment the following when using memcache session middleware

#memcache host
#memcache_host = 'localhost'

#you must define a cookie secret. you can use whirlwind-admin.py --generate-cookie-secret
cookie_secret = "setthistoyourowncookiesecret"
    

middleware_classes = [
    "core.middleware.flash.middleware.FlashMiddleware",
    "core.middleware.session.middleware.SessionMiddleware"
#    "core.middleware.session.redis.middleware.SessionMiddleware"  
     #"whirlwind.middleware.session.memcache.middleware.SessionMiddleware"
]
