import os 
import sys
from src.mlprojectfirst.exception import CustomException
from src.mlprojectfirst.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql

#import pickle
import numpy as np

load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


def read_sql_data():
    logging.info("Reading sql database")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
             
        )
        logging.info("connection Esablisted",mydb)
        df=pd.read_sql_query('Select * from students', mydb)
        print(df.head())

        return df 
    except Exception as ex:
        raise CustomException(ex)