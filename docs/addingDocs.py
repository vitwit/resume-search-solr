from __future__ import print_function
import requests
from common import Common
common = Common()

def add(url, xmlFile, params, headers):
  data = open(xmlFile, "rb").read()
  res = requests.post(url, data=data, params=params, headers=headers)
  print("*"*100)
  print("Status %s"%res.text)
  print("*"*100)
  print()

# Adding some
params = {
  "commit":"true"
}

add(common.add, "data/people.xml", params, common.headers["xml"])
