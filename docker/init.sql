CREATE TABLE IF NOT EXISTS postings (
  id SERIAL PRIMARY KEY,
  jobTitle VARCHAR(100),
  jobUrl VARCHAR(255),
  companyLogo VARCHAR(255),
  companyTitle VARCHAR(100),
  companyAddress VARCHAR(255),
  companySalary VARCHAR(100),
  companyMetadata VARCHAR(255),
  datePosted VARCHAR(50)
);