"""
Step 2:
transformation 
>> transform list into dataframe
>> add in new column named 'insert date' to show the ingested date and time

"""
import pandas as pd
from datetime import datetime
from google.cloud import bigquery
from load_to_bq import load_to_bq

def transform(data, headers):
    df = pd.DataFrame(data, columns=headers)
    df_str = df.astype(str)
    print(df_str.head())
    '''
    add new column 'insert date' to show the ingested date and time

    '''
    insertDate = datetime.utcnow()
    bq_client = bigquery.Client.from_service_account_json("secret_key.json")
    table_bq = 'myfirstproject-364809.socio_demographic.salaries_ethnicity_sex' # project.dataset.table
    df['insert_date'] = insertDate
    load_to_bq(bq_client, table_bq, df)

