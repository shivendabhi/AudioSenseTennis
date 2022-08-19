#!/usr/bin/env python3


#This is Shiven Dabhi's submission for the iDTech AI and Machine Learning Summer Class
#This program here will detect and track a tennis ball that is shown in the camera frame.
#The purpose of the program is so that it can be used to track tennis balls on a tennis court.
#This makes the balls on the screen more visible to people with visual impairment.
#With this, more people will be able to watch live tennis without having to wait for the match recording to be processed with ball highlighted after the match has finished

#ATTN: Do note that this code is not meant to be run while not in headless modeby default, as there will be no display window that will be shown.
#ATTN: It is possible to specify where to save the video file using the CLI arguments, so it can be run in headless mode if necessary

import sys
import argparse
import jetson.utils
import jetson.inference

#parses the command line
parser = argparse.ArgumentParser()
parser.add_argument("--input_location", type=str, default="/dev/video0", help="Location of the camera/video file(The default is the USB camera)")
parser.add_argument("--output_location", type=str, default="display://0", help="Location of the output(my_video.mp4 for a file output)")


#exits if there are any issues with the arguments
try:
	args=parser.parse_args()
except:
	print("")
	parser.print_help()
	sys.exit(0)

#gets and assigns the arguments from the CLI
net = jetson.inference.detectNet(argv=["--model=tennis-ball_model.onnx", "--labels=labels.txt", "--input_blob=input_0", "--output-cvg=scores", "--output-bbox=boxes"], threshold=0.3)
camera  = jetson.utils.videoSource(args.input_location)
display = jetson.utils.videoOutput(args.output_location)

while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

