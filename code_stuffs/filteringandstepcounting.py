import numpy as np
import math
import data_extract_ios as ex
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz, iirnotch, filtfilt, firwin
import sys
import math

def filter_signal(r):
    fs = 100 #sample rate
    nyq = fs/2
    cutoff = 1.25/nyq
    order = 4
    b, a = butter(order, cutoff, btype='low', analog=False)
    filtered_signal = filtfilt(b, a, r)
    windowSize = 10
    meansig = []
    for x in range(0, len(filtered_signal)):
        avgarr = filtered_signal[x:x+windowSize]
        c = np.average(avgarr)
        meansig.append(c)

    peak_locations = []
    peak_baseline =[]
    mean = meansig[0]
    peak = 0
    for j in range(0, len(filtered_signal)-1):
        if(j%windowSize):
            mean=meansig[j]
        if filtered_signal[j] < mean and filtered_signal[j+1]>=mean and not j in peak_locations and not j in peak_locations:
            peak_baseline.append(ts[j])
            peak_locations.append(r[j])
    return peak_baseline, peak_locations

def getSteps(r):
    peak_baseline, peak_locations = filter_signal(r)
    return len(peak_baseline)