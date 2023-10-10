FROM python:3.11-bookworm

RUN apt-get update && apt-get install -yq ocrmypdf && apt-get install tesseract-ocr-rus

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade --no-cache-dir -r requirements.txt

COPY ./ocr_files /ocr_files
COPY ./src /src
COPY ./main.py /main.py

# clean
RUN apt-get clean all \
  && rm -rf /var/lib/apt/lists/*

CMD ["python3","-u","main.py"]


