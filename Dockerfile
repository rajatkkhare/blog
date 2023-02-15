FROM python:3.8-slim-buster
COPY . /app/blog/
WORKDIR /app/blog/
RUN pip3 install -r requirements.txt
EXPOSE 5000
RUN chmod +x gunicorn_starter.sh
ENTRYPOINT ["./gunicorn_starter.sh"]
