# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:41:56 2017

export query result to file!

@author: tamelill
"""

class Exporter:
    def __init__(self):
        pass
    
    def export_query_txt(self,query):
        f = open("textexport.txt", "w+")        
        for element in query:
            tostring = str(element)
            f.write(tostring + "\n")
        
        f.close()
        
    def export_query_csv(self,query):
        pass
    
       
       
