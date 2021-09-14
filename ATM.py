class atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

cardnumberinput = str(input("Enter the card number: "))
cardpin = str(input("Enter the card pin: "))
carddetails = atm(cardnumberinput, cardpin)
carddetails.cardnumber
amount = str(input("Enter the amount you want to Withdraw: "))
print ("You have withdrawn Rupees "+ amount+" from your card with number " +carddetails.cardnumber)