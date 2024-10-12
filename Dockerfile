FROM python:3.12-slim

WORKDIR /backend

COPY /backend /backend

RUN pip3.12 install --no-cache-dir -r requirements.txt

CMD ["python3.12", "main.py"]