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

params = {
    'exclude_assignment_submission_types[]': 'wiki_page',
    'exclude_response_fields[]': [
        'description',
        'rubric',
    ],
    'include[]': [
        'assignments',
        'discussion_topic',
    ],
}

response = requests.get('https://canvas.swansea.ac.uk/api/v1/courses/36847/assignment_groups', params=params, cookies=cookies)

data = response.json()

for i in data:
    for j in i['assignments']:
        print(j['name'])
        print(j['due_at'])







