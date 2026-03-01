# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Connection Variables 
        USER = 'aacuser' 
        PASS = 'pass909275'
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals'  
        
        # Initialize Connection 
        
        connection_string = f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/{DB}?authSource=admin'
        
        self.client = MongoClient(connection_string)
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """ Implements the C in CRUD """
        if data is not None:
            # Inserts data into the collection and checks for success
            insert_result = self.collection.insert_one(data) 
            return True if insert_result.acknowledged else False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def read(self, query=None): 
        """ Implements the R in CRUD """
        if query is None:
            query = {}
            
        try:
            # Converts the cursor result into a list
            cursor = self.collection.find(query)
            result = [doc for doc in cursor]
            return result
        except Exception as e:
            print(f"Error querying documents: {e}")
            return []
        
    def update(self, query, update_data):
        """Implements the U in CRUD"""
        if query is not None and update_data is not None:
            # update_many used to handle one or multiple matches
            # The '$set' operator is used to update specific fields
            result = self.collection.update_many(query, {"$set":update_data})
            return result.modified_count
        else:
            raise Exception("Update failed: Query or Update Data is empty")
            
        
    def delete(self, query):
        """Implements the D in CRUD"""
        if query is not None:
            # delete_many returns a result object containing the count of deleted documents
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Delete failed: Query parameter is empty")