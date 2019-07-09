from flask import Flask, jsonify, request
from multiprocessing import Value

from pylibra import LibraWallet


counter = Value('i', 0)
app = Flask(__name__)

a = []
help_message = """
API Usage:
 
- GET    /api/list
- POST   /api/add data={"key": "value"}
- GET    /api/get/<id>
- PUT    /api/update/<id> data={"key": "value_to_replace"}
- DELETE /api/delete/<id> 

"""

def id_generator():
    with counter.get_lock():
        counter.value += 1
        return counter.value

@app.route('/libra/regenerate', methods=['GET'])
def regenerate():
    wallet1 = LibraWallet()
    assert len(wallet1.to_mnemonic().split()) == 12
    wallet2 = LibraWallet(strength=256)
    assert len(wallet2.to_mnemonic().split()) == 24
    return help_message


@app.route('/libra/regenerate', methods=['POST'])
def index():
    # Create a new random wallet
    wallet1 = LibraWallet()
    print(wallet1.to_mnemonic())

    # Regenerate wallet from an existing Mnemonic
    wallet2 = LibraWallet("student deliver dentist cat gorilla sleep proud naive gown fiber awkward weasel")
    print(wallet2.to_mnemonic())
    return "wallet1 : {} \n wallet2 : {}".format(wallet1, wallet2)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    name = data['name']
    location = data['location']
    print("Hello :{}.\n You are from {}.\n You have submitted the form successfully!".format(name, location))
    return "Hello :{}.\n You are from {}.\n You have submitted the form successfully!".format(name, location)



if __name__ == '__main__':
    # app = connexion.App(__name__, specification_dir='swagger/')
    # app.add_api('sample.yaml')
    app.run(debug=True,port=8080)