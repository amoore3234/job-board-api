import array
from typing import List
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class JobPosting(Base):
    __tablename__ = "postings"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    job_title: Mapped[str] = mapped_column(String(100))
    job_url: Mapped[str] = mapped_column(String(255))
    company_logo: Mapped[str] = mapped_column(String(255))
    company_address: Mapped[str] = mapped_column(String(255))
    company_salary: Mapped[str] = mapped_column(String(50))
    company_metadata: Mapped[List[str]] = mapped_column(String(255))
    date_posted: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return f"JobPosting(id={self.id}, job_title={self.job_title}, job_url={self.job_url}, company_logo={self.company_logo}, company_address={self.company_address}, company_salary={self.company_salary}, company_metadata={self.company_metadata}, date_posted={self.date_posted})"