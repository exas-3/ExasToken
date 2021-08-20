from brownie import accounts, config, TokenERC20

initial_supply = 100000000000000000000 #100
token_name = "Exas"
token_symbol = "EXA"

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}
    )
