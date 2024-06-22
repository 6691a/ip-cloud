## MAC
### Install dependencies
```
brew install pyenv poetry
```

### Install python
```
pyenv install 3.12.2
```

### Create virtualenv
```
poetry env use $(pyenv which python3.12)
poetry shell
```

### Install requirements
```
poetry install --dev
poetry env info
```

### pre-commit
   1. pre-commit test ```pre-commit run --all-files```
   2. pre-commit cache clear ```pre-commit clean```
