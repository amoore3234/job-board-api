
from dao.job_posting_dao import JobPostingDao
from mapping_model.job_posting_mapping import JobPostingMapping
from model.job_posting_request import JobPostingRequest
from model.job_posting_response import JobPostingResponse


class JobPostingService:
    def __init__(self):
        self.repository = JobPostingDao()

    def create_job_posting(self, posting) -> JobPostingRequest:
        job_posting = self.save_job_posting(posting)
        return self.repository.add_job_posting(job_posting)

    def create_job_postings(self, job_data_list) -> list[JobPostingRequest]:
        job_mappings = []
        for posting in job_data_list:
            job_mapping = self.save_job_posting(posting)
            job_mappings.append(job_mapping)
        return self.repository.add_job_postings(job_mappings)

    def get_job_postings(self) -> list[JobPostingResponse]:
        return self.repository.get_all_job_postings()

    def get_job_posting_by_id(self, job_id) -> JobPostingResponse:
        return self.repository.get_job_posting_by_id(job_id)

    def delete_job_posting(self, job_id) -> None:
        self.repository.delete_job_posting(job_id)

    def save_job_posting(self, posting: JobPostingRequest) -> JobPostingMapping:
        return JobPostingMapping(
            job_title=posting.job_title,
            job_url=posting.job_url,
            company_logo=posting.company_logo,
            company_address=posting.company_address,
            company_salary=posting.company_salary,
            company_metadata=posting.company_metadata,
            date_posted=posting.date_posted
        )

