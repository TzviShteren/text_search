from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

elasticsearch_client = Elasticsearch(os.environ['ELASTICSEARCH_URL'], basic_auth=(
os.environ['ELASTICSEARCH_USER_NAME'], os.environ['ELASTICSEARCH_PASSWORD']))


def create_index_if_not_exists(client, index_name, mapping=None):

    if client.indices.exists(index=index_name):
        print(f"Index '{index_name}' already exists.")
    else:
        client.indices.create(index=index_name, body=mapping)
        print(f"Index '{index_name}' created successfully.")