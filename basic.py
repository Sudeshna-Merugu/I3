import torch
from TTS.utils.radam import RAdam
import torch.serialization
from TTS.api import TTS

torch.serialization.add_safe_globals([RAdam])
tts = TTS("tts_models/en/ljspeech/glow-tts")
tts.tts_to_file(text="This is a basic text to speech example.", file_path="basic_tts.wav")
