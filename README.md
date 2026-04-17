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
python src/main.py
```

### Sending a Transcript

```bash
curl -X POST http://127.0.0.1:5056/transcription \
     -H "Content-Type: application/json" \
     -d '{"transcription": "This is a test transcription."}'
```

Or if you prefer to use HTTPie:

```bash
http POST 127.0.0.1:5056/transcription "transcription=This is a test transcription."
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

``bash
docker build -t transcriptor .
docker run -p 5056:5056 transcriptor
```

