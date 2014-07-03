#!/usr/bin/env python
import plotly
import plotly.plotly as py
import os


def update_temp(date,temp):
        py = plotly.plotly(username_or_email='jj358mhz', key='mqth4b4nqe')
        r =  py.plot(date,temp,
        filename='RPiTempCont2',
        fileopt='extend',
        layout={'title': 'Raspberry Pi 2 Temperature Status'})

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        date = sys.argv[1]
        temp = sys.argv[2]
        update_temp(date,temp)
    else:
        print 'Usage: ' + sys.argv[0] + ' date temp'