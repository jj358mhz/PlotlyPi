#!/usr/bin/env python

import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects
import json # used to parse config.json
import time # timer functions
import datetime

# Initialize some variables with your credentials
with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

username = plotly_user_config['plotly_username']
api_key = plotly_user_config['plotly_api_key']
stream_token = plotly_user_config['plotly_streaming_tokens'][0]

# Initialize a Plotly Object
py.sign_in(username, api_key)

# Initialize your graph (not streaming yet)
data = [Scatter(x=[],y=[],stream={'token': stream_token, 'maxpoints': 1000})]
layout = Layout(
    title='UCBPD RaspberryPi Temperature',
    xaxis={'title': 'Time of Day'},
    yaxis={'title': 'Degrees (Celsuis)'}
)
your_graph_url = py.plot(Figure(data=data, layout=layout), filename='RaspberryPi 2 Temp', auto_open=False)

import os

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()

if "error" in line:
   print "Error ... is your firmware up-to-date? Run rpi-update"
else:
   # line now contains something like: temp=41.2'C
   # to get the temperature, split on =, and then on '

   temp = line.split('=')[1].split("'")[0]
   print temp

# Initialize the Plotly Streaming Object
stream = py.Stream(stream_token)
stream.open()

# Start looping and streaming!
while True:
    stream.write({'x': datetime.datetime.now(), 'y': temp})
    time.sleep(5) # delay between stream posts
