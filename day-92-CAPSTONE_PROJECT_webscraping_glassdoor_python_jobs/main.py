from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

GLASSDOOR_URL = "https://www.glassdoor.com.br"
GLASSDOOR_USERNAME = "your@email.com"
GLASSDOOR_PASSWORD = "yourpassword"
JOB_TO_SEARCH = "python junior"
JOB_LOCATION = "São Paulo, Brasil"
python_jobs = []
file_name = JOB_TO_SEARCH.replace(" ", "")

opt = Options()
# Limit the size of window
opt.add_argument('window-size=800,800')
# opt.headless = True  # Do all the code without opening browser

driver = webdriver.Chrome(options=opt)
# Add wait time until 30 second to all commands, try 2 times per second
driver.implicitly_wait(30)

# Open a webpage
driver.get(GLASSDOOR_URL)

# Login and search for specified job and location
enter_login = driver.find_element(By.CLASS_NAME, "LockedHomeHeaderStyles__signInButton")
enter_login.click()
user_field = driver.find_element(By.XPATH, '//*[@id="modalUserEmail"]')
user_field.send_keys(GLASSDOOR_USERNAME)
password_field = driver.find_element(By.XPATH, '//*[@id="modalUserPassword"]')
password_field.send_keys(GLASSDOOR_PASSWORD)
enter_login2 = driver.find_element(By.XPATH, '//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/form/div[3]/button/span')
enter_login2.click()
jobs_search = driver.find_element(By.XPATH, '//*[@id="SiteNav"]/nav[2]/div/div/div[2]/div[1]/div[2]/a/span/div/span[1]')
jobs_search.click()
search = driver.find_element(By.XPATH, '//*[@id="SearchForm"]/div[1]/button/span')
search.click()
enter_job = driver.find_element(By.XPATH, '//*[@id="scKeyword"]')
enter_job.send_keys(JOB_TO_SEARCH)
enter_place = driver.find_element(By.XPATH, '//*[@id="scLocation"]')
enter_place.send_keys(Keys.CONTROL + "a")
enter_place.send_keys(JOB_LOCATION)
enter_place.submit()
exit_window = driver.find_element(By.XPATH, '//*[@id="JAModal"]/div/div[2]/span')
exit_window.click()

# Get page content with BeautifulSoap, find all jobs
page_content = driver.page_source
site = BeautifulSoup(page_content, 'html.parser')
jobs = site.findAll('div', attrs={'class': 'd-flex flex-column pl-sm css-1buaf54 job-search-key-1mn3dn8 e1rrn5ka0'})

# Iterate with Beautiful Soup, the jobs into the page, get company, title, location and link
for job in jobs:
    # get parameters for each job
    job_company_name = (job.find('span')).text
    job_title = (job.find(attrs={'class': 'jobLink job-search-key-1rd3saf eigr9kq1'})).text
    job_location = (job.find(attrs={'class': 'css-1buaf54 pr-xxsm job-search-key-iii9i8 e1rrn5ka4'})).text
    job_link = f"{GLASSDOOR_URL}{job.find(attrs={'class': 'jobLink job-search-key-1rd3saf eigr9kq1'})['href']}"
    python_jobs.append([job_company_name, job_title, job_location, job_link])

# This code to list all jobs to get more detailed information
list_jobs = driver.find_elements(By.CLASS_NAME, "react-job-listing")

# This code loop through all jobs, click and "get description"
for i, job in enumerate(list_jobs):
    job.click()
    # Increase time in case of NoSuchWindowException
    time.sleep(10)
    # # Need to find a solution to WebDriverWait inside this loop
    # wait = WebDriverWait(driver, 15)
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="JobDescriptionContainer"]/div[2]/span/svg')))
    job_page_content = driver.page_source
    job_site = BeautifulSoup(job_page_content, 'html.parser')
    job_description = job_site.find('div', attrs={'class': 'jobDescriptionContent desc'})
    # Add the description to each job list
    python_jobs[i].append(job_description.text)

# Transform the matrix into a dataframe, with titles
dados = pd.DataFrame(python_jobs, columns=['Company', 'Title', 'Location', 'URL', 'Description'])

# Convert dataframe to CSV
dados.to_csv(f'{file_name}jobs.csv', index=False)
