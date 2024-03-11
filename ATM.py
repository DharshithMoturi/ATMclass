users=["ram","arun","raju","suresh"]
passwords=["r123","a234","r345","s567"]
amount=[23000,42000,50000,65000]
pin=[482,663,721,801]


Username=input("Enter the username:")
if Username in users:
    index=users.index(Username)
    count=0
    while(count<3):
        Password=input("Enter the password:")
        if Password==passwords[index]:
            for choice in range(1,5):
                print("1.Deposit\n2.Withdraw\n3.Balance Enquiry\n4.Change Password")
                choice=int(input("Enter your choice:"))
                if (choice==1):
                    print("Enter amount to be deposited:")
                    Deposit=int(input())
                    print("Enter the pin:")
                    if(int(input())==pin[index]):
                        amount[index]=amount[index]+Deposit
                        print("Account Balance:",end=" ")
                        print(amount[index])
                    else:
                        print("Incorrect pin.Try Again.")
                    break        
                elif (choice == 2):
                    print("Enter the amount to be withdraw:")
                    Withdraw=int(input())
                    print("Enter the pin:")
                    if(int(input())==pin[index]):
                        if(Withdraw>amount[index]):
                            print("Insufficient balance")
                            break    
                        else:
                            amount[index]=amount[index]-Withdraw       
                            print("Account Balance:",end=" ")
                            print(amount[index])
                            break
                    else:
                        print("Incorrect pin.Try Again.")
                    break           
                elif choice==3:
                    print("The balance amount:")
                    print(amount[index])
                    break
                elif choice==4:
                    a=str(input("Enter your new Password:"))
                    b=str(input("Re-enter your new Password:")) 
                    if(a==b):    
                        passwords[index]=a
                        print("Your password has been changed.")    
                    else:   
                        print("Password doesn't match.Try Again")    
                        print("Do you want to continue?yes/no")
                    break
                else:
                    print("Invalid choice.Try Again.")
            break                                          
        else:
            print("Incorrect password.",2-count,"attempts left")
            count+=1                                   
else:
    print("User not found")                      
    