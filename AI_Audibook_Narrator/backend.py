from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kokoro import KPipeline
import soundfile as sf
import os
import re
import inflect
import numpy as np
import librosa

# Set MeCab environment variables
os.environ["MECABRC"] = "/etc/mecabrc"

# Initialize FastAPI app
app = FastAPI()

# Initialize Kokoro TTS Pipelines
pipeline = {
    "us": KPipeline(lang_code='a'),  # US English
    "uk": KPipeline(lang_code='b'),  # UK English
    "jp": KPipeline(lang_code='j'),  # Japanese
    "zh": KPipeline(lang_code='z'),  # Mandarin Chinese
    "es": KPipeline(lang_code='e'),  # Spanish
    "fr": KPipeline(lang_code='f'),  # French
    "hi": KPipeline(lang_code='h'),  # Hindi
    "it": KPipeline(lang_code='i'),  # Italian
    "pt": KPipeline(lang_code='p')   # Brazilian Portuguese
}

# Initialize number-to-word converter (for English only)
p = inflect.engine()

# Supported Voices by Language
SUPPORTED_VOICES = {
    "us": {
        "af_heart", "af_alloy", "af_aoede", "af_bella", "af_jessica",
        "af_kore", "af_nicole", "af_nova", "af_river", "af_sarah", "af_sky",
        "am_adam", "am_echo", "am_eric", "am_fenrir", "am_liam",
        "am_michael", "am_onyx", "am_puck", "am_santa"
    },
    "uk": {
        "bf_alice", "bf_emma", "bf_isabella", "bf_lily",
        "bm_daniel", "bm_fable", "bm_george", "bm_lewis"
    },
    "jp": {
        "jf_alpha", "jf_gongitsune", "jf_nezumi", "jf_tebukuro",
        "jm_kumo"
    },
    "zh": {
        "zf_xiaobei", "zf_xiaoni", "zf_xiaoxiao", "zf_xiaoyi",
        "zm_yunjian", "zm_yunxi", "zm_yunxia", "zm_yunyang"
    },
    "es": {
        "ef_dora", "em_alex", "em_santa"
    },
    "fr": {
        "ff_siwis"
    },
    "hi": {
        "hf_alpha", "hf_beta", "hm_omega", "hm_psi"
    },
    "it": {
        "if_sara", "im_nicola"
    },
    "pt": {
        "pf_dora", "pm_alex", "pm_santa"
    }
}

# Define request model
class NarrationRequest(BaseModel):
    text: str
    voice: str
    lang: str
    speed: float = 1.0

# Function to clean and preprocess text (for English only)
def clean_text(text, lang):
    if lang in ["us", "uk"]:  # Apply cleaning for English
        text = re.sub(r'\d+', lambda x: p.number_to_words(x.group()), text)
        text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', text)
        text = text.replace("–", "-").replace("—", "-").strip()
    return text

# Function to generate audio
def generate_audio(text, voice, lang, speed):
    try:
        if lang not in pipeline:
            raise ValueError(f"Unsupported language: {lang}")
        
        if voice not in SUPPORTED_VOICES[lang]:
            raise ValueError(f"Invalid voice: {voice} for language {lang}")

        text = clean_text(text, lang)

        sentences = re.split(r'(?<=[.?!])\s+', text)
        audio_files = []

        for i, sentence in enumerate(sentences):
            if len(sentence) < 2:
                continue
            
            generator = pipeline[lang](sentence, voice=voice, speed=speed, split_pattern=r'\n+')

            for j, (_, _, audio) in enumerate(generator):
                if audio is None:
                    continue
                
                audio_filename = f"chunk_{i}_{j}.wav"
                sf.write(audio_filename, audio, 24000, subtype="PCM_16")
                audio_files.append(audio_filename)

        if not audio_files:
            raise ValueError("No valid audio generated.")

        return merge_audio(audio_files)

    except Exception as e:
        print("❌ Error in TTS:", e)
        raise ValueError("TTS processing failed.")

# Function to merge audio chunks
def merge_audio(audio_files, output_file="final_audiobook.wav"):
    all_audio = []
    target_samplerate = 24000
    silence = np.zeros(int(target_samplerate * 0.3), dtype=np.float32)

    for file in audio_files:
        data, sr = sf.read(file, dtype="float32")

        if sr != target_samplerate:
            data = librosa.resample(data, orig_sr=sr, target_sr=target_samplerate)

        all_audio.append(data)
        all_audio.append(silence)

    merged_audio = np.concatenate(all_audio, axis=0)
    sf.write(output_file, merged_audio, target_samplerate, subtype="PCM_16")

    for file in audio_files:
        os.remove(file)

    return output_file

@app.post("/narrate/")
def narrate_text(request: NarrationRequest):
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty.")

        audio_file = generate_audio(request.text, request.voice, request.lang, request.speed)
        return {"message": "Audiobook created!", "audio_file": audio_file}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
