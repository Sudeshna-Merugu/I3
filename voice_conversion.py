import torch
from TTS.utils.radam import RAdam
import torch.serialization
from TTS.api import TTS

torch.serialization.add_safe_globals([RAdam])
vc_tts = TTS("voice_conversion_models/multilingual/vctk/freevc24")
vc_tts.voice_conversion_to_file(
    source_wav="voice1.wav",  # The voice speaking
    target_wav="voice2.wav",  # The target voice characteristics
    file_path="converted_voice.wav"
)