import requests
import sys

sub_list = open("wordlist.txt").read()
directories = sub_list.splitlinen()

for dir in directories:
  dir_enim = f"http://{sys.argv[1]}/{dir}.html"
  r = request.get(dir_enum)
  if r.status_code==404:
    pass
  else:
    print("Valid directory:" ,dir_enum)
