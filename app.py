import os
import numpy as np
import cv2
import math

def readSamples(directory):
  sampleImgs = []
  samplesFiles = os.listdir(directory)
  print(samplesFiles)
  for file in samplesFiles:
    truePath = os.path.abspath(os.path.join(directory, file))
    sampleImg = cv2.imread(truePath)
    sampleImgs.append(sampleImg)
  return sampleImgs


def resizeSamples(samples, mosaicSize):
  for index in range(len(samples)):
    samples[index] = cv2.resize(
      samples[index], mosaicSize, interpolation=cv2.INTER_AREA)