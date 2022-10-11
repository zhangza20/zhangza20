from git import Repo
import os
import sys

repo = Repo(os.getcwd())

if len(repo.untracked_files)!=0:
    print("NEW FILES ARE NOT ALLOW!!!")
    print("These are new files you added: ")
    for file in repo.untracked_files:
        print(f"- {file}")
    exit()

changed = [ item.a_path for item in repo.index.diff(None) ]

ALLOW_CHANGED = ['lint.sh', 'app/checkers/user.py', 'tests/test_basic.py', 'tests/test_api.py', 'test/test_selenium.py', '.flake8'] # noqa: E501

extras = []
for file in changed:
    if file not in ALLOW_CHANGED:
        extras.append(file)

if len(extras)!=0:
    print("MODIFIED FILES NOT IN ALLOW LIST ARE NOT ALLOW!!!")
    print("These are modified files not allowed: ")
    for file in extras:
        print(f"- {file}")
    exit()


if len(sys.argv) != 3:
    print("ILLEGAL ARGUMENTS")
    print("Usage: ")
    print("python zip.py name student_id")
    exit()

name = sys.argv[1]
id = sys.argv[2]

ZIP_PATH = f"{name}_{id}.zip"
if os.path.exists(ZIP_PATH):
    os.remove(ZIP_PATH)

stash = repo.git.stash('create')
if not stash:
    stash = repo.head._HEAD_NAME
with open(ZIP_PATH, 'wb') as f:
    repo.archive(f, treeish=stash)