# Use an official Python runtime as a parent image
FROM python:3.6.8

# Set the working directory to /app
WORKDIR /questionnaire

# Copy the current directory contents into the container at /app
COPY . /questionnaire


