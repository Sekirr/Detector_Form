## Установка

1. Клонируйте репозиторий:
git clone <repository-url>
cd detector_form


2. Установите зависимости:
pip install -r requirements.txt


3. Запустите приложение:
python app.py


4. Тестирование
Для тестирования запустите скрипт test.py или введите 


## Использование
curl -X POST -d "user_email=test@example.com&user_phone=+7 123 456 78 90&registration_date=12.12.2022" http://127.0.0.1:5000/get_form
