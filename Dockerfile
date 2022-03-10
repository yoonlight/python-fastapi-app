FROM python:alpine3.14

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "80"]