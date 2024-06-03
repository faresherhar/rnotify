FROM docker.io/python:3.12.3-alpine3.19

EXPOSE 8080

# Install TINI
RUN apk add --no-cache tini

# Configure user & directory
WORKDIR /home/rnotify
RUN adduser --disabled-password rnotify && \
    chown rnotify /home/rnotify

# Copy code
COPY ./requirements/common.txt ./requirements.txt
COPY ./src ./

# Install PIP packages
RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Run as non-root
USER rnotify

ENTRYPOINT ["/sbin/tini", "--"]
