from app.db.elasticsearch_db.connection import elasticsearch_client as es
from elasticsearch import helpers


def insert_to_elasticsearch_events(data_list, index_name: str):
    try:
        actions = [
            {
                "_index": index_name,
                "_id": data['_id'],
                "_source": {k: v for k, v in data.items() if k != '_id'}
            }
            for data in data_list
        ]
        success, failed = helpers.bulk(es, actions, stats_only=False, raise_on_error=False)
        print(f"Bulk insert successful: {success} documents indexed.")
        if failed:
            print(f"Failed documents: {failed}")
    except Exception as e:
        print(f"Error during bulk insert: {e}")


def delete_all_events(index_name: str):
    try:
        response = es.delete_by_query(
            index=index_name,
            body={"query": {"match_all": {}}},
            conflicts="proceed"
        )
        print(f"Deleted {response['deleted']} documents from index '{index_name}'")
    except Exception as e:
        print(f"Error deleting documents: {e}")
