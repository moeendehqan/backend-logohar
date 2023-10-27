FROM python:3.10.6-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \


WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

# فرمان اجرا
CMD ["python", "run.py"]
