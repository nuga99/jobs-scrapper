#!/usr/bin/python3
from bs4 import BeautifulSoup
from multiprocessing import pool

import os

# All type jobs suggest to use it for querying and scapping data
JOB_TYPE = ["Internship", 
            "Part Time", 
            "Full Time"]
            
'''
This class represents Job(s) Scrapper
using Beautiful Soup to gain data and 
via google dorks to get portal careers web.
'''

class JobsScrapper():

    def __init__(self):
        pass

    '''
    Handle captcha from google
    in order to sanitize being recognized a malicious
    input from google.
    '''
    def captcha_handle(self):
        pass

    '''
    Google dorks for searching subdomains
    web portal careers.
    '''
    def google_dorks(self, url):
        pass

    def job_type(self, job):
        pass


if __name__ == "__main__":
    run = JobsScrapper()
