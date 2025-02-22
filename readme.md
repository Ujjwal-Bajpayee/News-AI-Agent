# AI News Agent

An autonomous AI agent that fetches, summarizes, and publishes news articles on a WordPress website. The agent crawls the web for news articles, classifies them into topics, summarizes the content, optimizes it for SEO, and publishes it autonomously.

---

## Features

- **Web Crawling**: Fetches news articles from reliable sources.
- **Content Summarization**: Summarizes articles using the `facebook/bart-large-cnn` model.
- **SEO Optimization**: Extracts keywords and optimizes content for search engines.
- **Automated Publishing**: Publishes articles to a WordPress website without manual intervention.
- **Bonus Features**:
  - Multilingual support (e.g., English, Hindi).
  - Image generation for blog posts.
  - User engagement metrics tracking.

---

## Tech Stack

- **Programming Language**: Python
- **Libraries**:
  - `requests`, `BeautifulSoup`, `Scrapy` (Web Crawling)
  - `transformers`, `sumy` (Summarization)
  - `nltk`, `spaCy` (NLP and SEO Optimization)
  - `wordpress-xmlrpc` or `REST API` (Publishing)
- **Frameworks**: Hugging Face Transformers, WordPress API
- **Hosting**: WordPress.com or self-hosted WordPress.org

---

## Setup Instructions

# First make a module file and upload 
│   ├── crawler.py         
│   ├── summarizer.py       
│   ├── seo_optimizer.py    
│   ├── publisher.py


### 1. Clone the Repository
### 2. Set Up a Virtual Environment
### 3.  Install Dependencies
### 4.  Run the Script
python main.py
