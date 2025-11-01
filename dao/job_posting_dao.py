import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mapping_model.job_posting_mapping import JobPostingMapping as JobPosting

load_dotenv()

database_url = os.getenv("POSTGRES_DATABASE_URL")

engine = create_engine(database_url, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class JobPostingDao:

    def add_job_posting(self, job_posting) -> None:
        with Session() as session:
            session.add(job_posting)
            session.commit()

    def add_job_postings(self, job_postings) -> None:
        with Session() as session:
            session.add_all(job_postings)
            session.commit()

    def get_job_posting_by_id(self, job_id) -> JobPosting:
        with Session() as session:
            return session.query(JobPosting).filter(JobPosting.id == job_id).first()

    def get_all_job_postings(self) -> list[JobPosting]:
        with Session() as session:
            return session.query(JobPosting).all()

    def delete_job_posting(self, job_id) -> None:
        with Session() as session:
            job_posting = self.get_job_posting_by_id(job_id)
            if job_posting:
                session.delete(job_posting)
                session.commit()

