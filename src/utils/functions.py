import streamlit as st 
import pandas as pd
from typing import List
from psycopg2 import connect, sql
from dotenv import load_dotenv
import os 
import psycopg2

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DATABASE_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')



@st.cache_data
def load_data(file_path:str, cols:List) -> pd.DataFrame:
    """
    Load data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
        cols (List): List of columns to convert to datetime.
        
    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    # check extension of the file_path
    if file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
        for column in cols:
            data[column] = pd.to_datetime(data[column], errors='coerce')
            return data 
    elif file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
        for column in cols:
            data[column] = pd.to_datetime(data[column], errors='coerce')
        return data 

@st.cache_data
def get_data(table_name: str, date_cols:List[str], float_cols:List[str]) -> pd.DataFrame:
    """
    Get data from a database table.
    
    Args:
        database_name (str): Name of the database.
        table_name (str): Name of the table.
        
    Returns:
        pd.DataFrame: DataFrame containing the data from the table.
    """

    try: 
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cur = conn.cursor()
        query = sql.SQL("SELECT * FROM tca.{}").format(sql.Identifier(table_name))
        cur.execute(query)
        data = cur.fetchall()
        data = pd.DataFrame(data, columns=[desc[0] for desc in cur.description])
        cur.close()
        conn.close()
        for column in date_cols:
            data[column] = pd.to_datetime(data[column], errors='coerce')
        for column in float_cols:
            data[column] = pd.to_numeric(data[column], errors='coerce')
        return data

    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return pd.DataFrame()
    






        

