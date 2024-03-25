import asyncio
import json
from deepgram import Deepgram
from openai import OpenAI
from dotenv import load_dotenv
import os



# Your Deepgram API Key
DEEPGRAM_API_KEY = 'd380fd244cf86e26408a124e9535e4b116cc7deb'



def GPT_func(input_file_path='transcript_input.txt',output_file_path='sentiment_analysis_output.txt'):
    #gpt-3.5-turbo-instruct
    load_dotenv()
    api_key_1 = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key_1)

    with open(input_file_path, 'r') as file:
        # Read the entire contents of the file
        conversation_lines = file.readlines()

    string = "".join(conversation_lines)

    speaker_insights = []
    prompt = "Summarise each speaker's persona. There are only 2 speakers \n"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt + "\n" + string,
        temperature=0.7,
        max_tokens=100
    )

    # Extracting and formatting responses
    output_text = response.choices[0].text.strip()

    # Write output to file
    with open(output_file_path, 'w') as file:
        file.write(output_text)


async def main():
    # Initialize the Deepgram SDK
    load_dotenv()
    api_key_2 = os.getenv("DEEPGRAM_API_KEY")
    deepgram = Deepgram(api_key_2)

    URL = 'https://www.uclass.psychol.ucl.ac.uk/Release2/Conversation/AudioOnly/wav/F_0101_15y2m_1.wav'

    # Set the source
    source = {
        'url': URL,
    }

    # Send the audio to Deepgram and get the response
    response = await deepgram.transcription.prerecorded(
        source,
        {
           'language': 'en-US',  # Set the language of the audio
            'vocabulary': 'general',  # Specify the vocabulary
            'do_not_store': True,  # Optionally, set to True to prevent storing the audio
            'smart_format': True,  # Enable smart formatting
            'speaker_id': True,  # Enable speaker identification
            'summarize': 'v2',  # Use summarize API v2
        }
    )

    # Check if transcription was successful
    if 'results' in response:
        # Parse JSON response
        json_response = json.dumps(response, indent=4)
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        
        # Print JSON response
        print(json_response)

        # Save transcript to a file for analysis
        with open('transcript_input.txt', 'w') as file:
            file.write(transcript)
    else:
        print("Transcription failed.")

# Run the main asynchronous function
asyncio.run(main())
GPT_func()
