from aiohttp import TraceDnsCacheHitParams
from brownie import accounts, SimpleStorage, config, network

def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    # account = accounts.load("pk-account")
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    Updated_stored_value = simple_storage.retrieve()
    print(Updated_stored_value)

def main():
    deploy_simple_storage()

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
