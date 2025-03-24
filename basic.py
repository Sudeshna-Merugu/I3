import torch
from TTS.utils.radam import RAdam
import torch.serialization

# Add RAdam to the safe globals list
torch.serialization.add_safe_globals([RAdam])

# Now import TTS and create your model
from TTS.api import TTS

# Initialize with a basic English model
tts = TTS("tts_models/en/ljspeech/glow-tts")  # Try a different model

# Generate speech
tts.tts_to_file(text="This is a basic text to speech example.", file_path="basic_tts.wav")