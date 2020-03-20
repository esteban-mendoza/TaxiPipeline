# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:13:57 2020

@author: Jorge Esteban Mendoza Ortiz
"""

# Requisites:
# pip install sodapy
# MySQL Server 8.0.18
# MySQL Python Connector at https://dev.mysql.com/downloads/connector/python/

from Query import *

if __name__ == '__main__':
    # Download data from the whole Jan 1, 2018
    jan1 = fetch_day(d=1, m=1, y=2018, hours=[1])
    
    # Stores data trips into local database
    save_to_trips(jan1)
    
    