import google.cloud
import google.cloud.language

# Replace with API key
api_key = "MY_API_KEY"

# Initialize Google NLP client
client = google.cloud.language.LanguageServiceClient(credentials=api_key)

# Define text to analyze
text = "I am feeling stressed"

# Analyze sentiment of text
document = google.cloud.language.types.Document(content=text, type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)
sentiment = client.analyze_sentiment(document=document).document_sentiment

# Print results
print("Sentiment Score: {}".format(sentiment.score))
print("Sentiment Magnitude: {}".format(sentiment.magnitude))
