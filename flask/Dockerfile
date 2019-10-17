FROM python:3.7

ADD . /

WORKDIR /

RUN pip install -r requirements.txt 

ENV FLASK_APP=geo.py
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=development

#ENTRYPOINT ["python3"]
#CMD ["geo.py"]
CMD ["flask", "run"]