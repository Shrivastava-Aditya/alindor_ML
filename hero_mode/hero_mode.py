import asyncio
import json
from deepgram import Deepgram

# Your Deepgram API Key
DEEPGRAM_API_KEY = 'd380fd244cf86e26408a124e9535e4b116cc7deb'

async def main():
    # Initialize the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)

    URL = 'https://www.youtube.com/watch?v=DrQ9dPQbfes'

    # Set the source
    source = {
        'url': URL,
    }

    # Send the audio to Deepgram and get the response
    response = await deepgram.transcription.prerecorded(
        source,
        {
            'smart_format': "true",
            'summarize': "v2",
        }
    )

    # Write the response to the console
    print(json.dumps(response, indent=4))

# Run the main asynchronous function
asyncio.run(main())