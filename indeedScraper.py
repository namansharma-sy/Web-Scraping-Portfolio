from selenium import webdriver
import pandas as pd
import time


def getData():
    joblist = []
    for i in range(0,41,10):
        url = f'https://in.indeed.com/jobs?q=python%20developer&l=Gurgaon%2C%20Haryana&start={i}&vjk=3d72edd1baefcba6'
        driver = webdriver.Chrome()
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source)

        #cardOutline tapItem fs-unmask result job_dd170dbc54ba036f resultWithShelf sponTapItem desktop


        divs = soup.find_all('div', class_ = "job_seen_beacon")

        for item in divs:
            title = item.find('a').text
            company = item.find(class_ = 'companyName').text
            try:
                salary = item.find(class_ = 'attribute_snippet').text
                if salary == 'Full-time': salary = ''
            except:
                salary = ''
            summary = item.find('div', class_ = 'job-snippet').text.strip().replace('\n', '')

            job = {
                'Title' : title,
                'Company': company,
                'Salary' : salary,
                'Summary': summary
            }
            joblist.append(job)

    df = pd.DataFrame(joblist)
    return df.to_csv("joblist.csv")

getData()