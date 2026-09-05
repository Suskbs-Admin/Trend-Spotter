from crewai import Crew, Process
from trend_spotter.agents import get_agents
from trend_spotter.tasks import get_tasks

def run_trend_spotter(niche):
    """
    Sets up the agents, tasks, and crew to generate a trend-spotting newsletter.
    """
    # Get the agents and tasks
    agents = get_agents()
    tasks = get_tasks(niche)

    # Instantiate the Crew
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,  # Tasks will be executed one after another
        verbose=True
    )

    # Execute the crew and return the result
    return crew.kickoff()
