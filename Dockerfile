FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY ./backend /code/

COPY ./requirements.txt/ /code/
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt
# CMD [ start server here ]
