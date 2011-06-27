# Use this is generate log data for the default template
#git log --pretty="format:[START commit][author=%an][time=%at][message=%s][hash=%H]" --shortstat > out.txt

import re, os, datetime
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = os.path.join(os.path.abspath('templates'),"github")

ENV = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

data = re.compile(r"\[(\w+=.*?)\]")
changes = re.compile(r"(\d+) files changed, (\d+) insertions[(][+][)], (\d+) deletions")

def get_css(template):
    css = ""
    for fname in os.listdir(os.path.join(template,"css")):
        fname = os.path.join(template,"css",fname)
        if os.path.isfile(fname):
            f = open(fname)
            css += f.read() + "\n"
            f.close()
    return css

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
        commit.changed, commit.inserts, commit.deletes = re.search(changes,r_commit[1]).groups()
    else:
        commit.changed = commit.inserts = commit.deletes = "-"
    if hasattr(commit,"time"):
        datet = datetime.datetime.fromtimestamp(int(commit.time))
        commit.date = datet.strftime('%d-%m-%Y')
        commit.time = datet.strftime('%I:%M:%S %p')
    commits.append(commit)
    
template = ENV.get_template("main.html")

data = {"commits":commits,
        "title":"This is a test title",
        "style":get_css(TEMPLATE_DIR)}

f = open("out.html","w")
f.write(template.render(data))
f.close()
