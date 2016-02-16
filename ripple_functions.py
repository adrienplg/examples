import json


def getTotalAccountBalances(accountBalances):
    """Get a JSON object as an argument, returns the sum of all balances"""

    # Convert JSON object in Python dictionary object
    accountBalancesDic = json.loads(accountBalances)

    # Check for the existence of the key "balances" in the rpython dictionary object
    if "balances" in accountBalancesDic:
        result = 0
        # Loop through the array of balances
        for b in accountBalancesDic.get("balances"):
            # Add the value to the result after converting it to Float
            result += float(b.get("value"))

        print(result)
        return result

    else:
        raise Exception('Incorrect object format. The expected key "balances" was not found in the request response.')


def getTotalAccountOrders(accountOrders, taker):
    """Returns a dictionary of {currency: totalAmount}. Use taker=taker_gets for the seller perspective and taker=taker_pays for the buyer perspective"""

    while taker not in ('taker_gets', 'taker_pays'):
        taker = input('Please enter "taker_gets" or "taker_pays"')

    # Convert JSON object in Python dictionary object
    accountOrdersDic = json.loads(accountOrders)

    if 'orders' in accountOrdersDic:
        # Initiate empty variables
        result = dict()
        currency = ''

        # Loop through the different orders
        for o in accountOrdersDic.get('orders'):
                currency = o.get(taker).get('currency')
                value = float(o.get(taker).get('value'))

                # Returns the current value in the result dic for the current currency. If the currency is not part of the dic, returns 0
                dictValue = result.get(currency,0.0)
                newDict = {currency: value + dictValue}
                # Insert the updated currency/value in the dictionary
                result.update(newDict)

        #print (result)
        return result

    else:
        raise Exception('Incorrect object format. The expected key "orders" was not found in the request response.')

def conversionRate(dic1, dic2):
    """Print the conversion rate used between 2 objects {currency: amount}"""
    currency1 = dic1.keys()
    #print "key: %s" % currency1[0]
    valueCur1 = dic1.get(currency1[0])
    #print valueCur1
    currency2 = dic2.keys()
    #print "key: %s" % currency1[0]
    valueCur2 = dic2.get(currency2[0])
    #print valueCur2

    value1 = valueCur1 / valueCur2
    print("1 " + currency2[0] + " = " + str(value1) + " " + currency1[0])
    value2 = valueCur2 / valueCur1
    print("1 " + currency1[0] + " = " + str(value2) + " " + currency2[0])

#####################################
## TESTS SECTION
#####################################
#import NativeRippleCommands

from NativeRippleCommands import getAccountBalances, getAccountOrders

#ab = getAccountBalances()
#getTotalAccountBalances(ab)

#getTotalAccountBalances(getAccountBalances(currency='USD'))
#getTotalAccountOrders(getAccountOrders(), 'taker_gets')
#getTotalAccountOrders(getAccountOrders(), 'taker_pays')

conversionRate(getTotalAccountOrders(getAccountOrders(), 'taker_gets'), getTotalAccountOrders(getAccountOrders(), 'taker_pays'))

#ao = getAccountOrders()
#getTotalAccountOrders(ao, taker_gets)
#getTotalAccountOrders(ao, taker_pays)



