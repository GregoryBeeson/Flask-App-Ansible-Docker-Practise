FROM python:3.7
WORKDIR /logic_s4
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5004
ENTRYPOINT ["python", "app.py"]