accounts=[]
acc_number=1000
transactions=[]

class Account:      
    def creation(self,name,age,gender,amount):
        global acc_number 
        acc_number +=1
        acc={}
        acc["Account_number"]=acc_number
        acc["name"]=name
        acc["age"]=age
        acc["gender"]=gender
        acc["Amount"]=amount
        accounts.append(acc)
        print()
        print("Your account created successfully..!")


    def view(self,num): 
         for i in range(len(accounts)):
              if num == accounts[i]["Account_number"]:
                   for key,val in accounts[i].items():
                        print(key,": ",val)
                   print()
    
    
    def withdraw(self,num): 
         valid=0
         for i in range(len(accounts)):
            if num == accounts[i]["Account_number"]:
                valid+=1
                amount=int(input("Enter how much amount you want to withdraw: "))
                if accounts[i]["Amount"]>=amount:
                    pre_amount=accounts[i]["Amount"]
                    accounts[i]["Amount"]=accounts[i]["Amount"]-amount
                    print("Sucessfully withdrawed...Present you have {} in your account".format(accounts[i]["Amount"]))
                    transactions.append("Withdrawn satatement...previous amount is {} and present amount is {}".format(pre_amount,accounts[i]["Amount"]))
                    transactions.append(accounts[i]["Account_number"])

                else:
                    print()
                    print("Insufficient balanace...!")

         if valid==0:
                print()
                print("Oops! You do not have account. Please create Now..")
    
    def deposite(self,num): 
        valid=0
        for i in range(len(accounts)):
            if num == accounts[i]["Account_number"]:
                valid+=1
                amount=int(input("Enter how much amount you want to deposite: "))
                pre_amount=accounts[i]["Amount"]
                accounts[i]["Amount"]=accounts[i]["Amount"]+amount
                print("Deposited sucessfully...Present you have {} in your account".format(accounts[i]["Amount"]))
                transactions.append("Deposite satatement...previous amount is {} and present amount is {}".format(pre_amount,accounts[i]["Amount"]))
                transactions.append(accounts[i]["Account_number"])
        if valid==0:
                print()
                print("Oops! You do not have account. Please create Now..")
    
    def transfer(self,num):
        valid=0
        check=0
        for i in range(len(accounts)):
            if num == accounts[i]["Account_number"]:
                valid+=1
                transfering_to=int(input("Enter account number which you want to transfer: "))
                for j in range(len(accounts)):
                    if transfering_to == accounts[j]["Account_number"] and transfering_to!=num:
                         check+=1
                         amount=int(input("Enter how much amount you want to transfer: "))
                         if accounts[j]["Amount"]>=amount:
                              pre_amount1=accounts[i]["Amount"]
                              pre_amount2=accounts[j]["Amount"]
                              accounts[j]["Amount"]=accounts[j]["Amount"]+amount
                              accounts[i]["Amount"]=accounts[i]["Amount"]-amount
                              print("Transfered sucessfully...Present you have {} in your account".format(accounts[i]["Amount"]))
                              transactions.append("Transfered satatement...to {} account, previous amount is {} and present amount is {}".format(accounts[j]["Account_number"],pre_amount1,accounts[i]["Amount"]))
                              transactions.append(accounts[i]["Account_number"])
                              transactions.append("Recieved satatement...from {} account, previous amount is {} and present amount is {}".format(accounts[i]["Account_number"],pre_amount2,accounts[j]["Amount"]))
                              transactions.append(accounts[j]["Account_number"])
                         else:
                              print()
                              print("Insufficient balanace...!")
                if check==0:
                    print()
                    print("Enter a valid account number...Try again..!")

                
        if valid==0:
                print()
                print("Oops! You do not have account. Please create Now..")
     

         
    
    def print_transaction(self,num): 
         for i in range(1,len(transactions),2):
            if num == transactions[i]:
               print("*"*40)
               print(transactions[i-1])
               
          

acc=Account()

while True:
        print("="*40)
        print("1.CREATE ACCOUNT")
        print("2.VIEW ACCOUNT DETAILS BY ACCNO")
        print("3.WITHDRAW")
        print("4.DEPOSIT")
        print("5.FUND TRANSFER")
        print("6.PRINT TRANSACTIONS")
        print("7.EXIT")
        print()
   

        choice=int(input("Enter you choice 1-7: "))
        print()
        if choice == 1:
             name=input("Enter you name: ")
             age=int(input("Enter you age: "))
             gender=input("Enter you gender male/female: ")
             amount=int(input("How much you add in this opening account: "))
             acc.creation(name,age,gender,amount)
          
        if choice == 2:
             num=int(input("Enter you account number: "))
             acc.view(num)

        if choice == 3:
             num=int(input("Enter you account number: "))
             acc.withdraw(num)

        if choice == 4:
            num=int(input("Enter you account number: "))
            acc.deposite(num)

        if choice == 5:
             num=int(input("Enter you account number: "))
             acc.transfer(num)
        if choice == 6:
             num=int(input("Enter you account number: "))
             acc.print_transaction(num)
        if choice == 7:
             break
        


        
