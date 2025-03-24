import torch
from TTS.utils.radam import RAdam
import torch.serialization
from TTS.api import TTS

torch.serialization.add_safe_globals([RAdam])
tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path="german_tts.wav")
