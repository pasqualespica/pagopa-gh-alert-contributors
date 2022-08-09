# GH_TOKEN=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 python repos.py
import re
from github import Github
import os
# from pprint import pprint

token = os.getenv('GH_TOKEN', '...')
# print(f"token {token}")
print("Starting ...")
g = Github(token,timeout=10,retry=3)
org="pagopa"
no_commits=1
ext_contributors = set(('MassimoScattarella', 'furlaniilaria'))
excluded_repos = set(('','pagopa/io-ops','pagopa/testccas'))


repos = g.get_organization(org).get_repos('all')
members = g.get_organization(org).get_members()

members_set = {m.login for m in members}
print(f"PagoPA orgs members count {len(members_set)}")    
# print(members_set)    
did_something_set = set() # empty


count_prj = 0
for p in repos:
    count_prj+=1
    print(f"{count_prj}) Workin on {p.full_name}", end="\n")    
    if p.full_name not in excluded_repos:
        contributors = g.get_repo(p.full_name, True).get_stats_contributors()        
        if contributors is not None:
            contributors.sort(key=lambda x: x.total,reverse=True)
            filtered = filter(lambda c: c.total >= no_commits, contributors)
            contributor_set = {f.author.login for f in filtered}
            # print(f"ext_coll {len(ext_contributors & contributor_set)}")
            did_something_set = did_something_set| (members_set & contributor_set)
            print(f"contributors {len(contributor_set)} did_something_set {len(did_something_set)}")
        else : 
            print(">>> NO contributors <<<")
    else : 
        print(" ### SKIPPED ### ")

            
    # break
    
members_set.difference_update(did_something_set)
print(members_set)
print(len(members_set))
    