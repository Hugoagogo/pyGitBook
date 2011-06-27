#from git import Repo
#
#repo = Repo("C:\Users\Hugh\Desktop\citySquare")
#
#tags = repo.tags
#tagref = tags[0]
#print tagref.tag                  # tags may have tag objects carrying additional information
#print tagref.commit               # but they always point to commits
#
#
##for x in repo.iter_commits('master', max_count=100):
##    print x.message
##
##print help(git)

#git log --pretty="format:[START commit][author=%an][time=%at][message=%s][hash=%H]" --shortstat > out.txt

import re

data = re.compile(r"\[(\w+=.*?)\]")
changes = re.compile(r"(\d+) files changed, (\d+) insertions[(][+][)], (\d+) deletions")

f = open("out.txt")
r_commits = [x.strip().split("\n") for x in f.read().split("\n[START commit]")]
f.close()

commits = []

class Commit(object):pass

for r_commit in r_commits:
    commit = Commit()
    for item in re.findall(data,r_commit[0]):
        commit.__setattr__(*item.split("=",1))
    if len(r_commit) > 1:
        commit.changed, commit.inserts, commit.deleats = re.search(changes,r_commit[1]).groups()
    else:
        commit.changed = commit.inserts = commit.deleats = "-"
        
    commits.append(commit)
    
print len(commits)