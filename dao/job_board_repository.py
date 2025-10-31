import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.job_posting import JobPosting

load_dotenv()

database_url = os.getenv("POSTGRES_DATABASE_URL")
print(f"Database URL: {database_url}")

engine = create_engine(database_url, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class JobBoardRepository:

    def add_job_posting(self, job_posting) -> None:
        with Session() as session:
            session.add(job_posting)
            session.commit()
    
    def add_job_postings(self, job_postings):
        self.session.add_all(job_postings)
        self.session.commit()

    def get_job_posting_by_id(self, job_id):
        return self.session.query(JobPosting).filter(JobPosting.id == job_id).first()

    def get_all_job_postings(self):
        return self.session.query(JobPosting).all()

    def delete_job_posting(self, job_id):
        job_posting = self.get_job_posting_by_id(job_id)
        if job_posting:
            self.session.delete(job_posting)
            self.session.commit()

