import json
import urllib2
from pprint import pprint
from playhouse.postgres_ext import *

db = PostgresqlExtDatabase('my_database')  # note
json_data=open("survey2.json").read()

data = json.loads(json_data)
pprint(data)
