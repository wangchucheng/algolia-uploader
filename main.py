import os
import json

from algoliasearch.search_client import SearchClient

client = SearchClient.create(os.environ.get("INPUT_APP_ID"), os.environ.get("INPUT_ADMIN_KEY"))
index_name = os.environ.get("INPUT_INDEX_NAME")
index_file_path = os.environ.get("INPUT_INDEX_FILE_PATH")
languages = os.environ.get("INPUT_INDEX_LANGUAGES").split(",")
github_workspace = os.environ.get("GITHUB_WORKSPACE")


def upload(path, index):
    with open(path) as f:
        records = json.load(f)
        index.save_objects(records, {'autoGenerateObjectIDIfNotExist': True})


default_index = client.init_index(index_name)
upload("{}/{}".format(github_workspace, index_file_path), default_index)
for language in languages:
    i18n_index = client.init_index("{}_{}".format(index_file_path, language))
    upload("{}/{}/{}".format(github_workspace, language, index_file_path), i18n_index)
