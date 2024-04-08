from openai import OpenAI
from dotenv import load_dotenv
import os


#gpt-3.5-turbo-instruct
load_dotenv()
api_key_1 = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key_1)

input_file_path = 'explorer_mode/convo.txt'
output_file_path = 'explorer_mode/sentiment_insights_output.txt'

with open(input_file_path, 'r') as file:
    # Read the entire contents of the file
    conversation_lines = file.readlines()

string = ""
for i in conversation_lines:
    string += i
speaker_insights = []
prompt = "Summarise each speaker's persona"


response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt + "\n" + string,
    temperature=0.7,
    max_tokens=100
)

# Extracting and formatting responses
output_text = response.choices[0].text.strip()

# Write output to file
with open('explorer_mode/sentiment_analysis_output.txt', 'w') as file:
    file.write(output_text)