import random
import time
import json

# Simulated constants
SLOTS_PROCESSED = 10
LARGE_TRANSACTION_THRESHOLD = 1000  # SOL
SUSPICIOUS_PROGRAM_IDS = [
    "11111111111111111111111111111111",  # Example: System Program
    "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"  # Example: Token Program
]

# Generate random transaction for simulation
def generate_random_transaction():
    return {
        "slot": random.randint(1000000, 2000000),
        "transaction": {
            "meta": {
                "preBalances": [random.randint(1, 100000) * 10**9],
                "postBalances": [random.randint(1, 100000) * 10**9]
            },
            "instructions": [
                {"programId": random.choice(SUSPICIOUS_PROGRAM_IDS)}
            ]
        }
    }

# Simulate threat detection for Solana blockchain
def simulate_threat_detection():
    threats_detected = []
    for _ in range(SLOTS_PROCESSED):
        transaction = generate_random_transaction()
        pre_balances = transaction["transaction"]["meta"]["preBalances"]
        post_balances = transaction["transaction"]["meta"]["postBalances"]
        for pre, post in zip(pre_balances, post_balances):
            change = (pre - post) / 10**9  # Convert lamports to SOL
            if change >= LARGE_TRANSACTION_THRESHOLD:
                threats_detected.append({
                    "type": "Large Transaction",
                    "slot": transaction["slot"],
                    "amount": change
                })

        for instruction in transaction["transaction"].get("instructions", []):
            if instruction.get("programId") in SUSPICIOUS_PROGRAM_IDS:
                threats_detected.append({
                    "type": "Suspicious Program ID",
                    "slot": transaction["slot"],
                    "program_id": instruction.get("programId")
                })
    return threats_detected

# Simulate newly deployed smart contracts
def simulate_new_contracts():
    new_contracts = []
    for _ in range(random.randint(1, 5)):
        new_contracts.append({
            "address": f"Contract{random.randint(10000, 99999)}",
            "deployed_slot": random.randint(1000000, 2000000)
        })
    return new_contracts

# Main function
def main():
    print("Starting Solana Blockchain Threat Simulation...")

    while True:
        # Simulate detecting threats
        threats = simulate_threat_detection()
        if threats:
            print("\nThreats Detected:")
            print(json.dumps(threats, indent=2))
        else:
            print("No threats detected.")

        # Simulate new contract deployments
        new_contracts = simulate_new_contracts()
        if new_contracts:
            print("\nNewly Deployed Contracts:")
            print(json.dumps(new_contracts, indent=2))

        time.sleep(10)  # Simulate periodic checks

if __name__ == "__main__":
    main()
