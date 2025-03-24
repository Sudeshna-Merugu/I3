import torch
from TTS.utils.radam import RAdam
import torch.serialization

# Add RAdam to the safe globals list
torch.serialization.add_safe_globals([RAdam])

# Now import TTS
from TTS.api import TTS

# For German
tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path="german_tts.wav")