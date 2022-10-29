# Homework 3 - Virtual environment research

This instruction explains how to easily reproduce one of the results of the stunning virtual environment research presented in groundbreaking article, which is avalible at doi:10.1111/1000-7 

OS: Ubuntu 20.04.2 LTS

### 1. Create new folder and download repository with scripts from github

SSH:

```bash
mkdir venv_research
cd venv_research
git clone git@github.com:krglkvrmn/Virtual_environment_research.git
```

HTTPS:

```bash
mkdir venv_research
cd venv_research
https://github.com/krglkvrmn/Virtual_environment_research.git
```

### 2. Download and install Python 3.11

```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.11
sudo apt install python3.11-dev python3.11-venv -y
```

### 3. Create python virtual environment with Python 3.11 version and activate it (don’t forget to deactivate your current environment)

```bash
deactivate # or 'conda deactivate' if you use conda environment
```

```bash
python3.11 -m venv venv_research_env
source ./venv_research_env/bin/activate
```

### 4. Download and install modules required for running ultraviolence.py

- Install modules using requirements.txt file downloaded from this repository

```bash
pip install -r requirements.txt
```

- or use pip

```bash
pip install --upgrade google-api-python-client
pip install biopython
pip install aiohttp
pip install pandas
pip install opencv-python
pip install lxml
```

### 4. Edit [frame.py](http://frame.py) file from pandas

- Open [frame.py](http://frame.py) file in prefered text redactor (in this exmple we use gedit)

```bash
gedit venv_research_env/lib/python3.11/site-packages/pandas/core/frame.py
```

- Find lines [635:638] in [frame.py](http://frame.py/) and replace those lines with lines below (or make a comment from those line youself)

```python
#		if index is not None and isinstance(index, set):
#			raise ValueError("index cannot be a set")
#		if columns is not None and isinstance(columns, set):
#			raise ValueError("columns cannot be a set")
```

### 5. Run [ultraviolence.py](http://ultraviolence.py)

```bash
cd Virtual_environment_research/
python3.11 ultraviolence.py
```
