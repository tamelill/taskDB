# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:33:06 2017

@author: tamelill
"""

import pymysql
import pymysql.cursors



class DB_communication:
    '''comunicate with DB'''
    def __init__(self):
        try:
            self.conn = pymysql.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="Project_Scheme")
            self.cursor = self.conn.cursor()
            self.runningval = 1
        except:
            self.runningval = 0
            print("db not accessible")
        
    def my_print(self,string):
        print(string)
        
    def insert_entry(self,title,person,description,start):
        try:
            self.cursor.execute("INSERT INTO projects_table (Person,Title,Description,Start) VALUES (%s,%s,%s,%s)",(person,title,description,start,))
            self.conn.commit()
            print("\n ---- NEW ENTRY MADE ----\n")
        except:
            print("Failed")
            self.conn.rollback()
        
    def read_all(self):
        try:
            self.cursor.execute("SELECT * FROM projects_table")
            entrylist = self.cursor.fetchall()
            self.conn.commit()
            return entrylist
        except:
            print("reading Failed")
            self.conn.rollback()
            return 0

    def filter_person(self,str2):
        name = str2
        try:
            self.cursor.execute("SELECT * FROM projects_table WHERE Person = (%s)",(name,))
            entrylist = self.cursor.fetchall()
            self.conn.commit()
            return entrylist
        except:
            print("reading Failed")
            self.conn.rollback()
            return 0
    
    def filter_open(self):
        
        try:
            self.cursor.execute("SELECT * FROM projects_table WHERE NOT Done")
            entrylist = self.cursor.fetchall()
            self.conn.commit()
            return entrylist
        except:
            print("reading Failed")
            self.conn.rollback()
            return 0
    
    def file_export(self):
        try:
            self.cursor.execute("SELECT * FROM projects_table")
            entrylist = self.cursor.fetchall()
            self.conn.commit()
            return entrylist
        except:
            print("reading Failed")
            self.conn.rollback()
            return 0
        
    def export_csv(self):
        try:
            #TODO: find a way to overwrite (or timestamp) table.csv!
            self.cursor.execute("""SELECT * FROM projects_table INTO OUTFILE "C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/table.csv" """)
            self.conn.commit()
            print("\n ---- Export Done----\n")
        except:
            print("Failed")
            self.conn.rollback()
        
    
    