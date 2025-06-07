import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("tweets.db")

# Run a SQL query
query = "SELECT date(created_at) AS date, COUNT(*) AS count FROM tweets GROUP BY date"
# query = "SELECT * FROM tweets"
df = pd.read_sql(query, conn)

# Preview the data
print(df.head())
