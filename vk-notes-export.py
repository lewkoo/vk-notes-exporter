# -*- coding: utf-8 -*-

import codecs
import ConfigParser
import datetime
import json
import sys
import urllib2
from urllib import urlencode

import vk_auth

def _api(method, params, token):
    params.append(("access_token", token))
    url = "https://api.vk.com/method/%s?%s" % (method, urlencode(params))
    return json.loads(urllib2.urlopen(url).read())["response"]

# read config values

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

login = Config.get("auth", "username")
password = Config.get("auth", "password")
app_id = Config.get("application", "app_id")

# auth to get token

try:
    token, user_id = vk_auth.auth(login, password, app_id, 'notes')
except RuntimeError:
    sys.exit("Incorrect login/password. Please check it.")

sys.stdout.write('Authorized vk\n')

# get the list of notes

notes = _api("notes.get", [("count", "100")], token)

print len(notes)
print notes[0]
