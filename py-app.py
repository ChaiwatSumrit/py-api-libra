from flask import Flask, jsonify, request

from pylibra import LibraWallet
from pylibra import LibraClient
from pylibra.transaction import TransferTransaction

app = Flask(__name__)


@app.route('/libra/registerAccount', methods=['POST'])
def registerAccount():
        client = LibraClient() # Default client connecting to the official testnet
        wallet = LibraWallet()

        data = request.get_json()
        monny = data['monny']

        account = wallet.get_account(0)
        account = client.mint_with_faucet(account, monny)
        account_state = client.get_account_state(account)
        return {
                "mnemonic":wallet.to_mnemonic(),
                "authenticationKey":account_state.authentication_key,
                "balance":account_state.balance,
                "sequenceNumber":account_state.sequence_number,
                "receivedEventsCount":account_state.received_events_count,
                "sentEventsCount":account_state.sent_events_count
        },201

@app.route('/libra/mintMonnyAccount', methods=['POST'])
def mintMonnyAccount():
        
        data = request.get_json()
        mnemonic = data['mnemonic']
        monny = data['monny']

        client = LibraClient()
        wallet = LibraWallet(mnemonic)
        account = wallet.get_account(0)
        client.mint_with_faucet(account, monny)
        account_state = client.get_account_state(account)

        return {
                "mnemonic":mnemonic,
                "authenticationKey":account_state.authentication_key,
                "balance":account_state.balance,
                "sequenceNumber":account_state.sequence_number,
                "receivedEventsCount":account_state.received_events_count,
                "sentEventsCount":account_state.sent_events_count
        },200


@app.route('/libra/transfer', methods=['POST'])
def transfer():

        data = request.get_json()
        sender = data['sender'] #sender : mnemonic == SK
        receiver = data['receiver'] #receiver hash<hex> : PK
        monny = data['monny'] 

        if monny <= 0  :
                return { 
                        "massage" : "Transfer fail requiry monny >= 1 "
                },400

        #[EX]mnemonic : "zero job file nothing north ask gasp brush yard sand unhappy good"
        client = LibraClient()
       
        sender_wallet = LibraWallet(sender)
        sender_account = sender_wallet.get_account(0)
        sender_account_state = client.get_account_state(sender_account)
        if sender_account_state.balance < monny :
                return {
                        "massage" : "Transfer fail monny to transfer > now balance for wallet",
                        "sender" : sender_account_state.authentication_key,
                        "now_balance" : sender_account_state.balance
                },400

        sender_account = sender_wallet.get_account(0)

        # Create a transfer transaction object to send 0.001 Libra to account2 
        Transaction = TransferTransaction(receiver, monny)
        # Or to send to a plain hex address

        # You can send a transaction by calling `send_transaction` function, which takes a sender `Account` and a `Transaction` object. You can also optionally passed `max_gas_amount`, `gas_unit_price`, and `expiration_time`. 
        client.send_transaction(sender_account, Transaction)
        return { 
                "massage" : "Transfer success",
                "sender" : sender_account_state.authentication_key,
                "receiver" : receiver,
                "monny" : monny
        },201

@app.route('/libra/inquiryBalance', methods=['POST'])
def inquiryBalance():
        # client = LibraClient()
        # wallet = LibraWallet()
        client = LibraClient()
        data = request.get_json()
        
        mnemonic = data["mnemonic"]
        authentication_key = data['authentication_key']

        wallet = LibraWallet(mnemonic)
        account = wallet.get_account(0)
        account_state_by_mnemonic = client.get_account_state(account)

        if account_state_by_mnemonic.authentication_key != authentication_key :
                  return {
                        "massage" : "inquiryBalance fail mnemonic no relational with authentication_key",
                        "mnemonic" : mnemonic,
                        "authentication_key" : authentication_key
                },400

        account_state = client.get_account_state(authentication_key)

        return {
                # "mnemonic":mnemonic,
                "authentication_key":authentication_key,
                "balance":account_state.balance,
                "sequence_number":account_state.sequence_number,
                "received_events_count":account_state.received_events_count,
                "sent_events_count":account_state.sent_events_count
        },200


if __name__ == '__main__':
    # app = connexion.App(__name__, specification_dir='swagger/')
    # app.add_api('sample.yaml')
    app.run(host='3.16.23.43',debug=True,port=8080)