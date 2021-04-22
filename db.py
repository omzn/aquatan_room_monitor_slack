#!/usr/bin/python
import sys
import os
import MySQLdb
import re
import time
from time import strftime
from datetime import datetime as dt

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/lib')

class DB:
    def __init__(self, dbhost, dbname, dbuser, dbpass):
        self.dbhost = dbhost
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpass = dbpass

    def open(self):
        try:
            self.connector = MySQLdb.connect(host=self.dbhost, 
                              db=self.dbname, 
                              user=self.dbuser, 
                              passwd=self.dbpass)
            self.dbh = self.connector.cursor()
        except:
            return False
        return True
    
    def close(self):
        if self.dbh is not None:
            self.dbh.close()
        if self.connector is not None:
            self.connector.close()

    def v(self,label):
        if self.open():
            sql = "SELECT value,timestamp FROM log WHERE label=%s ORDER BY timestamp DESC LIMIT 1"
            self.dbh.execute(sql, (label,))
            result = self.dbh.fetchall()
            if len(result) != 0:
                retval = result[0]
            else:
                retval = None
            self.close()
            return retval
        else:
            return None

    def n(self,label):
        if self.open():
            sql = "SELECT note,timestamp FROM log WHERE label=%s ORDER BY timestamp DESC LIMIT 1"
            retval = None
            self.dbh.execute(sql,(label,))
            result = self.dbh.fetchall()
            if result:
                retval = result[0]
            self.close()
            return retval
        else:
            return None

    def set_n(self,label,note):
        if self.open():
            tdatetime = dt.now()
            ts = tdatetime.strftime('%Y-%m-%d %H:%M:%S')
            sql = "INSERT INTO log VALUES(null,%s,%s,null,%s)"
            self.dbh.execute(sql,(ts,label,note))
            self.connector.commit()
            self.close()

    def ibeaconList(self):
        if self.open():
            sql = "SELECT label,place,slack FROM room_monitor WHERE slack IS NOT NULL"
            self.dbh.execute(sql,)
            result = self.dbh.fetchall()
            self.close()
            return result
        else:
            return ()

                        
def main():
    db = DB('10.0.0.1','ibeacon','aquatan','aquatan')
    
if __name__ == '__main__':
    main()
