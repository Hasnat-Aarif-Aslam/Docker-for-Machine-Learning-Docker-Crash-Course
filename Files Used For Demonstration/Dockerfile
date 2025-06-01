# base image
FROM python:3.9

# working directory
WORKDIR /simple_flask_app

# copy
COPY . /simple_flask_app

# run
RUN pip install --no-cache-dir -r requirements.txt

# port expose
EXPOSE 5000

# command
CMD ["python", "./app.py"]