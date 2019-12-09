from project import User
from project import Transactions

class Main:

    # keep track of all the accounts
    accounts = []
    print("Welcome to New Age Banking")

    # User 1 prompts
    user1_username = input("Enter a username: ")
    user1_investment = input("Enter your initial deposit: ")
    user1 = User.User(user1_username,int(user1_investment))
    accounts.append(user1)

    # User 2 prompts
    print("Hello User 2! Let's get started, please follow the instructions bellow - ")
    user2_username = input("Enter a username: ")
    user2_investment = input("Enter your initial deposit: [only enter NUMBERS] ")
    user2 = User.User(user2_username,int(user2_investment))
    accounts.append(user2)
    #False: if session is active True: session inactive
    session_satus = False

    # Creating the Sending BlockChain
    s_transactionChain = Transactions.TransactionChain()

    # Creating the Request BlockChain
    r_transactionChain = Transactions.TransactionChain()

    while session_satus == False:
        # Finding the sending user from array of users, we could use hashtable for O(1) lookup speed
        #sending_user = None

        chosen_user = input("Please enter your username: ")
        for i in accounts:
            if chosen_user == i.getaccountname():
                    selectednumber = i.getlinenumber()

        chosen_dst = input("Who are you working with? ")
        if chosen_user != chosen_dst:
            for i in accounts:
                if chosen_dst == i.getaccountname():
                    selecteddstnumber = i.getlinenumber()

        transactionselection = input("What would you like to do? Send[0] Request[1] ")

        if transactionselection == "0":
            send_amount = input("How much do you want to send? [only enter NUMBERS] ")
            if int(send_amount):
                current_transactionid = str(accounts[selectednumber])+str(send_amount) + str(accounts[selecteddstnumber])
                transaction = Transactions.Transaction(current_transactionid)
                print("Approval pending...")
                s_transactionChain.mine(transaction)
                if transaction.getapproval() == 1:
                    print("Transaction as been approved!")
                    accounts[selecteddstnumber].receivemoney(accounts[selectednumber].sendmoney(send_amount))
                    for i in accounts:
                        print(str(i.getaccountname()) + ": Balance = " + str(i.getbalance()))
                else:
                    print("Your transaction was not approved!")


        elif transactionselection == "1":
            request_amount = input("How much do you want to request ")

            if int(request_amount):
                dst_approval = input(accounts[selecteddstnumber].getaccountname()+", Do you agree? [Y/N]")
                if dst_approval == "Y":
                    current_transactionid = str(accounts[selectednumber])+str(send_amount) + str(accounts[selecteddstnumber])
                    transaction = Transactions.Transaction(current_transactionid)
                    print("Approval pending...")
                    r_transactionChain.mine(transaction)

                    if transaction.getapproval() == 1:
                        print("Transaction as been approved!")
                        accounts[selectednumber].receivemoney(accounts[selecteddstnumber].sendmoney(request_amount))
                        for i in accounts:
                            print(str(i.getaccountname()) + ": Balance = " + str(i.getbalance()))
                    else:
                        print("Your transaction was not approved!")

                else:
                    print("Your transaction was not approved!")


        status = input("Is that all for this session? [Y/N] ")
        if status == "Y":
            session_satus = True
            print("Thank you for working with New Age Banking, come back soon!")
            print("Here are your chains:")
            print("Sending Chain: ")
            while s_transactionChain.head != None:
                print(s_transactionChain.head)
                s_transactionChain.head = s_transactionChain.head.next
            print("Request Chain: ")
            while r_transactionChain.head != None:
                print(r_transactionChain.head)
                r_transactionChain.head = r_transactionChain.head.next
            SystemExit
        else:
            session_satus = False
