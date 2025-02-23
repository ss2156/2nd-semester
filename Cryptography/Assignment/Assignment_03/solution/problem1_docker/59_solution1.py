import socket
import binascii

HOST = "127.0.0.1"  # If running on Docker locally
PORT = 5000         # Ensure this matches your Docker exposed port

def send_command(sock, command):
    """Sends a command and reads the response"""
    sock.sendall(command.encode() + b"\n")
    response = sock.recv(4096).decode().strip()
    print(f"[DEBUG] Server Response: {response}")
    return response

def get_challenge(sock):
    """Fetch the encrypted challenge"""
    response = send_command(sock, "1")
    try:
        return bytes.fromhex(response)
    except ValueError:
        print("[ERROR] Server did not send a valid hex string.")
        return None

def decrypt_challenge(sock, ciphertext):
    """Decrypt the challenge"""
    hex_ct = binascii.hexlify(ciphertext).decode()
    response = send_command(sock, f"2\n{hex_ct}")
    try:
        return bytes.fromhex(response)
    except ValueError:
        print("[ERROR] Failed to decrypt challenge properly.")
        return None

def get_flag(sock, plaintext):
    """Submit the decrypted challenge"""
    hex_pt = binascii.hexlify(plaintext).decode()
    response = send_command(sock, f"3\n{hex_pt}")
    return response

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("[*] Connecting to server...")
        sock.connect((HOST, PORT))
        print("[+] Connected.")

        print("[*] Fetching Challenge...")
        challenge_ct = get_challenge(sock)
        if not challenge_ct:
            print("[ERROR] Challenge retrieval failed.")
            return

        print(f"[+] Received Encrypted Challenge: {challenge_ct.hex()}")

        print("[*] Attempting to Decrypt Challenge...")
        decrypted_challenge = decrypt_challenge(sock, challenge_ct)
        if not decrypted_challenge:
            print("[ERROR] Decryption failed.")
            return

        print(f"[+] Decrypted Challenge: {decrypted_challenge.hex()}")

        print("[*] Submitting Challenge to Get Flag...")
        flag = get_flag(sock, decrypted_challenge)
        print(f"[+] Flag Retrieved: {flag}")

if __name__ == "__main__":
    main()
