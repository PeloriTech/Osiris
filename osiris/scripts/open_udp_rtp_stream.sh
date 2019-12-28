#!/usr/bin/env bash

gst-launch-1.0 -v udpsrc port=5000 caps = "application/x-rtp, media=(string)video, encoding-name=(string)H264" ! rtph264depay ! decodebin ! videoconvert ! autovideosink