from github import Github
import os

token = os.getenv('GH_TOKEN', '...')
# print(f"token {token}")
print("Starting ...")
g = Github(token, timeout=10, retry=3, per_page=100)
org = "pagopa"
members = g.get_organization(org).get_members()
members_set = {m.login for m in members}
# print(members_set)  

skipped = set(('io-app','io-backend','interop-be-purpose-process'))

did_something_set = set() # empty
repos = g.get_organization(org).get_repos('all')
index=0
for repo in repos:
    index+=1
    print(f"{index}) {repo.name}")
    if repo.name not in skipped :
        actor_events_on_repo = { event.actor.login for event in g.get_organization(org).get_repo(repo.name).get_issues_events() if event.actor is not None}
        print(actor_events_on_repo if len(actor_events_on_repo) > 0 else ">>>>>>>>>>>>>>>>>>>>>> NO events within the past 90 days")
        did_something_set = did_something_set| (members_set & actor_events_on_repo)
    else:
        print("Skipped")

# people who do not contribute 90 days
members_set.difference_update(did_something_set)
print(members_set)
print(len(members_set))
    

# io-
# pagopa-
# pn-
# pdnd-
# idpay-
# cstar-
# iterop-
# bpd-
# selfcare-
# ....

