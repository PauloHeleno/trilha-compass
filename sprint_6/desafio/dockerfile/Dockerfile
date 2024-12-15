FROM python:3.9

WORKDIR /app

RUN pip install boto3

COPY script_desafio.py /app/

VOLUME ["/app/csv"]

CMD ["python", "script_desafio.py"]


