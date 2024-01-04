import yfinance as yf
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests

# Download NLTK data for sentiment analysis
nltk.download('vader_lexicon')

# Function to analyze sentiment of a text
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']
    return sentiment_score

# Function to get stock information using yfinance
def get_stock_info(ticker):
    stock_data = yf.Ticker(ticker)
    return stock_data.info

# Function to get financial news and analyze sentiment
def get_news_sentiment(ticker):
    news_url = f'https://newsapi.org/v2/everything?q={ticker}&apiKey=your-api-key'  # Replace 'your-api-key' with an actual API key if needed
    
    response = requests.get(news_url)
    news_data = response.json()

    if 'articles' in news_data:
        for article in news_data['articles']:
            title = article['title']
            description = article.get('description', '')

            # Analyze sentiment of title and description
            title_sentiment = analyze_sentiment(title)
            description_sentiment = analyze_sentiment(description)

            print(f"Title: {title}")
            print(f"Title Sentiment: {title_sentiment}")
            print(f"Description: {description}")
            print(f"Description Sentiment: {description_sentiment}")
            print("\n")

# Example usage
if __name__ == "__main__":
    stock_ticker = 'AAPL'  # Replace with the desired stock ticker
    get_news_sentiment(stock_ticker)
    stock_info = get_stock_info(stock_ticker)
    print("Stock Information:")
    display(stock_info)