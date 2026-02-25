# MINI-DATA-PIPELINE

**Первый блок - объяснение на русском, второй - на английском. / The first block is an explanation in Russian, and the second is in English.**

# 🇷🇺

Проект демонстрирует следуюшие навыки:
- Работа с файлами
- Работа с JSON (load/dump)
- Запросы к API через requests
- Обработка ошибок и кастомные исключения
- Retry-механизм
- Экспорт в CSV
- Основы ООП
- Разделение слоёв (raw / clean)
- Exit codes

---

## Логика работы
Pipeline выполняет следующие шаги:

1. Загружает конфигурацию из `config.json`
2. Выполняет HTTP-запрос к публичному API
3. Сохраняет сырые данные в `data/raw/*.json`
4. Преобразует данные
5. Сохраняет результат в `data/clean/*.csv`
6. Завершается с корректным exit code

## API

По умолчанию - "https://jsonplaceholder.typicode.com/posts"

Можно поменять в `config.json`

---

## Запуск проекта

### 1. Создание виртуального окружения

```bash
python -m venv .venv
```

### 2. Активация

**WIN:**
```bash
.\.venv\Scripts\activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск

*Запуск производится из корня проекта*
```bash
python -m src.mdpf
```

---

# 🇬🇧

This project demonstrates the following skills:

- File handling
- JSON processing (load/dump)
- API requests using `requests`
- Error handling and custom exceptions
- Retry mechanism
- CSV export
- OOP fundamentals
- Layer separation (raw / clean)
- Exit codes

---

## Pipeline Logic

The pipeline performs the following steps:

1. Loads configuration from `config.json`
2. Sends an HTTP request to a public API
3. Saves raw data to `data/raw/*.json`
4. Transforms the data
5. Saves the result to `data/clean/*.csv`
6. Exits with the appropriate exit code

---

## API

By default:

```
https://jsonplaceholder.typicode.com/posts
```

The endpoint can be changed in `config.json`.

---

## How to Run

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment

**Windows:**
```bash
.\.venv\Scripts\activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

*Run from the project root directory*

```bash
python -m src.mdpf
```