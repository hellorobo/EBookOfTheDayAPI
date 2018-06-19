from datetime import datetime
from dbase import Database

class EbookModelDB():

    def __init__(self):    
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

    def get(self):
            try:
                return freebooks.find_record({"date": today.strftime("%Y-%m-%d")})
                result = logs.insert_record({"date": today , "event": "record has been fetched from database"})
            except:
                return {"message": "Internal error occurred, while getting database record"}, 500
                result = logs.insert_record({"date": today , "event": "error while getting database record"})
