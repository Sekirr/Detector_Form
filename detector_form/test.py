import requests 

url = 'http://127.0.0.1:5000/get_form'

test_data = [
	{'user_email': 'test@example.com', 'user_phone': '+7 123 456 78 90', 'registration_date': '01.01.2022'},
	{"name": "Order Form", "lead_email": "email", "order_date": "date", "customer_phone": "phone"},
	{'order_date': '2022-01-01', 'customer_phone': '+7 987 654 32 10', 'lead_email': 'lead@example.com'},
	{'unknown_field': 'some_value'}
]

for data in test_data:
	response = requests.post(url, data=data)
	print(f"Response for {data}: {response.json()}")