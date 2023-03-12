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

def load_single_job_from_db(id):
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM jobs where id={}".format(id))).all()
    if len(results) > 0:
        job_list = [row._mapping for row in results]
        return dict(job_list[0])
    else:
        return None
    
def add_application_into_db(job_id, data):
    full_name = data['name'] 
    email = data['email']
    country = data['country']
    degree = data['degree']
    linkedin_url = data['linkedin']

    with engine.connect() as conn:
        insert_str = "INSERT INTO applications (job_id, full_name, email, country, degree, linkedin_url) VALUES ('{job_id}', '{full_name}', '{email}', '{country}', '{degree}', '{linkedin_url}');".format(job_id=job_id, full_name=full_name, email=email, country=country, degree=degree, linkedin_url=linkedin_url)
        conn.execute(text(insert_str))