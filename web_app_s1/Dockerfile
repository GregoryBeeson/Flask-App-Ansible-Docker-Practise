FROM python:3.8.6
WORKDIR /web_app_s1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
ENTRYPOINT ["python", "app.py"]