from model.job_posting_request import JobPostingRequest
from model.job_posting_response import JobPostingResponse
from service.job_posting_service import JobPostingService
from fastapi import FastAPI, HTTPException
from mapping_model.job_posting_mapping import JobPostingMapping

app = FastAPI()

@app.post("/posting",
          response_model=JobPostingResponse,
          summary="Create a new job posting",
          description="Create job posting to store in the database.")
async def create_job(posting: JobPostingRequest):

    job_posting = JobPostingMapping(
        job_title=posting.job_title,
        job_url=posting.job_url,
        company_logo=posting.company_logo,
        company_address=posting.company_address,
        company_salary=posting.company_salary,
        company_metadata=posting.company_metadata,
        date_posted=posting.date_posted
    )

    service = JobPostingService()
    service.create_job_posting(job_posting)
    return posting

@app.post("/add_postings",
          response_model=list[JobPostingResponse],
          summary="Create multiple job postings",
          description="Create multiple job postings to store in the database.")
async def create_jobs(postings: list[JobPostingRequest]):
    job_mappings = []
    for posting in postings:
        job_posting = JobPostingMapping(
            job_title=posting.job_title,
            job_url=posting.job_url,
            company_logo=posting.company_logo,
            company_address=posting.company_address,
            company_salary=posting.company_salary,
            company_metadata=posting.company_metadata,
            date_posted=posting.date_posted
        )
        job_mappings.append(job_posting)

    service = JobPostingService()
    service.create_job_postings(job_mappings)
    return postings

@app.get("/postings",
         response_model=list[JobPostingResponse],
         summary="Get all job postings",
         description="Retrieve all job postings from the database.")
async def get_all_jobs():
    service = JobPostingService()
    return service.get_job_postings()

@app.get("/posting/{job_id}",
         response_model=JobPostingResponse,
         summary="Get a job posting by ID",
         description="Retrieve a specific job posting using its ID.")
async def get_job_by_id(job_id: int):
    service = JobPostingService()
    job = service.get_job_posting_by_id(job_id)
    if job:
        return job
    else:
        raise HTTPException(status_code=404, detail="Job posting {job_id} not found")

@app.delete("/posting/{job_id}",
            summary="Delete a job posting by ID",
            description="Delete a specific job posting using its ID.")
async def delete_job(job_id: int):
    service = JobPostingService()
    service.delete_job_posting(job_id)
