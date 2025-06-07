import pandas as pd
import re

def clean_text(text):
    text = re.sub(r"http\\S+", "", str(text))
    text = re.sub(r"@\\w+", "", text)
    text = re.sub(r"#\\w+", "", text)
    text = re.sub(r"RT\\s", "", text)
    text = re.sub(r"\\s+", " ", text).strip()
    return text

def transform_tweets(raw_tweets):
    df = pd.DataFrame(raw_tweets)
    df["clean_text"] = df["text"].apply(clean_text)
    df["length"] = df["clean_text"].apply(len)
    df["word_count"] = df["clean_text"].apply(lambda x: len(x.split()))
    df["hashtag_count"] = df["text"].apply(lambda x: len(re.findall(r"#\\w+", str(x))))
    df["is_retweet"] = df["text"].str.startswith("RT")
    df["created_at"] = pd.to_datetime(df["created_at"], errors='coerce')
    df["date"] = df["created_at"].dt.date
    df["hour"] = df["created_at"].dt.hour
    df = df.drop_duplicates(subset="id")
    df = df.dropna(subset=["clean_text"])
    return df
