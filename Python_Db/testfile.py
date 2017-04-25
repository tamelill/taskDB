# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 13:40:48 2017

@author: tamelill
"""
import MySQLdb

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="tasks_db")
cursor = conn.cursor()
        
title = "Julia"
description = "Julia vs. MatLab"
person = "Michael"
try:
    cursor.execute("INSERT INTO task_table (Title,Description,Person) VALUES (%s,%s,%s)",(title,description,person))
    conn.commit()
except:
    print("Failed")
    conn.rollback()