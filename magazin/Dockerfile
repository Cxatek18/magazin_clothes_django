# pull official base image
FROM python:3.9


# set work directory
WORKDIR /usr/src/magazin
ADD . /usr/src/magazin

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /usr/src/magazin/docker-entrypoint.sh

COPY . /usr/src/magazin

ENTRYPOINT ["/usr/src/magazin/docker-entrypoint.sh"]