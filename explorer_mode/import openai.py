from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key='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')

# Cached results to avoid redundant API calls
sentiment_cache = {}

def analyze_sentiment_batch(texts):
    global sentiment_cache
    results = []

    # Check cache for previously analyzed texts
    for text in texts:
        if text in sentiment_cache:
            results.append(sentiment_cache[text])
        else:
            results.append(None)

    # Batch texts for sentiment analysis
    batch_texts = [text for text, result in zip(texts, results) if result is None]
    if batch_texts:
        batch_results = client.completions.create(
            model="gpt-3.5-turbo-16k-0613",
            prompt=batch_texts,
            max_tokens=50,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        for text, result in zip(batch_texts, batch_results.choices):
            sentiment_cache[text] = result.text.strip()
            results.append(result.text.strip())

    return results

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        conversations = f.readlines()

    with open(output_file, 'w') as f_out:
        for i in range(0, len(conversations), 2):
            # Analyze sentiments in batches
            person1_sentiments = analyze_sentiment_batch(conversations[i:i+2])
            person1_sentiment, person2_sentiment = person1_sentiments

            f_out.write(f"Person 1: {person1_sentiment}\n")
            f_out.write(f"Person 2: {person2_sentiment}\n")
            f_out.write("\n")

if __name__ == "__main__":
    input_file = "conversation_input.txt"
    output_file = "sentiment_analysis_output.txt"
    main(input_file, output_file)
