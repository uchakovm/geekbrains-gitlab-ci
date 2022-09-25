# run gitlab-ci
# python stop_pipelines.py $API_TOKEN $CI_PROJECT_ID $REF_NAME

# example:
# image: "python:3.7"
# before_script:
#   - python --version
#   - python -m pip install requests
# pytest:
#   stage: test
#   script:
#   - python stop_pipelines.py $API_TOKEN $CI_PROJECT_ID stage

import requests
import sys

url = f"https://gitlab.com/api/v4/projects/{sys.argv[2]}/pipelines"
headers = {"PRIVATE-TOKEN" : sys.argv[1] }
r = requests.get(url, headers=headers)

import json

if(r.status_code == 200):
    for a in json.loads(r.text):
        if (a['ref'] == f"{sys.argv[3]}"):
            url = f"https://gitlab.com/api/v4/projects/{sys.argv[2]}/pipelines/{a['id']}/cancel"
            r = requests.post(url, headers=headers)
            if(r.status_code == 200):
                print(f"{a['id']} is stopped")
