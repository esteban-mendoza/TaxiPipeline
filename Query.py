# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:57:10 2020

@author: Jorge Esteban Mendoza Ortiz
"""

import pandas as pd
from sodapy import Socrata
from MySQLConnector import MySQLConnector


client = Socrata(
    domain="data.cityofnewyork.us",
    app_token="qVLvr56Nnt8io67HJ3Xy6DkUi",
    username="esteban.mendoza@outlook.com",
    password="M3nd0z40_",
    timeout=60
)


def fetch_day(d, m, y=2018, hours=range(24), limit=50000):
    """
    Fetches trips given a day, month, year and range of hours
    using the SODA API from data.cityofnewyork.us
    
    Input
        d:     int of day
        m:     int of month
        y:     int of year
        hours: iterable of hours
        limit: int 0-50,000 of number of registers per request for each hour
    
    Output
        regs:  list of dictionaries with registers fetched
    """
    # Resultant list
    regs = list()
    
    # Fetches 50000 results for each hour, 
    # returned as JSON from API / converted to Python 
    # list of dictionaries by sodapy.    
    for h in hours:    
        result = client.get("t29m-gskq",
            content_type="json",
            where=f"tpep_pickup_datetime between '{y}-{m:02}-{d:02}T{h:02}:00:00.000' and '{y}-{m:02}-{d:02}T{h:02}:59:59.999'",
            limit=limit)
        
        # Appends result to regs
        regs += result
        
    return regs


def save_to_trips(registers):
    """
    Saves a list of registers to local>taxi>trips
    
    Input:
        registers: list of suitable dictionaries
    
    Output:
        None
    """
    # Create MySQL connection
    cnx = MySQLConnector()
    
    # Insert registers into trips table
    for reg in registers:
            cnx.insert(reg)
    # Close connection
    cnx.close()


if __name__ == '__main__':
    # Example
    ex = fetch_day(d=1, m=1, y=2018, hours=[1], limit=5)
    
    print(pd.DataFrame.from_records(ex))
