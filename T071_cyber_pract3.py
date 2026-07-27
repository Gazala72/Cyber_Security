import hmac
import hashlib

# Function to generate MAC
def generate_mac(message, key):
    return hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

# Function to verify MAC
def verify_mac(message, key, received_mac):
    computed_mac = generate_mac(message, key)
    return hmac.compare_digest(computed_mac, received_mac)

# User Input
message = input("Enter the message: ")
key = input("Enter the secret key: ")

# Generate MAC
mac = generate_mac(message, key)

print("\nGenerated MAC:", mac)

# Verification
print("\n--- MAC Verification ---")
received_message = input("Enter the message to verify: ")
received_key = input("Enter the secret key: ")
received_mac = input("Enter the MAC: ")

if verify_mac(received_message, received_key, received_mac):
    print("MAC Verification Successful: Message is authentic.")
else:
    print("MAC Verification Failed: Message has been altered or the key is incorrect.")
