# 1. add imports
import algokit_utils as algokit
from pprint import pprint

# 2. copy/paste code from previous example above the break
# 3. add new code below the break

def main():
    # instatiate algod client on localnet
    algod = algokit.get_algod_client(algokit.get_default_localnet_config('algod'))

    # instatiate kmd client on localnet
    kmd = algokit.get_kmd_client_from_algod_client(algod)

    # create my_account
    my_account = algokit.Account.new_account()

    # get info about my_account from algod
    pprint(algod.account_info(my_account.address))

    # fund my_account with ALGO from localnet dispenser
    algokit.ensure_funded(
        algod,
        algokit.EnsureBalanceParameters(
            account_to_fund=my_account,
            min_spending_balance_micro_algos=1_000_000 #micro algos
        )
    )

    # set localnet default account from KMD as other_account
    other_account = algokit.get_localnet_default_account(algod)
    pprint(algod.account_info(other_account.address))


    # send 1 algo from my_account to other_account
    txn = algokit.transfer(algod, algokit.TransferParameters(
        from_account=other_account.signer,
        to_address=my_account.address,
        micro_algos=1_000_000
    ))

    # again, get info about my_account from algod
    pprint(algod.account_info(my_account.address))
    pprint(algod.account_info(other_account.address))
 
main()
