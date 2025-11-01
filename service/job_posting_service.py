
from dao.job_posting_dao import JobPostingDao


class JobPostingService:
    def __init__(self):
        self.repository = JobPostingDao()

    def create_job_posting(self, job_data):
        return self.repository.add_job_posting(job_data)

    def create_job_postings(self, job_data_list):
        return self.repository.add_job_postings(job_data_list)

    def get_job_postings(self):
        return self.repository.get_all_job_postings()

    def get_job_posting_by_id(self, job_id):
        return self.repository.get_job_posting_by_id(job_id)

    def delete_job_posting(self, job_id):
        return self.repository.delete_job_posting(job_id)