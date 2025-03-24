# Coqui

This repository is to checkout how the Coqui TTS service can be run on local systems. 

Please clone this repo
```bash
git clone https://github.com/Sudeshna-Merugu/I3.git
cd I3
```

Create and activate a virtual environment
```bash
python3 -m venv tts-venv
source tts-venv/bin/activate
```

Install TTS via pip
```bash
pip install --upgrade pip
pip install TTS
```

You can run the following command directly to checkout the basic text-to-speech model on your local host
```bash
tts-server
```


To do basic text-to-speech synthesis run
```bash
python3 basic.py
```

To do multilingual text-to-speech synthesis run
```bash
python3 multilingual.py
```

To voice clone run
```bash
python3 voice_clone.py
```

To do voice conversion run
```bash
python3 voice_conversion.py
```
