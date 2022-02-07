FROM python:3.9-alpine
EXPOSE 8000

WORKDIR /opt/app
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . /opt/app

CMD ["python3", "main.py"]