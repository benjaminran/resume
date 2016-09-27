FROM blang/latex
MAINTAINER Benjamin Ran <benjaminran2@gmail.com>

RUN apt-get update \
 && apt-get install -y git \
 && apt-get install -y python3-pip \
 && pip3 install Jinja2

#ADD bin /resume/bin
ADD . /resume
#ADD content /resume/content
#ADD lib /resume/lib
#ADD templates /resume/templates
#RUN mkdir /resume/output

ENV PATH /resume/bin:/resume/lib:$PATH
ENV PYTHONPATH /resume/lib:$PATH

WORKDIR /resume
