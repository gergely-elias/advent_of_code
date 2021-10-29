## setup
```
cp telescope_config.json.tmp telescope_config.json
cp cookie.json.tmp cookie.json
```
edit `cookie.json` by adding the session cookie

## virtual env
creation
```
python3 -m venv /path/to/virtual/environment
```
activation
```
source /path/to/virtual/environment/bin/activate
```

## pre-commit pipeline
installing packages
```
sudo apt install black flake8
```
installing pre-commit hook
```
pre-commit install
```
