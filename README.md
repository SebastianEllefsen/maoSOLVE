# maoSOLVE 3

Agentic AI CTF solver.

## Setup

```bash
pip install -e .
```

### Dependencies

- [ctfdget](https://github.com/HanEmile/ctfdget) — `go install github.com/HanEmile/ctfdget@latest`
- [stringcheese](https://github.com/MathisHammel/stringcheese) — `pip install stringcheese`
- [Infisical CLI](https://infisical.com/docs/cli/overview) — for secret management

Store your CTFd session cookie as `CTFD_SESSION` in Infisical.

## Usage

```bash
maosolve "FLAG{" --url https://ctf.example.com
```

### Options

| Flag | Description |
|------|-------------|
| `FLAG_FORMAT` | Flag prefix to search for (e.g. `CTF{`, `flag{`) |
| `--url` | CTFd instance URL (required) |
| `--out` | Output directory (default: `challdump`) |
| `--env` | Infisical environment (default: `dev`) |
| `--project-id` | Infisical project ID (or set `INFISICAL_PROJECT_ID`) |
