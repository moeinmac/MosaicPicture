import os
import numpy as np
import cv2
import math

def readSamples(directory):
  sampleImgs = []
  samplesFiles = os.listdir(directory)
  for file in samplesFiles:
    truePath = os.path.abspath(os.path.join(directory, file))
    sampleImg = cv2.imread(truePath)
    sampleImgs.append(sampleImg)
  return sampleImgs


def resizeSamples(samples, mosaicSize):
  for index in range(len(samples)):
    samples[index] = cv2.resize(
      samples[index], mosaicSize, interpolation=cv2.INTER_AREA)
    
def avgRGB(image):
  (h, w, d) = image.shape
  image = np.array(image)
  image = image.reshape((h*w, d))
  return np.average(image, axis=0)


def cropImage(image, mosaicSize, mosaicCount):
  h, w = mosaicSize
  row, col = mosaicCount
  croppedImgs = []
  for j in range(col):
    for i in range(row):
      croppedImgs.append(image[i * w: (i + 1) * w, j * h: (j + 1) * h])
  return (croppedImgs)

def getBestMatch(imgAvg, samplesAvg):
  sampleDists = []
  for sAVG in samplesAvg:
    dist = math.dist(imgAvg, sAVG)
    sampleDists.append(dist)

  minDist = np.min(sampleDists)
  return sampleDists.index(minDist)

def createMosaicImg(mosaicImgs, mosaicSize,mosaicCount):
  h, w = mosaicSize
  row, col = mosaicCount
  blankImg = np.zeros((row*h, col*w, 3), np.uint8)
  index = 0
  for j in range(col):
    for i in range(row):
      blankImg[i * w: (i + 1) * w, j * h: (j + 1) * h] = mosaicImgs[index]
      index +=1
  return blankImg


mainImage = cv2.imread("main.jpg")

sampleImgs = readSamples("samples")

mosaicSize = (10, 10)
mosaicCount = (
    int(mainImage.shape[0] / mosaicSize[0]), int(mainImage.shape[1] / mosaicSize[1]))



resizeMainImage = (mosaicCount[1]*mosaicSize[1], mosaicCount[0]*mosaicSize[0])
mainImage = cv2.resize(mainImage, resizeMainImage,interpolation=cv2.INTER_AREA)



resizeSamples(sampleImgs, mosaicSize)

avgSamples = []
for sample in sampleImgs:
  avgSamples.append(avgRGB(sample))

croppedImages = cropImage(mainImage, mosaicSize, mosaicCount)

print("Start Processing Image...")
mosaicImages = []
for img in croppedImages:
  index = getBestMatch(avgRGB(img), avgSamples)
  mosaicImages.append(sampleImgs[index])

finalImage = createMosaicImg(mosaicImages,mosaicSize,mosaicCount)
print("Image Processing is finished.")

cv2.imwrite('final.jpg', finalImage)

cv2.imshow("Main Image", mainImage)
cv2.imshow("Final Image", finalImage)
cv2.waitKey(0)
cv2.destroyAllWindows()