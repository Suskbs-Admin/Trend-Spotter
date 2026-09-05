import os
import sys
from dotenv import load_dotenv
from trend_spotter.crew import run_trend_spotter
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt

# Initialize Rich Console
console = Console()

def display_welcome():
    """Displays a professional welcome banner."""
    welcome_text = "[bold white]Trend-Spotter[/bold white]\n[dim]AI-Powered Trend Spotting Newsletter Generator[/dim]"
    console.print(Panel(welcome_text, expand=False, border_style="blue", title="Welcome"))

def main():
    # Load environment variables from .env file
    load_dotenv()

    display_welcome()

    # Check if SERPER_API_KEY is set
    if not os.getenv("SERPER_API_KEY"):
        console.print(Panel(
            "[bold red]Error: SERPER_API_KEY is not set![/bold red]\n"
            "Please create a .env file and add: [bold]SERPER_API_KEY=your_api_key_here[/bold]",
            title="Configuration Error",
            border_style="red"
        ))
        sys.exit(1)

    # Get the niche from command line arguments or prompt the user
    if len(sys.argv) > 1:
        niche = " ".join(sys.argv[1:])
    else:
        niche = Prompt.ask("\n[bold blue]Enter the niche you want to spot trends for[/bold blue]")

    if not niche:
        console.print("[bold red]Error: A niche must be provided.[/bold red]")
        sys.exit(1)

    try:
        # Wrap the long-running crew process in a status spinner
        with console.status("[bold blue]Analyzing trends and crafting your newsletter... Please wait...[/bold blue]", spinner="dots"):
            # Run the crew and get the final result
            result = run_trend_spotter(niche)

            # The result of kickoff() in newer CrewAI versions is often a CrewOutput object
            final_newsletter = str(result)

        # Save the result to a file
        filename = f"newsletter_{niche.replace(' ', '_').lower()}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_newsletter)

        console.print(f"\n[bold green]Newsletter generated successfully![/bold green]")
        console.print(f"Saved to: [italic]{filename}[/italic]\n")

        # Render the final newsletter as formatted Markdown in a Panel
        console.print(Panel(
            Markdown(final_newsletter),
            title="Generated Newsletter",
            border_style="green",
            expand=False
        ))

    except Exception as e:
        console.print(Panel(
            f"[bold red]An unexpected error occurred:[/bold red]\n{str(e)}",
            title="Execution Error",
            border_style="red"
        ))
        sys.exit(1)

if __name__ == "__main__":
    main()
