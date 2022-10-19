# Homework 3 - Virtual environment research

This instruction explains how to easily reproduce one of the results of the stunning virtual environment research presented in groundbreaking article, which is avalible at doi:10.1111/1000-7 

OS: Ubuntu 20.04.2 LTS

### 1. Download repository with scripts from github

SSH:

```bash
git clone git@github.com:krglkvrmn/Virtual_environment_research.git
```

HTTPS:

```bash
https://github.com/krglkvrmn/Virtual_environment_research.git
```

### 2. Download and install Python 3.11

```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.11
sudo apt install python3.11-dev python3.11-venv -y
```

### 3. Create python virtual environment with Python 3.11 version and activate it

```bash
python3.11 -m venv <env_name>
source ./<env_name>/bin/activate
```

### 4. Install required modules and run ultraviolence.py

- Install modules using requirements.txt file from this repository

```bash
pip install -r requirements.txt
```

      or use pip 

```bash
pip install google
pip install --upgrade google-api-python-client
pip install biopython
pip install aiohttp
pip install pandas
pip install opencv-python
pip install lxml
```

- Find lines [635:638] in [frame.py](http://frame.py) file located in “./<env_name>/lib/python3.11/site-packages/pandas/core/” and replace those lines with lines below (or make a comment from them yourself)

```python
#		if index is not None and isinstance(index, set):
#			raise ValueError("index cannot be a set")
#		if columns is not None and isinstance(columns, set):
#			raise ValueError("columns cannot be a set")
```

- Run [ultraviolence.py](http://ultraviolence.py)

```bash
python3.11 ultraviolence.py
```