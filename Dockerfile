FROM python:3

LABEL org.opencontainers.image.authors="james@voiceactivesolutions.co.uk"
LABEL org.opencontainers.image.vendor="Voice Active Solutions Ltd."
LABEL org.opencontainers.image.description="Transcriptor web service to write an audio transcription to storage as a text file."
LABEL org.opencontainers.image.version="1.0.0"

RUN mkdir -p /usr/app/logs
WORKDIR /usr/app

COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/main.py ./

EXPOSE 5056

CMD ["python", "main.py"]