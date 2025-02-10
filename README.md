# Multilingual-AI-Audiobook-Narrator 


## AI Audiobook Narrator 🎙️📖
This repository presents an AI-powered multilingual audiobook narrator that converts text into natural-sounding speech using FastAPI, Streamlit, and Kokoro TTS. The system supports multiple languages, offers customizable voices, and allows users to adjust narration speed, making it an efficient and user-friendly tool for text-to-speech applications.

## Table of Contents
- [Key Features](#key-features)
- [Supported Languages & Voices](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Results & UI Screenshots](#results)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Key Features:
- ***🎙 Multilingual TTS -***   Convert text to speech in multiple languages.
- ***🗣 Customizable Voices -*** Select from various AI-generated voices per language.
- ***⏩ Adjustable Speed -*** Control narration pace for a personalized experience.
- ***🌐 FastAPI Backend -*** Ensures efficient real-time text-to-speech conversion.
- ***💻 Streamlit UI -*** User-friendly interface for easy interaction.
- ***🎧 Audio Output -*** Save and download generated audiobooks.

## Supported Languages & Voices 🌍
This AI audiobook narrator currently supports the following languages and voices:
 

| **Language**            | **Code** | **Available Voices**                                      |
|-------------------------|---------|-----------------------------------------------------------|
| **US English**          | `us`     | af_heart, af_alloy, af_aoede, af_bella, af_jessica, af_kore, af_nicole, af_nova, af_river, af_sarah, af_sky, am_adam, am_echo, am_eric, am_fenrir, am_liam, am_michael, am_onyx, am_puck, am_santa|
| **UK English**          | `uk`     | bf_alice, bf_emma, bf_isabella, bf_lily, bm_daniel, bm_fable, bm_george, bm_lewis |
| **Japanese**           | `jp`     | jf_alpha, jf_gongitsune, jf_nezumi, jf_tebukuro, jm_kumo  |
| **Mandarin Chinese**   | `zh`     | zf_xiaobei, zf_xiaoni, zf_xiaoxiao, zf_xiaoyi, zm_yunjian, zm_yunxi, zm_yunxia, zm_yunyang |
| **Spanish**            | `es`     | ef_dora, em_alex, em_santa                                |
| **French**             | `fr`     | ff_siwis                                                 |
| **Hindi**              | `hi`     | hf_alpha, hf_beta, hm_omega, hm_psi                      |
| **Italian**            | `it`     | if_sara, im_nicola                                       |
| **Brazilian Portuguese** | `pt`    | pf_dora, pm_alex, pm_santa                               |


## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator.git
2. Change to Project directory
    ```bash
    cd AI_Audibook_Narrator
3. Install required packages :
    ```bash
    pip install -r requirements.txt
4. Install system Dependencies
    ```bash
    apt-get -qq -y install espeak-ng > /dev/null 2>&1
**Note:** If you encounter any issues with MeCab, dictionary indexing, or Python integration (e.g., ***ModuleNotFoundError: No module named 'fugashi*** or ***RuntimeError: Unknown dictionary format***), follow the step-by-step guide in the [**mecab-fix**](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/mecab-fix/mecab_fugashi_fix.txt) folder. 

Ensure that MeCab is properly installed, the dictionary is indexed correctly, and the correct environment variables are set. If the issue persists, try reinstalling MeCab, rebuilding the dictionary, and verifying the Python bindings.

For additional help, check the official [**MeCab documentation**](https://github.com/taku910/mecab/) or open an issue in this repository."

## Usage
1. Run the FastAPI Backend
    ```bash
    uvicorn backend:app --host 0.0.0.0 --port 8000
2. Start the Streamlit UI
    ```bash
    streamlit run main.py
3. Interact with the UI
    - Enter the text you want to convert to speech.
    - Select the language and voice.
    - Adjust narration speed.
    - Click "Generate Audiobook" to create the audio.
    - Listen to the generated speech or download the audiobook by clicking Download Audiobook button.
4. Sample Inputs & Outputs  
    - For reference, the input texts used for generating the audio samples along with voice used are stored in the `input_texts/` directory.  
        - 📄 [Sample US English Input](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/input_texts/US_English_test.txt)  
        - 📄[Sample UK English Input](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/input_texts/UK_English_test.txt)  
        - 📄[Sample Japanese Input](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/input_texts/Japanese_test.txt) 
        - 📄 [Sample Mandarin Chinese Input](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/input_texts/Chinese_test.txt) 
        - 📄 [Sample Spanish Input](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/input_texts/Spanish_test.txt)    
        - 📄 [Sample French Input](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/input_texts/French_test.txt)
        - 📄[Sample Hindi Input](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/input_texts/Hindi_test.txt)
        - 📄[Sample Italian Input](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/input_texts/Italian_test.txt)
        - 📄[Sample Brazilian Portuguese Input](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/input_texts/Brazilian_Portuguese_test.txt)  

The corresponding generated audio files can be found in the `generated_audio/` directory.


## Results & UI Screenshots

### 🎨 AI Audiobook Narrator UI

![alt text](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/demo_images/italian_image1.png?raw=true) 
![alt text](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/demo_images/US_english_image2.png?raw=true) 

### 📁 Audio Output Example
Generated audio files are saved in the output_audio/ directory.

📢 Here’s a sample of AI-generated audiobook narration.


🎧 [Download Sample US English Generated output](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/generated_audios/US_English_output.wav)

🎧 [Download Sample UK English Generated output](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/generated_audios/UK_English_output.wav)

🎧 [Download Sample Japanese Generated output](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/generated_audios/Japanese_output.wav)

🎧 [Download Sample Mandarin Chinese Generated output](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/generated_audios/Chinese_output.wav)

🎧 [Download Sample Spanish Generated output](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/generated_audios/Spanish_output.wav)

🎧 [Download Sample French Generated output](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/generated_audios/French_output.wav)

🎧 [Download Sample Hindi Generated output](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/generated_audios/Hindi_output.wav)

🎧[Download Sample Italian Generated output](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/generated_audios/Italian_output.wav)

🎧 [Download Sample Brazilian Portuguese Generated output](https://github.com/krishnapriya-nynaru/Multilingual-AI-Audiobook-Narrator/blob/main/AI_Audibook_Narrator/generated_audios/Brazilian%20Portuguese_output.wav)

## Contributing 
Contributions are welcome! To contribute to this project:
1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and ensure the code passes all tests.
4. Submit a pull request with a detailed description of your changes.

If you have any suggestions for improvements or features, feel free to open an issue!

## Acknowledgments  
- [**FastAPI**](https://fastapi.tiangolo.com/) For the high-performance backend.
- [**Streamlit**](https://streamlit.io/) For the interactive user interface.
- [**Kokoro TTS**](https://huggingface.co/hexgrad/Kokoro-82M) For AI-driven text-to-speech synthesis. 
- [**Librosa**](https://github.com/librosa/librosa) For audio processing.
- [**espeak-ng**](https://github.com/espeak-ng/espeak-ng) For multilingual speech synthesis.

🔗 Explore, contribute, and bring your text to life with AI-powered audiobooks! 🚀📖

