import os
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function




# define the function that would check the sum


def luhn_algorithm(cardNum):
    #converts the card number to a list
    cardNum = list(cardNum)
    #reverses the list
    cardNum.reverse()
    # check sum
    def checkSum(cardNum):  
        total = 0
        #gets both the item of the list and the corresponding index
        for index, num in enumerate(cardNum, start=1):
            if index % 2 == 0:
                #gets the last digit from a number if it is greater than 10 
                lastnum = (int(num, 10)*2) % 10
                #allows you get the first digit from a number 
                firstnum = (int(num, 10)*2) // 10
                #the grand total
                total = (total + lastnum + firstnum)
            else:
                total += int(num)
        return total % 10

    validate = checkSum(cardNum)
    # check conditions to know if card is AMEX, MASTERCARD OR VISA
    if validate is 0 and cardNum[-1] == '3' and (cardNum[-2] == '4' or cardNum[-2] == '7') and len(cardNum) == 15:
        return True
    elif validate is 0 and cardNum[-1] == '5' and (cardNum[-2] == '1' or cardNum[-2] == '2' or cardNum[-2] == '3' or cardNum[-2] == '4' or cardNum[-2] == '5') and len(cardNum) == 16:
        return True
    elif validate is 0 and cardNum[-1] == '4' and (len(cardNum) == 13 or len(cardNum) == 16):
        return True
    elif validate is 0 and cardNum[-1] == '5' and cardNum[-2] == '0' and (len(cardNum) == 16 or len(cardNum) == 18) :
        return True
    else:
        return False

#format the transportation price to be in naira 
def naira(amount):
    return f"₦{amount:,.2f}"