from __future__ import print_function
import requests
from common import Common
common = Common()

def update(url, xmlFile, params, headers):
  data = open(xmlFile, "rb").read()
  res = requests.post(url, data=data, params=params, headers=headers)
  print("*"*100)
  print("Status %s"%res.text)
  print("*"*100)
  print()

params = {
  "commit":"true"
}
# updating all the documents
#update(common.update, "data/update-all.xml", params, common.headers["xml"])

# updating single document
update(common.update, "data/update-one.xml", params, common.headers["xml"])