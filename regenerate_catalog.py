import os
import subprocess

process = subprocess.Popen(["git", "diff", "--name-only", os.environ['TRAVIS_COMMIT_RANGE']], stdout=subprocess.PIPE)
files = process.communicate()[0].decode("utf-8")

# Check if changes were made to code.json
if 'code.json' in files.split():
	print("REGENERATING CATALOG.JSON")
else:
	print("NO CODE.JSON DIFFS")



