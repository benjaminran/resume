FROM ubuntu:latest
MAINTAINER Benjamin Ran <benjaminran2@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q
RUN apt-get install -qy texlive-full 
