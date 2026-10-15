import click
from rich.console import Console

from maosolve.secrets import get_ctfd_session
from maosolve.ctfd import fetch_challenges
from maosolve.solver import scan_for_flags

console = Console()


@click.command()
@click.argument("flag_format")
@click.option("--url", required=True, help="CTFd instance URL.")
@click.option("--out", default="challdump", help="Output directory for challenges.")
@click.option(
    "--env",
    default="dev",
    help="Infisical environment (dev, staging, prod).",
)
@click.option(
    "--project-id",
    envvar="INFISICAL_PROJECT_ID",
    help="Infisical project ID. Can also set INFISICAL_PROJECT_ID.",
)
def main(flag_format, url, out, env, project_id):
    """maoSOLVE 3 — Agentic AI CTF solver.

    FLAG_FORMAT is the flag prefix to search for (e.g. 'CTF{', 'flag{').
    """
    console.print(f"[bold cyan]maoSOLVE 3[/bold cyan]")
    console.print(f"Flag format: [green]{flag_format}[/green]")
    console.print(f"CTF URL:     [green]{url}[/green]")
    console.print()

    console.print("[bold]Fetching CTFd session from Infisical...[/bold]")
    session = get_ctfd_session(env=env, project_id=project_id)

    console.print("[bold]Downloading challenges with ctfdget...[/bold]")
    fetch_challenges(url=url, session=session, out=out)

    console.print(f"[bold]Scanning files for flags matching [green]{flag_format}[/green]...[/bold]")
    flags = scan_for_flags(directory=out, flag_format=flag_format)

    if flags:
        console.print(f"\n[bold green]Found {len(flags)} flag(s):[/bold green]")
        for path, flag in flags:
            console.print(f"  [dim]{path}[/dim] → [bold yellow]{flag}[/bold yellow]")
    else:
        console.print("\n[bold red]No flags found.[/bold red]")
