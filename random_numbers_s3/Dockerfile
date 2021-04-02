FROM python:3.7
WORKDIR /random_numbers_s3
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5003
ENTRYPOINT ["python", "app.py"]