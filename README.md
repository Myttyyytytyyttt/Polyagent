<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/polymarket/agents">
    <img src="public/0110(1)/0110(1).gif" alt="banner" width="466" height="262">
  </a>

<h3 align="center">PolyAgent</h3>

  <p align="center">
    Trade autonomously on Polymarket using AI Agents
    <br />
    <a href="https://twitter.com/BabaVanga_ai"><strong>Twitter »</strong></a>
  </p>
</div>


<!-- CONTENT -->
# PolyAgent

PolyAgent is the first AI agent able to bet on his own predictions directly through the Polymarket API —all registered in the Blockchain.


## Features ⚙️

- Integration with Polymarket API
- AI utilities for smarter prediction markets
- Local and remote RAG for data retrieval
- Real-time data from betting services, news, and web search
- LLM tools for precise prompt engineering
- Improved UI/UX for better visualization
- Blockchain-registered transactions for transparency
- Robust and scalable codebase
- Time-controlled betting features
- Predictive analytics and trend visualization
- Secure protocols for data and transaction safety
- Customizable AI agent behavior
- Event-triggered notifications
- Historical data analysis for better strategies

More to come...

## Future features 🛠️

- Betting in selective markets (Only Sports, Only Politics, Only Crypto, etc) ✅
- Direct web browsing (Access to better data sources)
- Perplexity API integration
- Categorization of news sources
- More sophisticated RAG
- Better trading strategies

# Getting started 🚀

This repo is inteded for use with Python 3.9

1. Clone the repository

   ```
   git clone https://github.com/{username}/Polyagent.git
   cd Polyagent
   ```

2. Create the virtual environment

   ```
   virtualenv --python=python3.9 .venv
   ```

3. Activate the virtual environment

   - On Windows:

   ```
   .venv\Scripts\activate
   ```

   - On macOS and Linux:

   ```
   source .venv/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   - (In case of error, try: pip cache purge && pip install -r requirements.txt --no-cache-dir)

   +++

   ```
5. Set up your environment variables:

   - Create a `.env` file in the project root directory

   ```
   cp .env.example .env
   ```

   - Add the following environment variables:

   ```
   POLYGON_WALLET_PRIVATE_KEY=""
   OPENAI_API_KEY=""
   TAVILY_API_KEY=""
   NEWSAPI_API_KEY=""
   export PYTHONPATH="."
   DRY_RUN=
   ANALYSIS_DELAY_SECONDS= #Default is 30secs
   MARKET_CATEGORY="all"  # Options: all, sports, politics, crypto, entertainment, tech
   ```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download spaCy model:
```bash
python -m spacy download en_core_web_sm
```

3. Configure environment variables:
...

4. Load your wallet with USDC.

5. Try the command line interface...

   ```
   python scripts/python/cli.py
   ```

   Or just go trade! 

   ```
   python agents/application/trade.py
   ```

6. Note: If running the command outside of docker, please set the following env var:

   ```
   export PYTHONPATH="."
   ```

   If running with docker is preferred, we provide the following scripts:

   ```
   ./scripts/bash/build-docker.sh
   ./scripts/bash/run-docker-dev.sh
   ```

## Common issues

1. OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be
a Python package or a valid path to a data directory.
```bash
python -m spacy download en_core_web_sm
-
self.nlp = spacy.load("en_core_web_sm") OR python -m spacy download en_core_web_sm
```

## Architecture 📚

The Polyagent architecture features modular components that can be maintained and extended by individual community members.

### APIs 🌐

Polyagent connectors standardize data sources and order types.

- `Chroma.py`: chroma DB for vectorizing news sources and other API data. Developers are able to add their own vector database implementations.

- `Gamma.py`: defines `GammaMarketClient` class, which interfaces with the Polymarket Gamma API to fetch and parse market and event metadata. Methods to retrieve current and tradable markets, as well as defined information on specific markets and events.

- `Polymarket.py`: defines a Polymarket class that interacts with the Polymarket API to retrieve and manage market and event data, and to execute orders on the Polymarket DEX. It includes methods for API key initialization, market and event data retrieval, and trade execution. The file also provides utility functions for building and signing orders, as well as examples for testing API interactions.

- `Objects.py`: data models using Pydantic; representations for trades, markets, events, and related entities.

### Scripts 📜

Files for managing your local environment, server set-up to run the application remotely, and cli for end-user commands.

`cli.py` is the primary user interface for the repo. Users can run various commands to interact with the Polymarket API, retrieve relevant news articles, query local data, send data/prompts to LLMs, and execute trades in Polymarkets.

Commands should follow this format:

`python scripts/python/cli.py command_name [attribute value] [attribute value]`

Example:

`get-all-markets`
Retrieve and display a list of markets from Polymarket, sorted by volume.

   ```
   python scripts/python/cli.py get-all-markets --limit <LIMIT> --sort-by <SORT_BY>
   ```

- limit: The number of markets to retrieve (default: 5).
- sort_by: The sorting criterion, either volume (default) or another valid attribute.

# Prediction markets reading 📚

- Prediction Markets: Bottlenecks and the Next Major Unlocks, Mikey 0x: https://mirror.xyz/1kx.eth/jnQhA56Kx9p3RODKiGzqzHGGEODpbskivUUNdd7hwh0
- The promise and challenges of crypto + AI applications, Vitalik Buterin: https://vitalik.eth.limo/general/2024/01/30/cryptoai.html
- Superforecasting: How to Upgrade Your Company's Judgement, Schoemaker and Tetlock: https://hbr.org/2016/05/superforecasting-how-to-upgrade-your-companys-judgment
- The Future of Prediction Markets, Mikey 0x: https://mirror.xyz/1kx.eth/jnQhA56Kx9p3RODKiGzqzHGGEODpbskivUUNdd7hwh0
