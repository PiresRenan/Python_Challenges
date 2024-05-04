FROM python:3.12

RUN apt-get update && apt-get install -y postgresql postgresql-contrib

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["./start.sh"]
