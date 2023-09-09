# 1. open new terminal
# 2. install algokit_utils `pip install algokit-utils`
import algokit_utils as algokit

# 3. confirm installation `pip list` (algokit-utils & py-algorand-sdk)
# 4. change directory to session_1 `cd beginner-en/session_1`
# 5. launch VSCode from session_1 directory `code .`
# 6. add imports
# 7. add code below each comment

def main():
    # use new_account() method to generate a new account
    my_account = algokit.Account.new_account()

    # print the address of the account object
    print(my_account.private_key)

main()
