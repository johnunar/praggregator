FROM python:3
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=praggregator.local_settings
ENV AL_BASE_URL=https://applifting-python-excercise-ms.herokuapp.com/api/v1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/