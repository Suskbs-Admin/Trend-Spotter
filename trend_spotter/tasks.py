from crewai import Task
from trend_spotter.agents import get_agents

def get_tasks(niche):
    """
    Defines the tasks for the trend-spotting crew.
    The tasks are linked to specific agents and designed to create a pipeline
    of research, analysis, and synthesis.
    """
    agents = get_agents()

    # 1. Research Task
    research_task = Task(
        description=(
            f"Scan the internet for the top 3 emerging trends in the '{niche}' niche for the current week. "
            "Look for digital signals in Reddit, X, niche blogs, and GitHub. "
            "For each trend, provide a brief description and a list of sources/evidence."
        ),
        expected_output="A detailed report identifying 3 emerging trends with descriptions and supporting evidence.",
        agent=agents['researcher']
    )

    # 2. Analysis Task
    analysis_task = Task(
        description=(
            "Review the 3 emerging trends identified by the researcher. "
            "For each trend, evaluate its significance, potential market impact, and explain 'why now'. "
            "Separate genuine value from temporary hype and assign an impact score from 1 to 10."
        ),
        expected_output="A strategic analysis of the 3 trends, including impact scores and a 'why now' thesis for each.",
        agent=agents['analyst']
    )

    # 3. Editorial Task
    editorial_task = Task(
        description=(
            "Transform the research and strategic analysis into a high-engagement, punchy newsletter. "
            "Focus on a compelling 'Hook', clear storytelling, and a strong call to action. "
            "The final output should be formatted as a ready-to-send newsletter."
        ),
        expected_output="A polished, reader-friendly newsletter that synthesizes the trends and analysis into a compelling narrative.",
        agent=agents['editor']
    )

    return [research_task, analysis_task, editorial_task]
