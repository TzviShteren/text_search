from app.db.mongo_db.connection import get_collection_events, get_collection_news
import pandas as pd


def clearing_events():
    data = list(get_collection_events().find({}))
    df = pd.DataFrame(data)

    df['latitude'] = df['location'].apply(lambda x: x.get('latitude') if isinstance(x, dict) else None)
    df['longitude'] = df['location'].apply(lambda x: x.get('longitude') if isinstance(x, dict) else None)

    df = df.dropna(subset=["summary", "latitude", "longitude"])

    df = df[["_id", "summary", "latitude", "longitude"]]

    return df.to_dict(orient="records")


def clearing_news():
    data = list(get_collection_news().find({}))
    df = pd.DataFrame(data)

    df['latitude'] = df['location'].apply(lambda x: x.get('latitude') if isinstance(x, dict) else None)
    df['longitude'] = df['location'].apply(lambda x: x.get('longitude') if isinstance(x, dict) else None)

    df = df.dropna(subset=["summary", "latitude", "longitude"])

    df = df[["_id", "summary", "latitude", "longitude"]]

    return df.to_dict(orient="records")
