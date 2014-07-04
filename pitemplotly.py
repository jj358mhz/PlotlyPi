#!/usr/bin/env python

import plotly.plotly as py # plotly library
from plotly.graph_objs import * # all plotly graph objects
import json # used to parse config.json
import time # timer functions
import datetime
import os # used to acquire internal SoC temperature
import sys

# Initialize some variables with your credentials
with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

username = plotly_user_config['plotly_username']
api_key = plotly_user_config['plotly_api_key']
stream_token = plotly_user_config['plotly_streaming_tokens'][0]

# Initialize a Plotly Object
py.sign_in(username, api_key)

# Initialize your graph (not streaming yet)
data = [Scatter(
    x=[],y=[],
    mode='lines+markers',
    stream={'token': stream_token, 'maxpoints': 1000},
    name='UCBPD')
]
layout = Layout(
    title='Raspberry Pi Temperature',
    xaxis={'autorange': True, 'title': 'Time of Day'},
    yaxis={'autorange': True, 'title': 'Degrees (Celsuis)'}
)
your_graph_url = py.plot(Figure(data=data, layout=layout), filename='Raspberry Pi Temp', auto_open=False)

# Acquire internal SoC temperature
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()

if "error" in line:
    print "Error ... is your firmware up-to-date? Run rpi-update"
else:
   # line now contains something like: temp=41.2'C
   # to get the temperature, split on =, and then on '

    temp = line.split('=')[1].split("'")[0]

# Initialize the Plotly Streaming Object
stream = py.Stream(stream_token)
stream.open()

# Start looping and streaming!
while True:
    stream.write({'x': datetime.datetime.now(), 'y': temp})
    time.sleep(1) # delay between stream posts