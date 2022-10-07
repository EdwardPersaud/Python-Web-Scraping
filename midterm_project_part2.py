#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 20:03:13 2020

@author: edward
"""
#Edward Persaud-MGS314 Recitation Section B2
import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/jobs?q=python&l=New+York'
page = requests.get(URL)
jobs_file = open('jobs.txt', 'w')
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsBody')
job_elems = results.find_all("div", class_ ='jobsearch-SerpJobCard')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_ = 'title')
    company_elem = job_elem.find('span', class_ = 'company')
    location_elem = job_elem.find('div', class_ = 'location accessible-contrast-color-location')
    web_elem = job_elem.find('a')['href']
    if None in (title_elem, company_elem, location_elem):
        continue
    jobs_file.write('Job title: '+title_elem.text.strip()+'\n')
    jobs_file.write('Company: '+company_elem.text.strip()+'\n')
    jobs_file.write('Location: '+location_elem.text.strip()+'\n')
    jobs_file.write('URL: '+"https://www.indeed.com" + web_elem.strip()+"\n"+'-----------------------------------'+"\n")

jobs_file.close()
