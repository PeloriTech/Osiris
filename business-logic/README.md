# Osiris Server

This is where the Osiris Server code will live.

Osiris applies object detection to n-number of streams.

If n streams are incoming, then n streams are outputted.

There is a json output of what Osiris is seeing.



Video In ------- classification -------- Video Out                                
    + + + + + + + +                      L_______________ Json Stream Out

- video in
    - rtsp url
- classification
- video out
    - tcp sink
- json out
    - websocket

## Setup

### Ubuntu 18.04

In the osiris subfolder, run `sh setup_ubuntu_18.04.sh`

This will:

- Install all necessary apt packages.
- Setup a python virtual environment (python3.6).
- Install all necessary pip modules.
- Build opencv from source with gstreamer support.
- Make database migrations.
- Migrate database.

If you ever need to migrate the database run the following commands:

`python manage.py makemigrations osiris_server`

`python manage.py migrate`

## Run

To run the server, first open the virtual environment:

`cd osiris/`

`source venv/bin/activate`

`python manage.py runserver 0.0.0.0:8000`

## Architecture

This server follows model-view-controller format.

We also employ Data Access Object (DAO) structure.

## Pipelines

#### Viewing udp output 

gst-launch-1.0 -v udpsrc port=5000 caps = "application/x-rtp, media=(string)video, encoding-name=(string)H264" ! rtph264depay ! decodebin ! videoconvert ! autovideosink


## Pipelines

#### Viewing udp output 

gst-launch-1.0 -v udpsrc port=5000 caps = "application/x-rtp, media=(string)video, encoding-name=(string)H264" ! rtph264depay ! decodebin ! videoconvert ! autovideosink


### Database Design

![database design](https://gitlab.com/peloritech/osiris/raw/master/osiris-server/Osiris-Database.png)