from components.data_access.data_access import data_access
import pandas as pd
import sqlite3 as sql

class db_access(data_access):

    %load_ext sql
    %sql postgresql://postgres:Correlation1.@production.c2eu32xokeb1.us-east-1.rds.amazonaws.com/production

    var = %%sql SELECT * FROM clima_view
    print(var) 

    def __init__(self):
        pass


var = db_access()
