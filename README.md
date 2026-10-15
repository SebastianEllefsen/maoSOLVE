# maoSOLVE

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
maosolve init    # creates maosolve.toml
```

Edit `maosolve.toml` with your CTF details:

```toml
[maosolve]
flag_format = "FLAG{"
ctf_url = "https://ctf.example.com"
output_dir = "challdump"

[infisical]
env = "dev"
project_id = ""
```

Then run:

```bash
maosolve
```
