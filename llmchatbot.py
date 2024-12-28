

#pip install ipywidgets 
#pip install groq 

import streamlit as st
import ipywidgets as widgets
from IPython.display import display
import os
os.environ["GROQ_API_KEY"] =  'Your groq api key here'

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

# Base URL for Epicurious
base_url = "https://www.epicurious.com"

# Scraper function for Epicurious search results
def scrape_epicurious(search_query):
    # URL encode the search query to handle spaces and special characters
    encoded_query = quote_plus(search_query)
    search_url = f"{base_url}/search?q={encoded_query}"  # Unified search URL

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Fetch the HTML content
    response = requests.get(search_url, headers=headers)

    # Debugging: print out the URL to verify it
    print(f"Fetching URL: {search_url}")

    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    # Scraping recipe results from the search page (check for specific sections related to recipes)
    for item in soup.find_all('h2'):
        title = item.text.strip()  # Extract the title
        parent_link = item.find_parent('a')
        if parent_link and parent_link.get('href'):
            link = base_url + parent_link['href']  # Full URL for the recipe
            results.append({"title": title, "link": link})

    return results

# Test the scraper with sample queries
test_queries = [
    "vegetarian lasagna",
    "pasta recipe for beginners",
    "simple pizza dough recipe",
    "chicken thighs",
    "tomatoes and basil",
    "summer barbecue",
    "mixer",
    "how to make a roux"
]

# Run the tests
for query in test_queries:
    print(f"\nSearching for: {query}")
    data = scrape_epicurious(query)
    if data:
        for item in data:
            print(f"- {item['title']} - {item['link']}")
    else:
        print(f"No results found for {query}.")

# Generate response using a defined LLM (Groq or OpenAI)
def enhanced_generate_response(user_question):
    # Extract a simplified search term
    search_query = user_question.lower().replace("?", "").split("recipe")[-1].strip()

    # Scrape Epicurious
    recipes = scrape_epicurious(search_query)
    if not recipes:
        return "I couldn't find any recipes for that query. Please try again with a different term."

    # Prepare data for LLM
    recipe_summary = "\n".join(
        [f"{idx + 1}. {recipe['title']} - {recipe['link']}" for idx, recipe in enumerate(recipes[:5])]
    )
    prompt = f"""
    You are a helpful assistant specializing in all aspects the Epicurious website. Based on the user's query, provide helpful detailed suggestions with a link to each.
    User Query: {user_question}
    Recipes Found:
    {recipe_summary}
    """

    # Generate response
    try:
        response = client.chat.completions.create(
            messages=[{"role": "system", "content": prompt}],
            model="llama3-8b-8192"
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {e}"

# Streamlit app
def main():
    st.title("Epicurious Chatbot")
    st.write("Ask questions about recipes, ingredients, occasions, and more!")

    # Input from user
    user_input = st.text_input("You:", placeholder="Ask your question here...")

    if user_input:
        with st.spinner("Thinking..."):
            # Generate response
            response = enhanced_generate_response(user_input)
        
        # Display the response
        st.markdown(f"**Chatbot:** {response}")

if __name__ == "__main__":
    main()