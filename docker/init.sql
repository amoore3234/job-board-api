CREATE TABLE IF NOT EXISTS postings (
  id SERIAL PRIMARY KEY,
  job_title VARCHAR(100),
  job_url VARCHAR(255),
  company_logo VARCHAR(255),
  company_title VARCHAR(100),
  company_address VARCHAR(255),
  company_salary VARCHAR(100),
  company_metadata VARCHAR(255),
  date_posted VARCHAR(50)
);