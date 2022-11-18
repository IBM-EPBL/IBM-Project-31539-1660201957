FROM python

WORKDIR /myapp
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /myapp

EXPOSE 5000

ENTRYPOINT ["python3","app.py"]

