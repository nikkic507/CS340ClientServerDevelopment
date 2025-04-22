#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 20:12:09 2025

@author: nichollecaudy_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    def __init__(self, AACUSER, AACPASS):
        # Initializing the MongoClient. Helps to
        # access the MongoDB databases and collections
        # This is hardwired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apport environment.
        # 
        #Connection Variables
        #
        AACUSER = 'aacuser' #username for AAC
        AACPASS = 'NEC123' #password for aac user
        AACHOST = 'nv-desktop-services.apporto.com' 
        AACPORT = 30498 #Mongo DB port
        AACDB = 'AAC' #Database
        AACCOL = 'animals' #collection
        #
        #Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (AACUSER,AACPASS,AACHOST,AACPORT))
        self.database = self.client['%s' % (AACDB)]
        self.collection = self.database['%s' % (AACCOL)]
   
    #Method to implement the C in CRUD    
    def create (self, data):
        if data is not None:
        #Insert data for new animal
           self.database.animals.insert_one(data) #data should be dictionary
           print("animal successfully added") #print when the animal is added
           return True
       #else print error message
        else:
            return False
            raise Exception('Nothing to save, data parameter is empty')
    
    #Method to implement the R in CRUD
    def read(self, data):
        #using find() to search DB from an animal
        if data is not None:
            data = self.database.animals.find(data, {'_id': False})
        #else print error message
        else:
                raise Exception('Nothing to read, dataSearch parameter is empty')
        return data
    
    #Method to implement the U in CRUD    
    def update(self, data, dataUpdate):
        #if data is available to update change data
        if data is not None:
             updated= self.database.animals.update_many(data, {'$set': dataUpdate})
       #else print error message      
        else: 
            raise Exception ('Nothing to update, update parameter empty')
        #displays number of documents updated
    
        return updated.modified_count  
    
    #Method to implement the D in CRUD
    def delete(self, data):
        #if data is available to delete, remove from database
        if data is not None:
            deleted = self.database.animals.delete_many(data)
        #else print an error message   
        else:
            raise Exception ('Nothing to delete, delete parameter is empty')
            #displays number of documents deleted
        
            return deleted.deleted_count
            
    