from datetime import datetime

import wikipedia
wikipedia.set_user_agent("MyResearchAgent/1.0 (contact@example.com)")
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.tools import tool
from duckduckgo_search import DDGS

@tool
def save_to_txt(data: str, filename: str = "Research_output.txt") -> str:
    """Appends research data into a local text file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

@tool
def internet_search_function(query: str) -> str:
    """Performs a live web search using DuckDuckGo and returns top results."""
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            if not results:
                return "No results found."

            formatted_results = []
            for r in results:
                formatted_results.append(
                    f"Title: {r['title']}\nLink: {r['href']}\nSnippet: {r['body']}\n---"
                )
            return "\n".join(formatted_results)
    except Exception as e:
        return f"Error while searching: {str(e)}"


# --- 3. Wikipedia Search Tool ---
# Configuration for Wikipedia API Wrapper
api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_char_max=500)

@tool
def wikipedia_search(query: str) -> str:
    """Useful for searching Wikipedia for facts, history, and general knowledge."""
    return api_wrapper.run(query)
# --- LangChain Tool Instantiations ---

save_tool = save_to_txt
search_tool = internet_search_function
wiki_tool = wikipedia_search


# # --- LangChain Tool Instantiations ---

# save_tool = Tool(
#     name="save_text_to_file",
#     func=save_to_txt,
#     description="Saves the research output to a text file.",
# )

# search_tool = Tool(
#     name="DuckDuckGo_Search",
#     description="Useful for searching the internet for current events, facts, and real-time data.",
#     func=internet_search_function,
# )

# # Configuration for Wikipedia API Wrapper
# api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_char_max=500)
# wiki_tool = Tool(
#     name="Wikipedia_Search",  
#     description="Useful for searching Wikipedia for facts, history, and general knowledge.",
#     func=api_wrapper.run      
# )