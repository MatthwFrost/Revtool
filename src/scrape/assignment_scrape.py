import requests
import json

cookies = {
    '_legacy_normandy_session': 'dqTSENhlhxmu1-A1-PWgeQ+Ghc0ePlemYVRnzSE4z-UYQDBYJAp54G2d4Sgn15QxfDi0W3dWOuuyZYAOwMw25MFDV_RzeGbDqU2szVwQ5nXA_rKd-a3uOL1DRf27XTH6RCv4-lGrKc3xah-Jv5I1oosmzsmXHkdUh4Pvn0HP4Ethy0uW0MY23EPwBcJmx3DbIZUAFetn-uEsGluv_kCSj2vfg5Vqpp3n2zXxcSUtMD3yLErIqXblkaxga5C2qzqcJCbVOzShQK1al16wyWDC5gQyJzdFMoTvWsEP7BZ3TRaZO7wX9JPIhZXbAGtA2Mxgn8qLLjQFcix4sWQfObrhTGFuuvjVwP52-AawALABJkCLlYYaUsr00ABOPQ33uU1V8gvjKM3XrwIRXhmIaSU9cy-xXYzic5qEe6gAzVl6FvlRRDATjME5qyGDndpoOu-HXpMFZ3CWWpOUCC-YkgeP1qgZ-CdzebceLVeJxotLSrST5xk3rPFGKxVX81oOSRCNID0p-HloVEsFJsb6lZzEy08qmOdwLBIw1mQYg3c2cY7BA37QzGc0Qj9W79Yg4RJ4kGrKpvJTm3z3EzPZaGk4uD8.jj1nyjzyuEKZvpkimZDAqoXSPr4.Y31Unw',
    'canvas_session': 'dqTSENhlhxmu1-A1-PWgeQ+Ghc0ePlemYVRnzSE4z-UYQDBYJAp54G2d4Sgn15QxfDi0W3dWOuuyZYAOwMw25MFDV_RzeGbDqU2szVwQ5nXA_rKd-a3uOL1DRf27XTH6RCv4-lGrKc3xah-Jv5I1oosmzsmXHkdUh4Pvn0HP4Ethy0uW0MY23EPwBcJmx3DbIZUAFetn-uEsGluv_kCSj2vfg5Vqpp3n2zXxcSUtMD3yLErIqXblkaxga5C2qzqcJCbVOzShQK1al16wyWDC5gQyJzdFMoTvWsEP7BZ3TRaZO7wX9JPIhZXbAGtA2Mxgn8qLLjQFcix4sWQfObrhTGFuuvjVwP52-AawALABJkCLlYYaUsr00ABOPQ33uU1V8gvjKM3XrwIRXhmIaSU9cy-xXYzic5qEe6gAzVl6FvlRRDATjME5qyGDndpoOu-HXpMFZ3CWWpOUCC-YkgeP1qgZ-CdzebceLVeJxotLSrST5xk3rPFGKxVX81oOSRCNID0p-HloVEsFJsb6lZzEy08qmOdwLBIw1mQYg3c2cY7BA37QzGc0Qj9W79Yg4RJ4kGrKpvJTm3z3EzPZaGk4uD8.jj1nyjzyuEKZvpkimZDAqoXSPr4.Y31Unw',
    '_csrf_token': 'sXuKloGd%2F9uA2OevwCG9CaQijS0VACQGnThVPjHsddDYFaXX1ezUstbq0vWTFMgi%2FBvkalRad2TsXzFweK1B6Q%3D%3D',
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







