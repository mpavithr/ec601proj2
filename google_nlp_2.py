import google.cloud
import google.cloud.language

# Replace with API key
api_key = "YOUR_API_KEY"

# Initialize Google NLP client
client = google.cloud.language.LanguageServiceClient(credentials=api_key)

# Define URL to analyze
url = "https://www.cnn.com/2019/01/01/politics/trump-border-wall-speech/index.html"

# Analyze sentiment of text on page
document = google.cloud.language.types.Document(content=url, type=google.cloud.language.enums.Document.Type.WEB_PAGE)
sentiment = client.analyze_sentiment(document=document).document_sentiment

# Print results
print("Sentiment Score: {}".format(sentiment.score))
print("Sentiment Magnitude: {}".format(sentiment.magnitude))
