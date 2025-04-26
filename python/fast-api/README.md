# Exploring FastAPI Systems

Exploring system design patterns using FastAPI.

## Topics
- Batching
- Caches
- Counters
- Pub Sub
- Queues
- Rate Limiters

## Get Started
### Local
```bash
pyenv local 3.12.10
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
- in VS Code, press Ctrl+Shift+P -> search Python: Select Interpreter
- Pick the one that says .venv with the version in /.python-version

### Containerized
```bash
docker-compose up --build
```

#### Troubleshooting / Resolving common issues
Sometimes the containers build funcky and need to be pruned. You can use this command to prune the project:

```bash
docker-compose down --remove-orphans --volumes --rmi local
```