# sendTx

Send ETH from command line

### How to start

- Clone this repo

  `git clone https://github.com/Dave0x21/sendTx.git`

- Move inside the repo directory

  `cd sendTx`

- Create a virtual env

  `python3 -m venv env`

- Use your virtual env

  `source env/bin/activate`

- Install requirements

  `pip install -r requirements.txt`

### How to use

Frist of all, modify _config.py_, insert your private key in **PRIV_KEY** and an url for connecting to the network in **RPC_URL**, the rpc url can be either _websocket_ (ws, wss) or http.

###### Example

**config.py**

> PRIV_KEY = '0x7400921efaf63382984b72d980341fc815d435814aec1728f2c2fb103d555260'
>
> RPC_URL = 'wss://mainnet.infura.io/ws/v3/<PROJECT_ID>'

###### Basic Usage

`./sendTx recivingAddress ETH`

Where:

- _recivingAddress_ is the address where to send your ETH
- _ETH_ is the ammount to send in ether

###### Example

`./sendTx recivingAddress 0xd3823daae102A9E8663CAE63D3574cC27E7d9726 0.1`

This will send **0.1 ETH** from your address to **0xd3823daae102A9E8663CAE63D3574cC27E7d9726**, _gas price_ is read from the network and the _gas_ amount used is, by default, 12000

###### Customize gas and gas price

`./sendTx recivingAddress 0xd3823daae102A9E8663CAE63D3574cC27E7d9726 0.1 --gas 40000`

This will send **0.1 ETH** from your address to **0xd3823daae102A9E8663CAE63D3574cC27E7d9726**, max _gas_ amount is 40000 and _gas price_ is read from the network

`./sendTx recivingAddress 0xd3823daae102A9E8663CAE63D3574cC27E7d9726 0.1 --gasprice 29000000000`

This will send **0.1 ETH** from your address to **0xd3823daae102A9E8663CAE63D3574cC27E7d9726**, _gas price_ is 29000000000 WEI and the _gas_ amount used is, by default, 12000

`./sendTx recivingAddress 0xd3823daae102A9E8663CAE63D3574cC27E7d9726 0.1 --gasprice 29000000000 --gas 40000`

This will send **0.1 ETH** from your address to **0xd3823daae102A9E8663CAE63D3574cC27E7d9726**, _gas price_ is 29000000000 WEI and max _gas_ amount is 40000
