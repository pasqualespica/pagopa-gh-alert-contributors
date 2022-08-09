# pagopa-gh-alert-contributors

- [pagopa-gh-alert-contributors](#pagopa-gh-alert-contributors)
  - [Github API docs](#github-api-docs)
  - [Run script](#run-script)

## Github API docs

[GH REST api](https://docs.github.com/en/rest)

[The Events API is a read-only API to the GitHub events.](https://docs.github.com/en/rest/activity/events)

[PyGithub api](https://pygithub.readthedocs.io/en/latest/apis.html)


## Run script
```sh
python -m venv gh-stats-venv
. gh-stats-venv/bin/activate
pip install -r requirements.txt
time GH_TOKEN=<YOUR_TOKEN> python repos_details.py
```
> NOTE : to update requirements dependecy typing `pip freeze > requirements.txt`