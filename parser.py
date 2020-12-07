import argparse


def create_parser(w3):
    parser = argparse.ArgumentParser(
        description='Send ETH to another address.')
    parser.add_argument('toAddress', metavar='recivingAddress',
                        type=str, help='The reciving address')
    parser.add_argument('ethValue', metavar='ETH',
                        type=float, help='The ammount to send in ETH')
    parser.add_argument('--gas', metavar='gas', dest='gas', default=21000,
                        type=int, help='The maximum value of gas to use [default 21000]')
    parser.add_argument('--gasprice', metavar='gasPrice', dest='gasPrice', 
                        default=w3.eth.gasPrice if w3 else 0, type=int, help='Gas price in WEI [default is taken from network]')
    args = parser.parse_args()
    return args
