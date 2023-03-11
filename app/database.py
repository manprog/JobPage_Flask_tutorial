from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
import os

db_conn_str = os.getenv("db_conn_str")
engine = create_engine(db_conn_str, 
                       connect_args={
                        "ssl": { "ssl_ca": "/etc/ssl/cert.pem" }
                       }
                    )

def load_jobs_from_db():
    jobs_list = []
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM jobs")).all()
        jobs_list = [row._mapping for row in results]
    return jobs_list