from crewai import Agent, LLM
from crewai_tools import SerperDevTool
import os

# Initialize tools that will be shared across agents
# SerperDevTool is used for general web searches
search_tool = SerperDevTool()

# Initialize OpenRouter LLM
# We use the LLM class from crewai to point to OpenRouter's OpenAI-compatible API
llm = LLM(
    model=os.getenv("MODEL_NAME", "openai/minimax/minimax-m3:free"),
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def get_agents():
    """
    Returns the defined agents for the trend-spotting crew.
    Each agent is defined with a specific role, goal, and backstory to
    shape its behavior and the quality of its output.
    """

    # 1. Trend Researcher: The 'Scout'
    # This agent is responsible for the initial discovery phase.
    trend_researcher = Agent(
        role='Trend Researcher',
        goal='Identify the top 3 emerging trends in a given niche for the current week by scanning digital signals.',
        backstory=(
            "A digital native and 'internet sleuth' with an obsession for early signals. "
            "You know exactly where to look—Reddit, X, niche blogs, and GitHub—to find "
            "what is about to blow up before it hits the mainstream media."
        ),
        tools=[search_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        memory=False
    )

    # 2. Market Analyst: The 'Strategist'
    # This agent adds a layer of critical thinking to the raw research.
    market_analyst = Agent(
        role='Market Analyst',
        goal='Evaluate the significance, potential impact, and the "why now" for the identified trends to separate hype from value.',
        backstory=(
            "A former venture capitalist and data scientist who specializes in structural shifts. "
            "You possess a critical eye and can synthesize raw data into a strategic thesis, "
            "assigning impact scores to emerging technologies."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
        memory=False
    )

    # 3. Newsletter Editor: The 'Storyteller'
    # This agent transforms the technical analysis into a reader-friendly format.
    newsletter_editor = Agent(
        role='Newsletter Editor',
        goal='Synthesize the research and analysis into a high-engagement, punchy newsletter that readers actually want to open.',
        backstory=(
            "An award-winning journalist known for making complex topics accessible and addictive. "
            "You specialize in 'The Hook,' storytelling, and clear calls to action, "
            "transforming dry analysis into a compelling narrative."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
        memory=False
    )

    return {
        "researcher": trend_researcher,
        "analyst": market_analyst,
        "editor": newsletter_editor
    }
