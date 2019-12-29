#!/usr/bin/env bash

gst-launch-1.0 rtspsrc latency=0 location=  ! queue ! application/x-rtp,encoding-name=H264,payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink
