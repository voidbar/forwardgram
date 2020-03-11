# forwardgram
Forward messages from multiple Telegram channels or chats to one (or more) chat or channel of your own!

## Prerequisites
- Python 3.6+

## Setup
- `python3 -m pip install -r requirements.txt`.
- Fill out a configuration file. An exmaple file can be found at `config.yml-sample`. 

## Run
`python3 forwardgram.py {YOUR_CONFIG_FILE}`
Please note that in the first time initializing the script, you will be requried to validate your phone number using telegram API. This happens only at the first time (per session name).
