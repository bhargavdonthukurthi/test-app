
from sqlalchemy import create_engine
import pandas as pd

TURSO_DATABASE_URL = "libsql://bhargav-bhargavdonthukurthi.turso.io"
TURSO_AUTH_TOKEN = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzQwMTUxMzYsImlkIjoiYTc4NjExOGMtYTY1MC0xMWVlLTg1YzktMWE1OTZkZGUwY2MwIn0.3SkOzckYCTCPCjV0_JlbFyCWXs5iZveI3-XMu6WOd2zC4JHuqSKXJNXMUu-iq6NxtaAmMVFGIr5evDJnybR1Bg"

dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

engine = create_engine(dbUrl, connect_args={'check_same_thread': False}, echo=True)

pd.read_sql("select * from users", engine)


