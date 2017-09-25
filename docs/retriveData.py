from __future__ import print_function
import requests
from common import Common
common = Common()

def retrieve(params):
  result = requests.get(common.select, params)
  print("*"*100)
  print(result.json()[common.response][common.docs])
  print("*"*100)
  print()

# For retreiving all the documents
params = {
  "wt":"json",
  "indent":"on",
  "q":"*:*"
}
retrieve(params)

# For retrieving some docs
params["q"] = "id:001"
retrieve(params)
