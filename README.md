## setup
```
cp telescope_config.json.tmp telescope_config.json
cp cookie.json.tmp cookie.json
```
edit `cookie.json` by adding the session cookie

## virtual env
install
```
sudo apt-get install python3-venv
```
creation
```
python3 -m venv /path/to/virtual/environment
```
activation
```
source /path/to/virtual/environment/bin/activate
```

## env packages
installing packages already on requirement list
```
pip install -r requirements.txt
```
installing new package
```
pip install [package name]
```

## pre-commit pipeline
installing packages
```
pip install black flake8
```
installing pre-commit hook
```
pre-commit install
```
