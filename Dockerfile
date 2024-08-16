# Use Python 3.12 Slim Bookworm as base image
FROM python:3.12-slim-bookworm

# Set username, home path and venv path
ARG USERNAME=app
ARG HOME=/home/$USERNAME
ARG VENV_PATH=$HOME/venv

ENV FLASK_APP=$USERNAME.wsgi:application

# Install Git for Setuptools SCM to figure out version
RUN apt update
RUN apt install -y git

# Create a new user and group called 'user'
RUN groupadd -r $USERNAME
RUN useradd -r -g $USERNAME -m -d $HOME $USERNAME

# Set the working directory to the app location and change ownership
WORKDIR $HOME/app
RUN chown -R $USERNAME:$USERNAME $HOME/app

# Switch to the new user
USER $USERNAME

# Set up a virtual environment and activate it
RUN python3 -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Copy the application code and install dependencies
COPY --chown=$USERNAME:$USERNAME . .
RUN pip install -e ".[deployment]"
