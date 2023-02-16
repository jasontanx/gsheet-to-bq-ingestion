from google.cloud import bigquery
import logging
import time

def get_logging_format() -> logging.Logger:
    """
    function to return custom format logging

    return logging.Logger
    """

    logging.Formatter.converter = time.gmtime
    logging.basicConfig(
        format="[%(asctime)s,%(msecs)d] %(levelname)-8s [%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d, %H:%M:%S",
        level=logging.INFO,
    )
    _logger: logging.Logger = logging.getLogger("de-logging")
    return _logger


logger: logging.Logger = get_logging_format()

def load_to_bq(bq_client, table_bq, df):
    '''
    load to bq
    '''
    logger.info("ingesting to bq...")
    bq_client = bigquery.Client.from_service_account_json('/Users/junshengtan/Desktop/gsheet-to-bq-ingestion/secret_key.json')
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition="WRITE_TRUNCATE" # "WRITE_APPEND" as alternative
    job = bq_client.load_table_from_dataframe(
        df, table_bq, job_config=job_config) 
    job.result() 
    logger.info("Data ingested to BQ -> %s", table_bq)
