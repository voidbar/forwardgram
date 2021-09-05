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

## Run as daemon
Run script locally to sign in to Telegram application. File `forwardgram.session` should be created in local folder. This step is crucial, since daemon will not be able to sign in interactively. 

All code beyond specific to Azure Linux instances - AWS and other hosters will have different default user and different folders.

Sign in to VM and create folder `forwardgram` in default user folder (run remotely)

`mkdir forwardgram`

Copy files from local machine to VM (run locally)

`scp -i <path to pem file> * azureuser@<VM IP>:/home/azureuser/forwardgram`

Copy `forwardgram.service` to `/etc/systemd/system` (run remotely)

`cp forwardgram.service /etc/systemd/system/forwardgram.service`

Reload daemon (run remotely)

`sudo systemctl daemon-reload`

Enable our service (run remotely)

`sudo systemctl enable forwardgram.service`

Start our service (run remotely)

`sudo systemctl start forwardgram.service`

Now you can check service status (run remotely)

`sudo systemctl status forwardgram.service`

or inspect logs (run remotely)

`sudo journalctl -u forwardgram.service -n 50 --no-pager`