# Background selector from video stream
# By: Ammar Chalifah
# 2020/7/17
import cv2
import numpy as np
import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--frame_per_pop', default = 24, help = 'Number of frames passed for each granary pop.')
parser.add_argument('-t','--total_frame_granary', default = 10, help = 'Number of frames stored in granary.')
parser.add_argument('-s', '--save_bool', default = True, help = 'Pass true for saving the background generated in each pop.')
parser.add_argument('-i', '--input_path', default = 'sample.mp4', help ='path to video input. Pass 0 for video stream from webcam.')
parser.add_argument('-l', '--last_frame', default = 600, help = 'last frame of the video stream to be processed')

args = parser.parse_args()

#Pop image to granary.
#Granary is a term I use to refer a variable that stores several images sampled from the video stream.
def pop_granary(image, granary):
  """Granary is an arbitrary word used to conceptualize a data that stores the last 30 second clip of a video.
  The pop granary is used to store the newest image to the graanary, and pop out the last image.

  Args:
    image: grayscale image
    granary: 30 seconds of video clip
  Return
    new granary
  """
  w, h, d = granary.shape
  for i in range(d-1):
      granary[:,:,i] = granary[:,:,i+1]
  image = np.expand_dims(image, axis = 0)
  granary[:,:,d-1]=image
  return granary

#Backrgound Selection
def background_selection(granary):
  """Function to generate backrgound.

  Args:
    granary
  returns: image"""
  w, h, d = granary.shape
  image = np.zeros((w,h), dtype='uint8')
  for i in range(w):
    for j in range(h):
      vals = granary[i,j,:].tolist()
      vals.sort()
      vals = vals[round(d/5):-1*round(d/5)]
      image[i,j] = max(set(vals), key=vals.count)
  return image

frame_per_pop = args.frame_per_pop
total_frame_granary = args.total_frame_granary
last_frame = args.last_frame
save_result = args.save_bool

framecount = 1
start_time = time.time()
video_capture = cv2.VideoCapture(args.input_path)
while video_capture.isOpened():
    success, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if framecount == 1:
        w, h = gray.shape
        granary = np.zeros((w, h, total_frame_granary), dtype='uint8')
    if framecount % frame_per_pop ==0:
        granary = pop_granary(gray, granary)
        print('popping frame {:d} to granary'.format(framecount))
        if framecount/frame_per_pop >= total_frame_granary:
            cv2.imwrite('image-{:d}.jpg'.format(framecount), background_selection(granary))
            cv2.imwrite('original-{:d}.jpg'.format(framecount), frame)
    framecount += 1
    if framecount >= last_frame:
        break
print("--- %s seconds ---" % (time.time() - start_time))

for i in range(granary.shape[2]):
    cv2.imwrite('granary{:d}.jpg'.format(i), granary[:,:,i])