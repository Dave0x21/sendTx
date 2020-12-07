#!/usr/bin/env python

from web3 import HTTPProvider, Web3, WebsocketProvider

from config import PRIV_KEY, RPC_URL
from parser import create_parser


def check_rpc_url():
    if RPC_URL.startswith('ws'):
        flag = True
        w3 = Web3(WebsocketProvider(RPC_URL))
    elif RPC_URL.startswith('http'):
        flag = True
        w3 = Web3(HTTPProvider(RPC_URL))
    else:
        flag, w3 = False, None
        print('Invalid RPC URL!')
    return flag, w3


def send_tx(w3, args):
    acct = w3.eth.account.privateKeyToAccount(PRIV_KEY)

    print('Creating transaction...')

    tx = dict(
        nonce=w3.eth.getTransactionCount(acct.address),
        gasPrice=args.gasPrice,
        gas=args.gas,
        to=args.toAddress,
        value=w3.toWei(args.ethValue, 'ether'),
        data=b'',)

    print('Signing transaction with your private key')
    signedTx = acct.signTransaction(tx)

    print('Sending transaction, waiting for the recepit...', end='')
    hashTx = w3.eth.sendRawTransaction(signedTx.rawTransaction)

    recepit = w3.eth.waitForTransactionReceipt(hashTx)
    print(' The trasaction recepit is ready!')
    strRecepit = '\n\n\nTransaction Hash:\t{}\nBlock hash:\t\t{}\nBlock number:\t\t{}\nFrom:\t\t\t{}\nTo:\t\t\t{}\nGas used:\t\t{}\nStatus:\t\t\t{}'.format(
        recepit.transactionHash.hex(), recepit.blockHash.hex(), recepit.blockNumber, recepit['from'], recepit.to, recepit.gasUsed, recepit.status)
    print(strRecepit)


if __name__ == '__main__':
    rpc_is_valid, w3 = check_rpc_url()
    args = create_parser(w3)
    if rpc_is_valid:
        send_tx(w3, args)
