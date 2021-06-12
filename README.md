# Algolia Uploader

![build](https://github.com/wangchucheng/algolia-uploader/workflows/build/badge.svg)
![license](https://img.shields.io/github/license/wangchucheng/algolia-uploader)

Algolia Uploader enables you to upload your algolia index file automatically.

## Try Algolia Uploader

You can use the following example as a template to create a new file with any name under `.github/workflows/`.

```yaml
name: <action_name>

on: 
  - push

jobs:
  upload_algolia_index:
    runs-on: ubuntu-latest
    name: Upload Algolia Index
    steps:
    - uses: actions/checkout@v2
      with:
        fetch-depth: 0
    - uses: wangchucheng/algolia-uploader@master
      with:
        # Such as `Z0U0ACGBN8`
        app_id: <your_app_id>
        # You can store token in your project's 'Setting > Secrets' and reference the name here. Such as ${{ secrets.ALGOLIA_ADMIN_KEY }}
        admin_key: <your_admin_key>
        # The index name. 
        index_name: <your_index_name>
        # The index file path relative to repo root.
        index_file_path: <your_index_file_path>
```
