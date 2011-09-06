#!/usr/bin/env python

from pprint import pprint
from urllib import urlretrieve
import imp

urlretrieve('https://raw.github.com/gist/1194123/fbconsole.py', '.fbconsole.py')
fb = imp.load_source('fb', '.fbconsole.py')

fb.AUTH_SCOPE = ['publish_stream']
fb.authenticate()

# Post a status update
# status = fb.graph_post("/me/feed", {"message":"Hello from my awesome script"})

# Fetch likes on a status update
# likes = fb.graph("/"+status["id"]+"/likes")

# Delete a status update
# fb.graph_delete("/"+status["id"])

# Upload a photo
# fb.graph_post("/me/photos", {"message":"My photo", "source":open("my-photo.jpg")})

# Query FQL tables
friends = fb.fql("SELECT name FROM user WHERE uid IN "
                 "(SELECT uid2 FROM friend WHERE uid1 = me())")

pprint(friends)
