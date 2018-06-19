from scrap import Scrap
from dbase import Database
from datetime import datetime

url = 'https://www.packtpub.com/packt/offers/free-learning'
con_str = 'mongodb://h7r2v6rf8p9c:BLYv98kFW5bPYwufskSG@ds016138.mlab.com:16138/packtebook' 
db = 'packtebook' 
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

