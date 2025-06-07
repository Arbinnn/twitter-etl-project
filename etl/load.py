
import pandas as pd
from sqlalchemy import create_engine

def load_to_csv(df, filename="elon_tweets.csv"):
    df.to_csv(filename, index=False)
    print(f"Saved to CSV: {filename}")

def load_to_sqlite(df, db_name="tweets.db"):
    engine = create_engine(f"sqlite:///{db_name}")
    df.to_sql("tweets", engine, if_exists="replace", index=False)
    print(f"Saved to SQLite DB: {db_name}")
