# transcriptor
A simple web application for ASR callbacks. It accepts a transcription and writes it to a file in a bucket.

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

You should see the following response:

```json
{
  "length": 29,
  "message": "Transcription received successfully"
}
```