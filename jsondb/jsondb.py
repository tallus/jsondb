#!/usr/bin/env python
'''Contains JsonDB - load a dictionary from a json file as a key-value store'''

from __future__ import absolute_import, print_function, unicode_literals
import json
import os.path

class JsonDB_Error(Exception):
    pass

class JsonDB:
    '''load a dictionary from a json file as a key-value store'''
    def __init__(self, dbfile, readonly=False):
        '''load dbfile as dict, blank if file does not exist yes'''
        self.dbfile = os.path.expanduser(dbfile)
        self.readonly = readonly
        self.db  = self._load()

    def set(self, key, value):
        '''Set the (string,int,whatever) value of a key'''
        self.db[key] = value

    def get(self, key):
        '''Get the value of a key'''
        try:
            return self.db[key]
        except KeyError:
            return None

    def getall(self):
        '''return a list of all the keys'''
        return self.db.keys()

    def rem(self, key):
        '''Delete a key'''
        del self.db[key]
    
    def kexists(self, key):
        '''determine if key exists in db'''
        if key in self.db:
            return True
        else:
            return False
     
    def deldb(self):
        '''Delete everything from the database'''
        self.db = {}
    
    def _load(self):
        '''load db from file'''
        if os.path.exists(self.dbfile):
            try:
                db  = json.load(open(self.dbfile, 'rb'))
            except ValueError:
                raise JsonDB_Error('unable to open DB')
        else:
            db = {}
        if not self.readonly:
            try:
                json.dump(db, open(self.dbfile, 'wb'))
            except IOError:
                raise JsonDB_Error('unable to write to  DB')
        return db

    def dumpdb(self):
        '''write to file'''
        if self.readonly:
            raise JsonDB_Error('DB opened in read only mode')
        try:
            json.dump(self.db, open(self.dbfile, 'wb'))
        except IOError:
            raise  JsonDB_Error('unable to write to  DB')
        

if __name__ == "__main__":
    pass
