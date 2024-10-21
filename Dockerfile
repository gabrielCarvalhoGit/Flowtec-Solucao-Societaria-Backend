FROM python:3.12.2-slim

WORKDIR /flowtech-solucao-societaria

COPY requirements.txt requirements.txt 

RUN apt-get update && apt-get install --no-install-recommends -y gcc libpq-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]