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

#course_path = "courses/36829"
course_path = []
course_info = []
data = []

# Take all the course paths and put them into a list
with open('course_info.json', 'r') as f:
    course_info = json.load(f)
    f.close()

for i in course_info:
    course_path.append(i['course_path'])

#print(course_path)
#for i in course_path:
#    response = requests.get(f'https://canvas.swansea.ac.uk/api/v1/{i}/assignment_groups', cookies=cookies)
#    data.append({
#        # Change to json(), the text isn't very good
#        f'assignments-{i}': response.text
#    })


with open('course_assignments.json', 'w') as f:
     json.dump(data, f, indent=4)
     f.close()


requests.Session()
