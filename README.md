## Дипломный проект. Задание 3: Веб-приложение

Автотесты для веб-приложения Stellar Burgers (https://stellarburgers.nomoreparties.site/).

## Структура проекта

- endpoints/ - модули с API-запросами
- pages/ - объекты страниц
- tests/ - тесты

## Запуск автотестов

### Установка зависимостей

```bash
$ pip install -r requirements.txt
```

### Запуск тестов

Запустите тесты с помощью pytest:

```bash
pytest --browser [chrome | firefox]
```
например: 

```bash
pytest --browser chrome
```

Запуск автотестов с отчетом Allure

```bash
pytest --browser chrome --alluredir=allure_results
```

Просмотр отчета:

```bash
allure serve allure_results
```