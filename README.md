# Coqui

This repository is to checkout how the Coqui TTS service can be run on local systems. Your output files will be created upon running the python scripts. 

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


To do basic text-to-speech synthesis run. NOTE: You can change the model being used to any of the models available. To get available models, enter the command: `tts --list_models`.
```bash
python3 basic.py # stored in `basic_tts.wav`
```

To do multilingual text-to-speech synthesis run. NOTE: You can change the language here as well, by going through the listed languages.
```bash
python3 multilingual.py # stored in `german_tts.wav`
```

To voice clone run. NOTE: Source voice needed to run this (example, `voice1.wav`)
```bash
python3 voice_clone.py # stored in `cloned_voice.wav`
```

To do voice conversion run. NOTE: Source voice needed to run this (example, `voice1.wav`) as well as Target voice (example, `voice2.wav`).
```bash
python3 voice_conversion.py # stored in `converted_voice.wav`
```
