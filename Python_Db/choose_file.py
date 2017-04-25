# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:30:35 2017

@author: tamelill
"""

import class_DB
import os
import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import rsubcall
import write_file
import show_bar
import cmd_commands
#import class_exporter


def choose_option():
    myobj = class_DB.DB_communication()
    print("Hey Hoh, what do you want to do?:\n")
    
    if myobj.runningval == 1:
        print("db accessible")
    
        inputvar = "init"
        
        while inputvar != "exit":
            inputvar = input("<make> entry, <read> db, <export> , <barplot> or <exit>\n")
            
            if inputvar == "make":
                title = input("Titel:\n")
                description = input("Description:\n")
                person = input("Person:\n")
                datestart = input("(optional)Start d m Y:\n")
            
                try:
                    start = datetime.datetime.strptime(datestart, "%d %m %Y").date()
                except:
                    start = datetime.date.today()
                
                print(start)
                
                myobj.insert_entry(title,person,description,start)
            
            elif inputvar == "read":
                entrylist = myobj.read_all()
                print(entrylist)
            
            elif inputvar == "fileupload":
                content = myobj.read_file("H:\Python_Db")
                print(content)
                
            elif inputvar == "export":
                data = myobj.file_export()      
                try:
                    write_file.write_file(data) 
                    rsubcall.rsub_call()
    
                except: 
                    print("writing failure\n")
                    
            elif inputvar == "barplot":
                
                show_bar.show_barplot()
                
                #print(os.getcwd())
                #myobj.export_csv()
                #expobj = class_exporter.Exporter()
                #expobj.export_query_txt(content)
                
                
            elif inputvar.startswith("read "):
                try:
                    words = inputvar.split()
                    if len(words) > 1:
                        if words[1] == "opentasks":
                            datalist = myobj.filter_open()
                        elif words[1] == "all":
                            datalist = myobj.read_all()
                        else:
                            datalist = myobj.filter_person(words[1])
                    if len(words) > 2:
                        if words[2] == "txt":
                            name = words[1]
                            write_file.write_file(datalist,name)
                    else:
                        write_file.write_cmd(datalist)
                except: 
                    print("invalid input...\n")
                
            elif inputvar == "cls":
                cmd_commands.cls()
                
    else:
        print("local mode:")
        
        inputvar = "init"
        while inputvar != "exit":
            inputvar = input("<export>, <barplot> or <exit>\n")
        
            if inputvar == "export":     
                try:
                    rsubcall.rsub_call()
                except: 
                    print("writing failure\n")
                
            elif inputvar == "barplot":
                
                show_bar.show_barplot()
            

    
    
    
    
    