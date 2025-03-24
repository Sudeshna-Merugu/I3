import torch
from TTS.utils.radam import RAdam
import torch.serialization
from TTS.api import TTS

torch.serialization.add_safe_globals([RAdam])
tts = TTS("tts_models/multilingual/multi-dataset/your_tts")
tts.tts_to_file(
    text="This is my cloned voice speaking English.",
    speaker_wav="voice1.wav",
    language="en",
    file_path="cloned_voice.wav"
)