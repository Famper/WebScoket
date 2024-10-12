FROM python:3.12

COPY ./backend /python-server

WORKDIR /python-server

RUN pip3.12 install -r requirements.txt

CMD ["python3.12", "main.py"]