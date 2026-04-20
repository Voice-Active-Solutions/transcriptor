# transcriptor

A simple web application for ASR callbacks. It accepts a transcription and writes it to a file in a bucket.

See the [IBM Cloud Docs](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-async) for more details on how to use a callback URL.

## Setup

Assumes that you'll be using a virtual environment.

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Trying it Out

### Starting the web application

```bash
python src/app.py
```

### Sending a Transcript

```bash
curl -X POST http://127.0.0.1:8080/transcription \
     -H "Content-Type: application/json" \
     -d '{"transcription": "This is a test transcription."}'
```

Or if you prefer to use HTTPie:

```bash
http POST 127.0.0.1:8080/transcription "transcription=This is a test transcription."
```

You should see the following response:

```json
{
  "length": 29,
  "message": "Transcription received successfully"
}
```

## Build the container image

You can then build the web service as a container image using the Dockerfile:

```bash
docker build -t transcriptor .
docker run -p 8080:8080 transcriptor
```

## Deploy as a Code Engine Application

You can deploy directly from the GitHub repo to IBM Code Engine like this:

```bash
ibmcloud ce application create --name transcriptor \
    --build-source https://github.com/Voice-Active-Solutions/transcriptor.git \
    --build-strategy buildpacks --build-context-dir /src/ \
    --cpu 0.25 --memory 1G --max-scale 4 --concurrency 6 \
    --port 8080
```

