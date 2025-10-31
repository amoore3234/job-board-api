from dao.job_board_repository import JobBoardRepository
from model.job_posting import JobPosting
from model.person import Person
from model.vehicle import Vehicle

# Function to calculate the sum of two numbers
def calculate_sum(a, b):
    return a + b
print(calculate_sum(3, 5))

# Function to concatenate strings with numbers from 0 to 9
def concat_strings(str):
    index = 0
    while index < 10:
        str += index.__str__() + " "
        index += 1
    return str
print(concat_strings(""))

# Function to iterate over a range of numbers
def iterate_numbers(n, m):
    for i in range(n, m):
        print(i)
print(iterate_numbers(5, 10))

# Function to iterate over a list of items
items = ["apple", "banana", "cherry"]
def iterate_items(items):
    for item in items:
        print(item)
print(iterate_items(items))

# Function to iterate over a dictionary and print key-value pairs
dictionary = {"name": "Tony", "age": 35, "city": "Fontana"}
def iterate_dictionary(dict):
    for key, value in dictionary.items():
        print("Key: %s, Value: %s" %(key, value))
print(iterate_dictionary(dictionary))

# Creating an instance of Vehicle and printing number of wheels
sonic_lt_turbo = Vehicle(4, "Gasoline", 4, 250)
print (f"Number of wheels: {sonic_lt_turbo.number_of_wheels}")
sonic_lt_turbo.set_number_of_wheels(6)
print (f"Updated number of wheels: {sonic_lt_turbo.number_of_wheels}")

my_person = Person()
my_person.set_name("Alice")
print(f"Person's name: {my_person.get_name()}")

job_posting = JobPosting(
    job_title="Frontend Engineer",
    job_url="https://example.com/jobs/1",
    company_logo="https://example.com/logo.png",
    company_address="11523 Newport Blvd, Newport Beach, USA",
    company_salary="$200,000",
    company_metadata=["Python", "React", "Java"],
    date_posted="2025-07-15"
)

repository = JobBoardRepository()
repository.add_job_posting(job_posting)

