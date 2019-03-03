#!/usr/bin/env python

import argparse
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(track):
    fig = plt.figure()
    minimum, maximum = min_max(track)
    for channel in range(track.shape[1]):
        fig.add_subplot(1, track.shape[1], channel+1)
        plt.hist(track[:, channel], range=(minimum[channel], maximum[channel]), bins=512, log=True)
    plt.show()


def plot_diff_histogram(track):
    track_diff = np.diff(track, axis=0)
    plot_histogram(track_diff)


def min_max(track):
    minimum = np.min(track, axis=0)
    maximum = np.max(track, axis=0)
    return minimum, maximum

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="wav file to plot amplitude from")
    return parser.parse_args()


def main():
    args = parse_args()
    rate, data = wavfile.read(args.file)
    plot_diff_histogram(data)
    return True



if __name__ == "__main__":
    exit(not main())
