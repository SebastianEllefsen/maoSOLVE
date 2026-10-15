import click
from rich.console import Console

from maosolve.config import config_path, create_default_config, load_config
from maosolve.secrets import get_ctfd_session
from maosolve.ctfd import fetch_challenges
from maosolve.solver import scan_for_flags

console = Console()


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """maoSOLVE 3 — Agentic AI CTF solver."""
    if ctx.invoked_subcommand is None:
        ctx.invoke(run)


@main.command()
def init():
    """Create a default maosolve.toml config file."""
    path = config_path()
    import os
    if os.path.exists(path):
        console.print(f"[yellow]Config already exists:[/yellow] {path}")
        return
    create_default_config()
    console.print(f"[green]Created config:[/green] {path}")
    console.print("Edit it with your CTF details, then run [bold]maosolve[/bold].")


@main.command()
def run():
    """Fetch challenges and scan for flags."""
    cfg = load_config()
    if not cfg:
        console.print("[red]No maosolve.toml found.[/red] Run [bold]maosolve init[/bold] first.")
        raise SystemExit(1)

    ms = cfg.get("maosolve", {})
    inf = cfg.get("infisical", {})

    flag_format = ms.get("flag_format", "")
    ctf_url = ms.get("ctf_url", "")
    out = ms.get("output_dir", "challdump")
    env = inf.get("env", "dev")
    project_id = inf.get("project_id", "")

    if not flag_format:
        console.print("[red]flag_format is not set in maosolve.toml[/red]")
        raise SystemExit(1)
    if not ctf_url:
        console.print("[red]ctf_url is not set in maosolve.toml[/red]")
        raise SystemExit(1)

    console.print("[bold cyan]maoSOLVE 3[/bold cyan]")
    console.print(f"Flag format: [green]{flag_format}[/green]")
    console.print(f"CTF URL:     [green]{ctf_url}[/green]")
    console.print()

    console.print("[bold]Fetching CTFd session from Infisical...[/bold]")
    session = get_ctfd_session(env=env, project_id=project_id or None)

    console.print("[bold]Downloading challenges with ctfdget...[/bold]")
    fetch_challenges(url=ctf_url, session=session, out=out)

    console.print(f"[bold]Scanning files for flags matching [green]{flag_format}[/green]...[/bold]")
    flags = scan_for_flags(directory=out, flag_format=flag_format)

    if flags:
        console.print(f"\n[bold green]Found {len(flags)} flag(s):[/bold green]")
        for path, flag in flags:
            console.print(f"  [dim]{path}[/dim] → [bold yellow]{flag}[/bold yellow]")
    else:
        console.print("\n[bold red]No flags found.[/bold red]")
