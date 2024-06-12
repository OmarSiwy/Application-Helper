#!/bin/bash

docker build -t ResumeBuilder .

docker run -it --rm --name RunningResumeBuilder ResumeBuilder
