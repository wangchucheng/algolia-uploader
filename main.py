import os
import json

from algoliasearch.search_client import SearchClient

client = SearchClient.create(os.environ.get("INPUT_APP_ID"), os.environ.get("INPUT_ADMIN_KEY"))
index = client.init_index(os.environ.get("INPUT_INDEX_NAME"))
path = "{}/{}".format(os.environ.get("GITHUB_WORKSPACE"), os.environ.get("INPUT_INDEX_FILE_PATH"))

with open(path) as f:
    records = json.load(f)
    index.save_objects(records,  {'autoGenerateObjectIDIfNotExist': True})
