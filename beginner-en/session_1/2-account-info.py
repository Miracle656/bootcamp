# 1. add imports
import algokit_utils as algokit
from pprint import pprint


# 2. copy/paste code from previous example above the break
# 3. add new code below the break

def main():
    # use new_account() method to generate a new account
    my_account = algokit.Account.new_account()

    # print the address of the account object
    print(my_account.address)

    #####################################################################
    # NEW BELOW
    #####################################################################

    # instatiate algod client on localnet
    algod = algokit.get_algod_client(algokit.get_default_localnet_config('algod'))

    # print the version for algod
    #pprint(algod.versions())

    # get info about my_account from algod
    pprint(algod.account_info(my_account.address))

    # instatiate kmd client on localnet
    kmd = algokit.get_kmd_client_from_algod_client(algod)

    # fund my_account with ALGO from localnet dispenser
    algokit.ensure_funded(
        algod,
        algokit.EnsureBalanceParameters(
            account_to_fund=my_account,
            min_spending_balance_micro_algos=1_000_000 #micro algos
        )
    )

    # again, get info about my_account from algod
    pprint(algod.account_info(my_account.address))


main()
