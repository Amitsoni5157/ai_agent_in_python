from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

class ResearchAgent:
    def __init__(self, llm, tools):
        """Initializes the agent with an LLM instance and a list of tools."""
        self.llm = llm
        self.tools = tools
        self.prompt = self._create_prompt()
        self.executor = self._create_executor()

    def _create_prompt(self) -> ChatPromptTemplate:
        """Defines the prompt structure required by the tool-calling agent."""
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a research assistant that will help generate a research paper. "
                    "Answer the user query using the necessary tools provided. "
                    "For any factual, academic, or research-oriented query, you MUST use the search tools (`wikipedia_search` or `internet_search_function`) to find the information, even if you already know the answer. Do not answer directly without using a tool. "
                    "When you need to call a tool, output ONLY the tool call without any conversational text or filler before or after it. "
                    "Once you have final research insights, provide a comprehensive summary. "
                    "If the user's query is completely unrelated to research, academic topics, or factual queries "
                    "(for example, simple greetings, casual chitchat, jokes, or commands like 'tell me a joke'), "
                    "do NOT use any tools. Instead, politely inform the user in English/Hinglish that you are a "
                    "research assistant designed to help with research papers, and ask them to ask a research-oriented question.",
                ),
                ("placeholder", "{chat_history}"),
                ("human", "{query}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

    def _create_executor(self) -> AgentExecutor:
        """Creates the runtime agent and binds it within an AgentExecutor."""
        agent = create_tool_calling_agent(
            llm=self.llm,
            prompt=self.prompt,
            tools=self.tools
        )
        return AgentExecutor(agent=agent, tools=self.tools, verbose=True)

    def run(self, query: str) -> str:
        """Executes the user query through the agent framework."""
        try:
            raw_response = self.executor.invoke({"query": query})
            return raw_response.get("output", "")
        except Exception as e:
            print(f"\n[DEBUG ERROR] actual error is: {e}\n")
            return "I am a research assistant designed to help with research papers. Please ask a research-oriented question."