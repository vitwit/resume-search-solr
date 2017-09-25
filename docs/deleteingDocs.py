from __future__ import print_function
import requests
from common import Common
common = Common()

def delete(url, xmlFile, params, headers):
  data = open(xmlFile, "rb").read()
  res = requests.post(url, data=data, params=params, headers=headers)
  print("*"*100)
  print("Status %s"%res.text)
  print("*"*100)
  print()

params = {
  "commit":"true"
}

# deleting some documents

delete(common.delete, "data/delete.xml", params, common.headers["xml"])

# deleting all the documents

delete(common.delete, "data/delete-all.xml", params, common.headers["xml"])

