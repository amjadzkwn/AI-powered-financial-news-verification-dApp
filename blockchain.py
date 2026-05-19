from stellar_sdk import Server, Keypair, TransactionBuilder, Network
import hashlib
import os
from test_blockchain import hash_value

# Stellar Testnet
server = Server("https://horizon-testnet.stellar.org")

# Replace with YOUR secret key
SECRET_KEY = os.getenv("STELLAR_SECRET_KEY")

keypair = Keypair.from_secret(SECRET_KEY)
public_key = keypair.public_key


# =========================
# Generate SHA256 Hash
# =========================
def generate_hash(news_text):

    return hashlib.sha256(news_text.encode()).hexdigest()


# =========================
# Store Hash on Blockchain
# =========================
def store_hash_on_stellar(news_hash):

    source_account = server.load_account(public_key)

    transaction = (
        TransactionBuilder(
            source_account=source_account,
            network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
            base_fee=100
        )
        .append_manage_data_op(
            data_name=f"news_{hash_value[:10]}",
            data_value=news_hash[:64]
        )
        .set_timeout(30)
        .build()
    )

    transaction.sign(keypair)

    response = server.submit_transaction(transaction)

    return response["hash"]