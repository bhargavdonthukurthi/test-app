import libsql_experimental as libsql
import os

url = "libsql://bhargav-bhargavdonthukurthi.turso.io"
auth_token = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzQwMTUxMzYsImlkIjoiYTc4NjExOGMtYTY1MC0xMWVlLTg1YzktMWE1OTZkZGUwY2MwIn0.3SkOzckYCTCPCjV0_JlbFyCWXs5iZveI3-XMu6WOd2zC4JHuqSKXJNXMUu-iq6NxtaAmMVFGIr5evDJnybR1Bg"

conn = libsql.connect("local.db", sync_url=url, auth_token=auth_token)
conn.sync()

cur = conn.cursor()

conn.execute("DROP TABLE IF EXISTS users;")
conn.execute("CREATE TABLE IF NOT EXISTS users (name TEXT);")
#conn.execute("CREATE TABLE MENU_ITEM (ID INT PRIMARY KEY , NAME NVARCHAR(255) NOT NULL, DESCRIPTION NVARCHAR(255), CREATED_AT NVARCHAR(20) );")
conn.execute("CREATE TABLE RAW_MATERIAL (ID INT PRIMARY KEY, NAME NVARCHAR(255) NOT NULL, SUPPLIER NVARCHAR(255), CREATED_AT NVARCHAR(20));")
conn.execute("CREATE TABLE UNIT_MEASURE (ID INT PRIMARY KEY, NAME NVARCHAR(50) NOT NULL, SYMBOL NVARCHAR(10), CREATED_AT NVARCHAR(20));")
conn.execute("CREATE TABLE RECIPE (ID INT PRIMARY KEY, MENU_ITEM_NAME NVARCHAR(255) NOT NULL, RAW_MATERIAL_NAME NVARCHAR(255) NOT NULL, QUANTITY INT NOT NULL, UNIT_MEASURE_NAME NVARCHAR(50) NOT NULL, MEMBER_COUNT INT DEFAULT 4, CREATED_AT NVARCHAR(20));")

2/2







conn.commit()


print(conn.execute("select * from users").fetchall())