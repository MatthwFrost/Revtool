#!/usr/bin/env python

# Learning how to scrape canvas

import requests
import json
from dotenv import load_dotenv
import os

dotenv_path = "../../.env"
load_dotenv(dotenv_path=dotenv_path)
CANVAS_TOKEN = os.getenv('CANVAS_TOKEN')

cookies = {
    '_legacy_normandy_session': CANVAS_TOKEN
}


data = requests.get('https://canvas.swansea.ac.uk/api/v1/dashboard/dashboard_cards', cookies=cookies).json()

substring = "2223"
course_details = []

for i in data:
    if substring in i['originalName']:
        course_details.append({
            'course_name': i['originalName'],
            'course_code': i['courseCode'][5:],
            'course_path': i['href']
        })


with open('course_info.json', 'w') as f:
    json.dump(course_details, f, ensure_ascii=False, indent=4)
    f.close()


