#!/usr/bin/env python

import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects
import json # used to parse config.json
import time # timer functions
import readadc # helper functions to read ADC from the Raspberry Pi
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
layout = Layout(title='Live graphing from a Raspberry Pi')
your_graph_url = py.plot(Figure(data=data, layout=layout), filename='Raspi Graph', auto_open=False)

# Specify the connected channel for your sensor
# sensor_pin = 0

# Initialize the GPIO
# readadc.initialize()

# Initialize the Plotly Streaming Object
stream = py.Stream(stream_token)
stream.open()

# Start looping and streamin'!
while True:
    #sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, $
    stream.write({'x': datetime.datetime.now(), 'y': sensor_data})
    time.sleep(0.1) # delay between stream posts