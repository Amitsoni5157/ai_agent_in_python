from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel
from tools import search_tool, wiki_tool, save_tool
from agent import ResearchAgent

# Define the structured output model using Pydantic
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Initialize the Language Model (LLM)
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    
    # Collect all imported tools into a list
    tools = [search_tool, wiki_tool, save_tool]  
    
    # Initialize our custom ResearchAgent class
    research_agent = ResearchAgent(llm=llm, tools=tools)
    
    # Define execution query
    query = "What is the capital of France?"
    print("Executing query...")
    
    # Execute the query using our agent's clean run interface
    output = research_agent.run(query)
    
    print("\n--- Agent Final Output ---")
    print(output)


if __name__ == '__main__':
    main()