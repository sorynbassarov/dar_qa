# dar_api_automation
## Установить requirements.txt
1. pip install -r requirements.txt
## Запуск API тестов
1. cd tests
2. task test -- test_warehouse.py 
3. Дополнительно: pytest test_warehouse.py -vv --count 10

## dar_gui_automation 
1. cd locust_load 
2. locust -f document_load.py
3. Дополнительно: sudo lsof -i:8089, kill -9 18687
