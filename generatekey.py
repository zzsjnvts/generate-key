import random
import string

def generate_serial_key(length=16):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    serial_key = ''.join(random.choice(characters) for _ in range(length))
    return serial_key + "-aesthetic"

# Generate 20 serial keys with "-aesthetic" at the end
for _ in range(20):
    serial_key = generate_serial_key()
    print(serial_key)
