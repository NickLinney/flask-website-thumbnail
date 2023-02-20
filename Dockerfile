FROM ubuntu:20.04

# Create ENV variable to fix tzdata region selection during 'docker build' command.
ENV TZ=Asia/Dubai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Update apt-get
RUN apt-get update

# Install Python 3 and pip
RUN apt-get install -y python3 python3-pip

# Install Selenium dependencies
RUN apt-get install -y \
  firefox \
  chromium-browser \
  unzip \
  wget \
  libglib2.0-0 \
  libnss3 \
  libgconf-2-4 \
  libfontconfig1 \
  xvfb

# Install geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -xzf geckodriver-v0.30.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-v0.30.0-linux64.tar.gz

# Install chromedriver
RUN wget https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    rm chromedriver_linux64.zip

# Set display environment variable
ENV DISPLAY=:99

# Copy the application files
COPY . /app

# Set the working directory
WORKDIR /app

# Install the application dependencies
RUN pip3 install -r requirements.txt

# Run the application
CMD [ "python3", "app.py" ]
