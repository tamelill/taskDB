# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:42:45 2017


ACHTUNG: PFAD ANPASSEN ZU Rscript

@author: tamelill
"""

import subprocess

def rsub_call():
    process = subprocess.Popen(['C:\\Users\\tamelill\\Documents\\R\\R-3.3.2\\bin\\Rscript','Rscript.R'], stdout=subprocess.PIPE,shell = True)
    process.wait()
    out,err = process.communicate()
    print(out.decode('utf-8'))