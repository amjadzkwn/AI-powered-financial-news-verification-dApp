from blockchain import generate_hash, store_hash_on_stellar

news = "Apple announces new AI financial system for banking industry"

hash_value = generate_hash(news)

print("HASH:", hash_value)

tx_hash = store_hash_on_stellar(hash_value)

print("TRANSACTION:", tx_hash)