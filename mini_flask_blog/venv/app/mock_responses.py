from string import digits
from random import choice
from datetime import datetime
from datetime import timedelta
from random import randint


if __name__ == '__main__':

	for i in range(10):

		transaction_identity =int(str(b) + str(math.floor(time())))
		time_of_tansaction = datetime.now().strftime('%d/%m/%Y %I:%M:%S %p')
		amount_paid = '{:.2f}'.format(randint(100, 999))
		tax_paid = '{:.2f}'.format(randint(10, 99))
		pin_numbers = '-'.join([str(randint(1000, 9999)) for i in range(5)])
		units_number = '{:.2f}'.format(randint(10, 99))
		paid_debt = '{:.1f}'.format(randint(1, 9))
		tax_debt = '{:.1f}'.format(randint(1, 9))
		amount_fixed = '{:.1f}'.format(randint(1, 9))
		tax_fixed = '{:.1f}'.format(randint(1, 9))
		remaining_debt = '{:.1f}'.format(randint(1, 9))
		debt_description =
		some_days_ago = datetime.now() + timedelta(randint(5, 30))
		the_last_vend_date = some_days_ago.strftime('%d/%m/%Y %I:%M:%S %p')

		PREPAID_PAYMENT_RESPONSE ={
		    "transaction_id": transaction_identity,
		    "vend_time": time_of_tansaction,
		    "meter_class": "SINGLE PHASE RESIDENTIAL (R2)",
		    "retailer": "Tech Advance",
		    "charge": {
		        "debt_paid": paid_debt,
		        "debt_tax": tax_debt,
		        "fixed_amount": amount_fixed,
		        "fixed_tax":tax_fixed,
		        "debt_remaining": remaining_debt,
		        "debt_desc": None,
		        "fixed_desc": "Last Vend Date": the_last_vend_date },
		    "token": {
		        "tariff": "32.0 KWh @ 29.81 N/KWh:  :  : ",
		        "amount": amount_paid,
		        "tax": tax_paid,
		        "units": units_number,
		        "pin": pin_numbers,
		    "code": 100,
		    "message": "SUCCESSFUL",
		    "time": time_of_tansaction
		}

		print(PREPAID_PAYMENT_RESPONSE)
