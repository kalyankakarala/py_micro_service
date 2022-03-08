FROM ubuntu:bionic

RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        software-properties-common \
    && add-apt-repository -y ppa:deadsnakes \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3.8-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && :

RUN apt-get update
RUN apt-get install -y python3.8-dev
RUN apt-get install -y ffmpeg
RUN apt-get install -y iputils-ping

RUN python3.8 -m venv /venv
ENV PATH=/venv/bin:$PATH

COPY . /py_ms_demo
WORKDIR /py_ms_demo

RUN pip install -r requirements.txt

ENV APP_VERSION=1.0.1
EXPOSE 8055
ENV FLASK_APP=main_app.py
CMD [ "python3", "./main_app.py" ]
