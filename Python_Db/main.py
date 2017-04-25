# -*- coding: utf-8 -*-
"""
DB connection 
"""

import class_DB
import choose_file


myobj = class_DB.DB_communication()

title = input("Titel:\n")
description = input("Description:\n")
person = input("Person:\n")
myobj.insert_entry(title,description,person)




