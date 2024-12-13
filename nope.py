import gmpy2
import hashlib

# Example function that tries to find the valid nonce (proof of work)
def solve_pow(challenge_string, difficulty):
    for i in range(1000000):  # Adjust this range as needed
        test_string = f"{challenge_string}{i}"
        hashed = hashlib.sha256(test_string.encode()).hexdigest()
        
        # Example condition (check for leading zeros or any other PoW condition)
        if hashed.startswith("0000"):  # Change the condition based on difficulty
            print(f"Found solution: {test_string}")
            print(f"Hash: {hashed}")
            break

# Example usage
challenge = "s.ACcQ.AAAWFevRT4AGFKDFvcfIyE5U"
difficulty = 1337
solve_pow(challenge, difficulty)
