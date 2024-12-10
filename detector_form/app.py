from flask 	import Flask, request, jsonify
from tinydb import TinyDB, Query

import re

app = Flask(__name__)
db 	= TinyDB('db.json')

# функция для определения типов поля
def determine_field_type(value):
	# email
	if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
		return 'email'
	# проверка даты
	elif re.match(r'^\d{2}\.\d{2}\.\d{4}$', value) or re.match(r'^\d{4}-\d{2}-\d{2}$', value):
		return 'date'
	# телефон
	elif re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
		return 'phone'
	else:
		return 'text'

@app.route('/get_form', methods=['POST'])
def get_form():
	data = request.form.to_dict()

	# проверка совпадения с шаблонами
	for templates in db.all():
		matches = True
		for field_name, field_type in templates.items():
			if field_name == 'name':
				continue
			if field_name not in data or determine_field_type(data[field_name]) != field_type:
				matches = False
				break
		if matches:
			return jsonify(templates['name'])
		
	# если нет совпадений, вернем тип поля
	result = {field_name: determine_field_type(value) for field_name, value in data.items()}

	return jsonify(result)
	
if __name__ == '__main__':
	app.run(debug=True)