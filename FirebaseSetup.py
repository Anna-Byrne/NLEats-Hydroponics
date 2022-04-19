#!/usr/bin/env python
########################################################################
# Filename    : SensorReading
# Description : Gets Avgerage Temperature and pH, Also gets Date of reading
# Author      : Anna Byrne
# modification: 2022/04/13
########################################################################

from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import threading


cred = credentials.Certificate("ServiceAccount.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#this will shouldnt be hard coded. But without the tools to fix it it will have to stay like this
UserID=db.collection(u'User').document(u'FrwcSfvnasgUS4TZ7NcRdcTbmiC2')
SysID=db.collection(u'System').document(u'tE1XJmhxfN0YQei3eQTs')


# Add a new doc in collection 'cities' with ID 'LA'(this was a test used to make sure the Pi was behaving with the database as expected)
# db.collection(u'Cities').document(u'LA').set(data)
# db.collection(u'Cities').add(data)