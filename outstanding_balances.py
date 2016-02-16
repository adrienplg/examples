#
# OutstandingBalances.py
#
# @author: Adrien Pouligny, 02/24/2015, technical assignment for Ripple Labs
#
# Prints the sum of all Bitso balances in MXN currency
#

import requests, json

print "hello"

# Parameter directly in the URL
#r = requests.get('https://api.ripple.com/v1/accounts/rG6FZ31hDHN1K5Dkbma3PSB5uVCuVVRzfn/balances?currency=MXN')

# Parameter passed as an argument
payload = {'currency': 'MXN'}
r = requests.get('https://api.ripple.com/v1/accounts/rG6FZ31hDHN1K5Dkbma3PSB5uVCuVVRzfn/balances', params=payload)

# TEST the "Incorrect object format" exception.
#r = requests.get('https://api.ripple.com/v1/wallet/new')

# Raise an error if the request response contain an error status code
r.raise_for_status()

# Convert JSON object in Python dictionary object
rpython = json.loads(r.text)

# Check for the existence of the key "balances" in the rpython dictionary object
if "balances" in rpython:
	result = 0
	# Loop through the array of balances
	for b in rpython.get("balances"):
		# Add the value to the result after converting it to Float
		result += float(b.get("value"))

	print (result)

else:
	raise Exception('Incorrect object format. The expected key "balances" was not found in the request response.')

exit()
