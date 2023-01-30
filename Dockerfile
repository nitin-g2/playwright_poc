FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3.9
RUN apt install -y python3-pip

WORKDIR /home/deployer
COPY . .

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    vim \
    git \
    sudo \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' deployer \
    && adduser deployer sudo \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER deployer

RUN sudo pip install -r requirements.txt
RUN sudo playwright install --with-deps chromium

RUN echo "Starting process..."
CMD ["python3", "threaded_pw.py"]
