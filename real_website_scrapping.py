from bs4 import BeautifulSoup
import requests
#import time

# Filtering out the data which matches the unfamiliar skill
print("Put some skills that you are not familiar with")
unfamiliar_skill = input(">")
print(f"Filtering Out: {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=Python&txtKeywords=Python%2C&cboWorkExp1=0&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        # filtering the jobs which is posted few days ago
        if 'few'in published_date:
            job_post = job.find('h2',class_='heading-trun').text.replace('\n','').replace('\t','').replace('\r','')
            company_name = job.find('h3',class_='joblist-comp-name').text.replace('\t','') .replace('\n','') .replace('\r','')
            skills = job.find('div',class_='srp-skills').text.replace('\t','').replace('\n','').replace('\r','')
            more_info = job.header.h2.a['href']
            # will filter the skill which we are familiar with
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                        f.write(f'''
                        Post: {job_post.strip()}
                        Company Name: {company_name.strip()} 
                        Required Skills: {skills.strip()}
                        Published Date: {published_date.strip()}
                        More Info: {more_info.strip()}'''
                    )
                        print(f'File Saved {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        #time_wait = 10
        #print(f"Waiting {time_wait} seconds...")
        #time.sleep(time_wait * 6)
