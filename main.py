from algosdk.v2client import algod
from algosdk import account, mnemonic 
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation 

algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address) 

# CREATE ASSET
Rafaa = account.generate_account()

# Get network params for transactions before every transaction.
params = algod_client.suggested_params()

mnemonic_pharase = "galaxy fantasy exhibit rookie dust right amazing dream danger stumble charge bean almost eyebrow whip diet service elbow cake wage drift cinnamon wet abandon cargo"

Rafaa = {
    "pk": "VDMHB6FOFS24JRWKATOQJDX7B44KN43E2FPM66N73JK3XHDAJADVYX2CAM",
    "sk": mnemonic.to_private_key(mnemonic_pharase) #sk = 'secret key'
}

# Asset Creation transaction
txn = AssetConfigTxn(
    sender=Rafaa['pk'],
    sp=params,
    total=10,
    default_frozen=False,
    unit_name="10x",
    asset_name="10 Academy",
    manager=Rafaa['pk'],
    reserve=Rafaa['pk'],
    freeze=Rafaa['pk'], #put someone on the white or blacklist
    clawback=Rafaa['pk'], 
    url="https://10academy.org", 
    decimals=0)

# Sign with secret key of creator
stxn = txn.sign(Rafaa['sk'])

# Send the transaction to the network and retrieve the txid.
txid = algod_client.send_transaction(stxn)
print("Signed transaction with txID: {}".format(txid))

# Wait for the transaction to be confirmed
confirmed_txn = wait_for_confirmation(algod_client, txid, 4)  
print("TXID: ", txid)
print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))   

if __name__ == "__main__":
    print(algod_client.status())
    print(Rafaa)
    #print(memonic.from_private_key("VDMHB6FOFS24JRWKATOQJDX7B44KN43E2FPM66N73JK3XHDAJADVYX2CAM"))
    # print(mnemonic.from_private_key("sxszP/tqNqEvedPIb1M1g6X8K3VD3/ndQKVbgkMHNsm8Oj5REiUtOp0piNih6h8TvWF0XaOTUvZD17zUTaZbpQ=="))
