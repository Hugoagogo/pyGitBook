pyGitBook
========

gitBookLog is a simple and slightly hackish program that can be used to turn a dump from git-log into a nice logbook

## Usage
Requirements: Python3
1. cd into your repository folder inside a terminal
2. Run `git log --pretty="format:[START commit][author=%an][time=%at][message=%s][hash=%H]" --shortstat > git-data.txt` for creating a git-data.txt file with your commit history
3. Put your created `git-data.txt` file into the repository folder and run `python main.py` inside of it