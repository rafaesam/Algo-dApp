# Algo-dApp
In this project we will build end-to-end Web3 decenertalized apps(dApps) on the Algorand Blockchain to generate and distribute Non-Fungible Tokens (NFTs).

# Development Setup
This repo requires Python 3.6 or higher. We recommend you use a Python virtual environment to install the required dependencies.

Set up venv (one time):

* `python3 -m venv venv`

Active venv:
* `. venv/bin/activate` (if your shell is bash/zsh)
* `. venv/Scripts/activate`
* `. venv/bin/activate.fish` (if your shell is fish)

Install dependencies:
* `pip install -r requirements.txt`

Run tests:
* First, start an instance of sandbox (requires Docker):
  `./sandbox up`
* `pytest`
* When finished, the sandbox can be stopped with
  `./sandbox down`
