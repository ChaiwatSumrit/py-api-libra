
#!/usr/bin/env python3
# countasync.py

from flask import Flask, jsonify, request

from pylibra import LibraWallet
from pylibra import LibraClient
from pylibra.transaction import TransferTransaction

# import sys
import time
import asyncio
# import aiohttp

app = Flask(__name__)


config_coin = 1000000 #1E micro libra == 1 libra coin
@asyncio.coroutine
@app.route('/createWallet', methods=['POST'])
def createWallet():
        functionName = "[createWallet]"
        print(functionName)
        client =  LibraClient() # Default client connecting to the official testnet
        wallet =  LibraWallet()
        # data = request.get_json()
        # amount = data['amount']

        # yield from asyncio.sleep(5)
        account = "AAAAA"
        print("to_mnemonic : {}".format(wallet.to_mnemonic()))
        print("to_mnemonic : {}".format(wallet.to_mnemonic()))

        print("account: {}".format(account))
        wallet =  LibraWallet(wallet.to_mnemonic())
        account =  wallet.get_account(0)

        print(client.mint_with_faucet(account, 1000000*config_coin)) #1 000 000 lan lan
        account_state = "BBBBBB"

        time.sleep(0.5)
        account_state = client.get_account_state(account)
        print("account_state : {}".format(account_state))
        print("PK : {}".format(account_state.authentication_key))

        result = {
                "mnemonic":wallet.to_mnemonic(),
                "address":account_state.authentication_key,
                "balance":account_state.balance/config_coin,
                "sequenceNumber":account_state.sequence_number,
                "receivedEventsCount":account_state.received_events_count,
                "sentEventsCount":account_state.sent_events_count
        }

        print("result : {}".format(result))
        return result,201

@app.route('/mint', methods=['POST'])
def mint():

        functionName = "[mint]"
        print(functionName)
        
        data = request.get_json()
        # mnemonic = data['mnemonic']
        address = data['address']
        amount = data['amount']

        client = LibraClient()

        # wallet = LibraWallet(mnemonic)
        # account = wallet.get_account(0)
        # account_state = client.get_account_state(address)
        # if account_state.authentication_key != address :
        #         return {
        #                 "massage" : "inquiryBalance fail mnemonic no relational with address",
        #                 "mnemonic" : mnemonic,
        #                 "address" : address
        #         },400

        client.mint_with_faucet(address, amount*config_coin)
        account_state = client.get_account_state(address)


        result = {
                # "mnemonic":mnemonic,
                "address":account_state.authentication_key,
                "balance":account_state.balance/config_coin,
                "sequenceNumber":account_state.sequence_number,
                "receivedEventsCount":account_state.received_events_count,
                "sentEventsCount":account_state.sent_events_count
        }

        print("result : {}".format(result))
        return result,200


@app.route('/transfer', methods=['POST'])
def transfer():

        functionName = "[transfer]"
        print(functionName)

        data = request.get_json()
        sender = data['mnemonic'] #sender : mnemonic == SK
        receiver = data['toAddress'] #receiver hash<hex> : PK
        amount = int(data['amount'])*config_coin

        if amount <= 0  :
                return { 
                        "massage" : "Transfer fail requiry amount >= 1 "
                },400

        #[EX]mnemonic : "zero job file nothing north ask gasp brush yard sand unhappy good"
        client = LibraClient()
       
        sender_wallet = LibraWallet(sender)
        sender_account = sender_wallet.get_account(0)
        sender_account_state = client.get_account_state(sender_account)
        if sender_account_state.balance < amount :
                return {
                        "massage" : "Transfer fail amount to transfer > now balance for wallet",
                        "sender" : sender_account_state.authentication_key,
                        "now_balance" : sender_account_state.balance
                },400

        sender_account = sender_wallet.get_account(0)

        # Create a transfer transaction object to send 0.001 Libra to account2 
        Transaction = TransferTransaction(receiver, amount)
        # Or to send to a plain hex address

        # You can send a transaction by calling `send_transaction` function, which takes a sender `Account` and a `Transaction` object. You can also optionally passed `max_gas_amount`, `gas_unit_price`, and `expiration_time`. 
        client.send_transaction(sender_account, Transaction)
        result =  { 
                "massage" : "Transfer success",
                "sender" : sender_account_state.authentication_key,
                "receiver" : receiver,
                "amount" : amount/config_coin
        }

        print("result : {}".format(result))
        return result,201

@app.route('/getBalance', methods=['POST'])
def getBalance():

        functionName = "[getBalance]"
        print(functionName)
     
        client = LibraClient()
        data = request.get_json()

        mnemonic = data["mnemonic"]
        address = data['address']
        # wallet.to_mnemonic(),
        wallet = LibraWallet(mnemonic)
        # try :
        # wallet = LibraWallet(mnemonic)
        # except TypeError as error :
        #         print("Error : {}".format(error))
        #         return { "error" : error },400

        account = wallet.get_account(0)
        account_state_by_mnemonic = client.get_account_state(account)
        print(account_state_by_mnemonic)
        if account_state_by_mnemonic.authentication_key != address :
                  return {
                        "massage" : "inquiryBalance fail mnemonic no relational with address",
                        "mnemonic" : mnemonic,
                        "address" : address
                },400

        account_state = client.get_account_state(address)

        result = {
                "mnemonic":mnemonic,
                "address":address,
                "balance":account_state.balance/config_coin,
                "sequence_number":account_state.sequence_number,
                "received_events_count":account_state.received_events_count,
                "sent_events_count":account_state.sent_events_count
        }

        print("result : {}".format(result))
        return result,200


@app.route('/getBalanceByMnemonic', methods=['POST'])
def getBalanceByMnemonic():

        functionName = "[getBalanceByMnemonic]"
        print(functionName)
     
        client = LibraClient()
        data = request.get_json()

        mnemonic = data["mnemonic"]
        # wallet.to_mnemonic(),
        wallet = LibraWallet(mnemonic)
        # try :
        # wallet = LibraWallet(mnemonic)
        # except TypeError as error :
        #         print("Error : {}".format(error))
        #         return { "error" : error },400

        account = wallet.get_account(0)
        account_state_by_mnemonic = client.get_account_state(account)
        print(account_state_by_mnemonic)

        result = {
                "mnemonic":mnemonic,
                "address":account_state_by_mnemonic.authentication_key,
                "balance":account_state_by_mnemonic.balance/config_coin,
                "sequence_number":account_state_by_mnemonic.sequence_number,
                "received_events_count":account_state_by_mnemonic.received_events_count,
                "sent_events_count":account_state_by_mnemonic.sent_events_count
        }

        print("result : {}".format(result))
        return result,200



if __name__ == '__main__':
    # app = connexion.App(__name__, specification_dir='swagger/')
    # app.add_api('sample.yaml')
    app.run(host='0.0.0.0',debug=True,port=3000)