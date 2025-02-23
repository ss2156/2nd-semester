import os
import random
import socket
from Crypto.Cipher import DES3

class Functional_Des:
    def __init__(self):
        self.key = os.urandom(24)
        self.iv = os.urandom(8)
        self.flipped_bits = set(range(0, 192, 8))
        self.challenge = os.urandom(64)
        self.counter = 128

    def get_random_string(self, plain):
        if plain == self.challenge:
            with open("string.txt", "rb") as f:
                FLAG = f.read()
            return FLAG
        return b"Not quite right"

    def get_challenge(self):
        cipher = DES3.new(self.key, mode=DES3.MODE_CBC, iv=self.iv)
        return cipher.encrypt(self.challenge)

    def alter_key(self):
        if len(self.flipped_bits) == 192:
            self.flipped_bits = set(range(0, 192, 8))
        remaining = list(set(range(192)) - self.flipped_bits)
        num_flips = random.randint(1, len(remaining))
        self.flipped_bits = self.flipped_bits.union(
            random.choices(remaining, k=num_flips))
        mask = int.to_bytes(sum(2**i for i in self.flipped_bits), 24, byteorder="big")
        return bytes(i ^ j for i, j in zip(self.key, mask))

    def decrypt(self, text: bytes):
        self.counter -= 1
        if self.counter < 0:
            return b"Out of balance"
        key = self.alter_key()
        if len(text) % 8 != 0:
            return b"Invalid ciphertext"
        cipher = DES3.new(key, mode=DES3.MODE_CBC, iv=self.iv)
        return cipher.decrypt(text)

def handle_client(conn):
    chal = Functional_Des()
    try:
        while True:
            option = conn.recv(1024).strip().decode()
            
            if option == "1":
                # Send only the challenge, no menu text
                conn.sendall(chal.get_challenge().hex().encode() + b"\n")
            elif option == "2":
                conn.sendall(b"(hex) ct: ")
                ct = bytes.fromhex(conn.recv(1024).strip().decode())
                conn.sendall(chal.decrypt(ct).hex().encode() + b"\n")
            elif option == "3":
                conn.sendall(b"(hex) pt: ")
                pt = bytes.fromhex(conn.recv(1024).strip().decode())
                conn.sendall(chal.get_random_string(pt) + b"\n")
                conn.close()
                break
            else:
                conn.sendall(b"Invalid option\n")
    except Exception as e:
        conn.sendall(str(e).encode())
        conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))  # Listen on port 5000
    server.listen(5)
    print("[*] Listening on port 5000")
    while True:
        client, addr = server.accept()
        print(f"[*] Connection from {addr}")
        handle_client(client)

if __name__ == "__main__":
    main()
