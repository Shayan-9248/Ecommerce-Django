FROM python:3.9

LABEL maintainer='shayan.aimoradii@gmail.com'

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src/
COPY . /src/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]