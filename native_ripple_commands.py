import requests

def generateWallet():
    r = requests.get('https://api.ripple.com/v1/wallet/new')

    # Raise an error if the request response contain an error status code
    r.raise_for_status()

    return r.text




# Returns the JSON object if the status code is OK
def getAccountBalances(currency='MXN', account='rG6FZ31hDHN1K5Dkbma3PSB5uVCuVVRzfn'):
    """Default currency used is MXN, default account is rG6FZ31hDHN1K5Dkbma3PSB5uVCuVVRzfn"""

    # Parameter directly in the URL
    #r = requests.get('https://api.ripple.com/v1/accounts/rG6FZ31hDHN1K5Dkbma3PSB5uVCuVVRzfn/balances?currency=MXN')
    c = currency
    # Parameter passed as an argument
    payload = {'currency': c}
    r = requests.get('https://api.ripple.com/v1/accounts/' + account + '/balances', params=payload)

    # Raise an error if the request response contain an error status code
    r.raise_for_status()

    return r.text




def getAccountSettings(account='rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn'):
    """Default account is rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn"""

    r = requests.get('https://api.ripple.com/v1/accounts/' + account + '/settings')

    # Raise an error if the request response contain an error status code
    r.raise_for_status()

    #print r.text
    return r.text




def getAccountOrders(account='rJnZ4YHCUsHvQu7R6mZohevKJDHFzVD6Zr', ledger='10399192', limit='15'):
    """Retrieve orders"""

    rparams = {'ledger': ledger, 'limit': limit}

    #r = requests.get('https://api.ripple.com/v1/accounts/' + account + '/orders', params=rparams)
    r = requests.get('https://api.ripple.com/v1/accounts/rJnZ4YHCUsHvQu7R6mZohevKJDHFzVD6Zr/orders', params=rparams)

    # Raise an error if the request response contain an error status code
    r.raise_for_status()

    #print r.text
    return r.text




def preparePayment(sourceAccount='rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn', destinationAccount='ra5nK24KXen9AHvsdFTKHSANinZseWnPcX', currency='USD', amount='1'):

    urlLastPart = amount + '+' + currency + '+' + sourceAccount

    r = requests.get('https://api.ripple.com/v1/accounts/' + sourceAccount + '/payments/paths/' + destinationAccount + '/' + urlLastPart, params=urlLastPart)

    # Raise an error if the request response contain an error status code
    r.raise_for_status()

    #print r.text
    return r.text



#getAccountOrders()
#getAccountSettings()
#print ('-------------')
#preparePayment()
