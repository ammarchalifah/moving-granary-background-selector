# Moving Granary Background Selector
Ammar Chalifah
![Image of Granary](https://github.com/ammarchalifah/moving-granary-background-selector/blob/master/images/banner.jpg)

Simple implementation to generate grayscale background image from a video stream. Implemented using OpenCV library and Python language.
## Introduction
The idea behind this background selector implementation program is interval-based image sampling from a video, storing those sampled image inside a variable (with dimension w x h x d, d denotes the depth or number of images to be stored), and calculating the element-wise mode of intensity without incorporating the extreme 20% highest and 20% lowest value.

The variable used for storing the sampled images is called **granary**. I don't really know whether there is an actual term for this (and I shouldn't name it granary), but I think granary sounds cool and represents the concept perfectly.

Because of the simple implementation, there are some important notes to be considered before using this program:
- It can't automatically detects the length of your video. So please input the total number of frames manually.
- The parameters used depend on the condition of your setup and object characteristics. This program will automatically defines still objects as backgrounds.
- This program is useless in location where there are too many objects that move and almost always cover up the background pixels.

## How to Use
- Clone this respository using HTTPS or SSH protocol.
```
git clone https://github.com/ammarchalifah/moving-granary-background-selector.git
```
```
git clone git@github.com:ammarchalifah/moving-granary-background-selector.git
```
- Install opencv and numpy
```
pip install opencv-python
pip install numpy
```
- Move inside the folder
- Run the program by using
```
python backgroundselector.py -f frame_per_pop -t total_frame_granary -i input_path -l last_frame
```
  - *frame_per_pop*: frame periods for each pop. A pop is a process of loading newest image into the granary and deleting the oldest image in the granary.
  - *total_frame_granary*: the depth of your granary. Use bigger number if you have sufficient computing power and relatively constant background image.
  - *input_path*: path for the video file.
  - *last_frame*: the total number of frames you want to consider.
- Example for running this program
```
python backgroundselector.py -f 24 -t 10 -i sample.mp4 -l 620
```
## FAQs
**I want to specify name and directory of the saved images. How?**
Manually change the source code.

**I want to edit and improve this project. Can I?**
SURE! Just fork it and suggest new changes. :)

## (Possible) Future Updates
- [ ] Integrate this with a webcam/CCTV stream
- [ ] Implement more sophisticated algorithms to detect background with less compututation
- [ ] Able to detect human objects in the stream
