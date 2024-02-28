FROM python:3.12-slim-bullseye

LABEL maintainer="Amogh Madan <amoghmadaan@gmail.com>"

WORKDIR /app

COPY . .

RUN pip install .[production]

CMD [ "gunicorn", "wsgi:application", "-b=0.0.0.0:8000", "--chdir=/app/src", "-w=4", "-t=10" ]
