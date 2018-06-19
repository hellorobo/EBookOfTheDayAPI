import pymongo

class Database():
    def __init__(self, connection, database, collection):
        self.dbcol = database+"/"+collection
        self.connection = pymongo.MongoClient(connection)
        self.db = self.connection[database]
        self.col = self.db[collection]
        print("opened new connection to "+self.dbcol)

    def find_record(self, json):
        return self.col.find_one(json)

    def insert_record(self, json):
        return self.col.insert_one(json)
    
    def __del__(self):
        print("closing "+self.dbcol+ " connection")
        return self.connection.close()
