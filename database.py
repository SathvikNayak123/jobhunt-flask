import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

cloud_host=os.getenv('cloud_host')
cloud_key=os.getenv('cloud_key')


def load_jobs():
    timeout = 10
    conn = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host=cloud_host,
        password=cloud_key,
        read_timeout=timeout,
        port=23877,
        user="avnadmin",
        write_timeout=timeout,
    )

    cursor = conn.cursor()
    cursor.execute('select * from jobs')
    jobs=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return jobs
def search_jobs(id):
    timeout = 10
    conn = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host=cloud_host,
        password=cloud_key,
        read_timeout=timeout,
        port=23877,
        user="avnadmin",
        write_timeout=timeout,
    )
    cursor = conn.cursor()
    cursor.execute('select * from jobs where id = %s', (id,))
    job=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if len(job)==0:
        return None
    else:
        return job[0]
    
def add_application_to_db(job_id, data):
    query = """
        INSERT INTO applications 
        (job_id, full_name, email, linkedin, education, work_experience, resume_url) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """    
    timeout = 10
    conn = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host=cloud_host,
        password=cloud_key,
        read_timeout=timeout,
        port=23877,
        user="avnadmin",
        write_timeout=timeout,
    )
    cursor = conn.cursor()
    cursor.execute(query, (
        job_id, 
        data['name'],
        data['email'],
        data['linkedin'],
        data['education'],
        data['work_experience'],
        data['resume']
    ))
    conn.commit()
    cursor.close()
    conn.close()
