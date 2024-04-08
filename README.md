# Sentiment and Psychological Analysis

This repository provides solutions for sentiment and psychological analysis using text-to-text and speech-to-text conversion methods, integrating OpenAI's GPT API and Deepgram. Below are the details and instructions for navigating the project:

## Directory Structure

- **Explorer Mode**: Contains text-to-text solutions utilizing OpenAI's GPT API.
- **Hero Mode**: Contains solutions for speech-to-text conversion using OpenAI and Deepgram.
Note : Output is stored in sentiment_analysis_output.txt for both the solutions.
## Installation

To run the provided scripts, you need to install the necessary dependencies. Below are the commands to download the required packages:

### For Explorer Mode:
```bash
pip install openai
pip install python-dotenv
```

### For Hero Mode:
```bash
pip install openai
pip install deepgram
pip install python-dotenv
```

## Running the Files

### 1. `openAIapi.py` (For Explorer Mode)

This script utilizes OpenAI's GPT API to perform sentiment and psychological analysis on text data.

#### Command to run:
```bash
python openAIapi.py
```

### 2. `hero_mode.py` (For Hero Mode)

This script integrates both OpenAI's GPT API and Deepgram for sentiment and psychological analysis on audio data.

#### Command to run:
```bash
python hero_mode.py
```

## Additional Notes

- Ensure you have appropriate API keys and configurations set up, especially if utilizing services like OpenAI and Deepgram.
- Make sure to have proper environment variables set up, especially for sensitive information like API keys. Utilize a `.env` file for storing these variables securely.

By following these instructions, you can effectively utilize the sentiment and psychological analysis solutions provided in this repository.

Planning to further extending this idea as web interface using flask or FastAPI. Contributions are welcome 🤍