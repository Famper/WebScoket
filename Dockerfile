FROM python:3.12-slim

WORKDIR /python-server

COPY /backend /python-server

RUN pip3.12 install --no-cache-dir -r requirements.txt

CMD ["python3.12", "main.py"]