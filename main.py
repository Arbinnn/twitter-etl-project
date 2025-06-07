from etl.extract import extract_tweets
from etl.transform import transform_tweets
from etl.load import load_to_csv, load_to_sqlite

def main():
    user_id = "44196397"  # Elon Musk's user ID
    raw_data = extract_tweets(user_id)
    transformed_data = transform_tweets(raw_data)
    load_to_csv(transformed_data)
    load_to_sqlite(transformed_data)

if __name__ == "__main__":
    main()
