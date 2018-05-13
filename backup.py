import requests
import json
import os, sys

user = str()
oauth_key = str()
oauth_sec = str()

if os.path.isfile('backup.conf'):
    with open('backup.conf') as conf:
        conf = [c.strip() for c in conf.readlines()]

    for c in conf:
        c = c.replace(' ', '')
        if c.startswith('user='):
            user = "".join(c.split('=')[1:])
        if c.startswith('oauth_key='):
            oauth_key = "".join(c.split('=')[1:])
        if c.startswith('oauth_sec='):
            oauth_sec = "".join(c.split('=')[1:])

if not user:
    print('ERROR: user not defined')
if not oauth_key:
    print('ERROR: oauth key not defined')
if not oauth_sec:
    print('ERROR: oauth secret key not defined')
if not user or not oauth_key or not oauth_sec:
    sys.exit(1)
else:
    print('user =', user)
    print('oauth_key =', oauth_key)
    print('oauth_sec =', oauth_sec)

likes = f"http://api.tumblr.com/v2/blog/{user}.tumblr.com/likes?api_key={oauth_key}"
likes = requests.get(likes)
likes = json.loads(likes.text)

print(likes['meta']['status'], likes['meta']['msg'])
