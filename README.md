# llm-chatbot 
# LLM-Powered Epicurious Chatbot

This project is a chatbot powered Groq (using llama3-8b-8192 for the model) that provides detailed answers about content on the Epicurious website. Users can ask questions about recipes, ingredients, occasions, techniques, and more, and the chatbot will fetch relevant data and provide helpful responses.

---

## Features

- Answers questions about Epicurious and site content.
- Fetches recipes, ingredients, and kitchen tips.
- Uses the Groq API for advanced LLM capabilities.
- Simple interface powered by Streamlit.

---

## Prerequisites

Before running the chatbot, ensure the following are installed on your system:
1. **Python**: Version 3.7 or above.
2. **Pip**: Ensure pip is up to date.

---

## Installation & Setup

1. Instructions for setup can be found in the instructions.txt file

---

## Technical Stack
**Web Scraping**: BeautifulSoup, Requests (for scraping Epicurious). 

**Language Model**: Groq, model: llama3-8b-8192 

**Web Framework**: Streamlit for interactive user interface.  

--- 

## Steps Taken
**Web Scraping**: Used BeautifulSoup to scrape Epicurious for relevant data, including recipes, ingredients, and kitchen tools. 

**LLM Integration**: Integrated Groq API to generate detailed and context-based responses to user queries based on the scraped data. 

**Chatbot Interface**: Built an interactive chatbot UI using Streamlit, where users input their questions, and the chatbot responds using scraped data and generated LLM answers. 

**Testing**: Created 20 test questions to cover different categories of data and ensured that the chatbot can handle them correctly. 

**Deployment**: The chatbot was deployed locally by running it in powershell, and tested through manual interactions.




