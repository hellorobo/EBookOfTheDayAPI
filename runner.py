from scrap import Scrap
from dbase import Database
from datetime import datetime

dbserver = os.environ['DB_SERVER']
dbname = os.environ['DB_NAME']
dbuser = os.environ['DB_USER']
dbpass = os.environ['DB_PASS']
con_str = pymongo.MongoClient('mongodb://{}:{}@{}/{}'.format(dbuser,dbpass,dbserver,dbname))
db = dbname
col_freebooks = 'freebooks'
col_logs = 'logs'
freebooks = Database(con_str, db, col_freebooks)
logs = Database(con_str, db, col_logs)
today = datetime.utcnow()

if freebooks.find_record({"date": today.strftime("%Y-%m-%d")}):
    result = logs.insert_record({"date": today , "event": "record already in the database, skipping"})
    print('record already exists')
else:
    document = Scrap().get(url)
    result = freebooks.insert_record(document.json())
    result = logs.insert_record({"date": today , "event": "new record added to database"})
    print('new record added')

