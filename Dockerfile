
FROM python:3

WORKDIR /app
COPY . /app

ENV HOST=rabbit_web
ENV PORT=5672

RUN pip install -r requirements.txt

CMD ./wait-for-it.sh $HOST:$PORT -t 25 -- python main.py
