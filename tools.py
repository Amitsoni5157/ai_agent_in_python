from datetime import datetime
from langchain_core.tools import Tool
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from duckduckgo_search import DDGS

def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """Appends research data into a local text file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"


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


# --- LangChain Tool Instantiations ---

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves the research output to a text file.",
)

search_tool = Tool(
    name="DuckDuckGo_Search",
    description="Useful for searching the internet for current events, facts, and real-time data.",
    func=internet_search_function,
)

# Configuration for Wikipedia API Wrapper
api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_char_max=500)
wiki_tool = Tool(
    name="Wikipedia_Search",  
    description="Useful for searching Wikipedia for facts, history, and general knowledge.",
    func=api_wrapper.run      
)