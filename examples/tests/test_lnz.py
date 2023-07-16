import requests
import json
from pprint import pprint

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
#  Question 1
json_data = {"input": "what's the cube root of 625"}

response = requests.post(
    "http://127.0.0.1:8000/examples.lnz:agent/run", headers=headers, json=json_data
)

decoded_content = response.content.decode("utf-8")
dc = json.loads(decoded_content)
pprint(dc)

"""

❯ python3.10 examples/tests/test_ex7.py


"""
