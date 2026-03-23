# Проект: Тестирование API интернет-магазина

## Описание
Проект демонстрирует навыки автоматизации API-тестирования, работы с Docker и настройки CI/CD.  
Тестируется REST API (эндпоинты: товары, корзина, заказы). 

## Технологии
- Python 3.11
- pytest (автотесты)
- requests (HTTP-клиент)
- PostgreSQL (база данных)
- Docker / Docker Compose
- GitHub Actions (CI/CD)

## Как запустить локально
```bash
git clone https://github.com/Venera-h/git_CI-CD.git
cd git_CI-CD
pip install -r requirements.txt
pytest test_main.py -v
