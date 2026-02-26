from datetime import datetime
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from pathlib import Path
import os

import psycopg
from psycopg.rows import dict_row


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5433")),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "postgres"),
    "dbname": os.getenv("DB_NAME", "eshop"),
}

def get_db_connection():
    return psycopg.connect(**DB_CONFIG, row_factory=dict_row)

app = FastAPI(title="E-Shop-СI-CD")

@app.get("/products")
async def get_products():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_all_products()")
            return [{**dict(r), "price": float(r["price"])} for r in cur.fetchall()]
    finally:
        conn.close()

@app.get("/health")
async def health():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT get_products_count()")
            count = cur.fetchone()["get_products_count"]
        return {"status": "ok", "products": count}
    finally:
        conn.close()


