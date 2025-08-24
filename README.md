# KGRV

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python пакет для экспериментов и обучения созданию Python пакетов.

## 🎯 Описание

KGRV - это демонстрационный Python пакет, который показывает лучшие практики:
- 📦 Организации структуры Python пакета
- 📚 Документирования кода и API
- 🧪 Написания тестов
- 🚀 Публикации на PyPI
- ⚙️ Настройки инструментов разработки

## ✨ Возможности

- **Класс About** - для отображения информации о разработчике
- **Управление навыками и проектами** - добавление и просмотр
- **CLI интерфейс** - командная строка для взаимодействия
- **Демонстрационные скрипты** - примеры использования
- **Полное покрытие тестами** - unit-тесты для всех компонентов

## 🏗️ Структура проекта

```
kgrv/
├── kgrv/                   # 📦 Основной пакет (для PyPI)
│   ├── __init__.py        # Инициализация и экспорты
│   └── about.py           # Модуль About
├── scripts/               # 🎮 Демонстрационные скрипты
│   ├── demo.py           # Интерактивная демонстрация
│   └── cli.py            # CLI интерфейс
├── docs/                  # 📚 Документация
│   ├── index.md          # Главная страница
│   ├── installation.md   # Инструкции по установке
│   └── api.md           # API документация
├── tests/                 # 🧪 Тесты
│   └── test_about.py     # Тесты для модуля about
├── setup.py              # 🔧 Конфигурация пакета
├── pyproject.toml        # 🔧 Современная конфигурация
└── requirements-dev.txt  # 🛠️ Зависимости для разработки
```

## 🚀 Быстрый старт

### Установка

```bash
# Клонирование репозитория
git clone https://github.com/kogriv/kgrv.git
cd kgrv

# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (Linux/Mac)
source venv/bin/activate

# Установка в режиме разработки
pip install -e .
```

### Использование

#### Python API

```python
from kgrv import About

# Создание объекта
about = About("Ваше имя")

# Вывод информации
about.print_info()

# Добавление навыков
about.add_skill("Python")
about.add_skill("Machine Learning")

# Получение данных
skills = about.get_skills()
info = about.get_info()  # Все данные в JSON формате
```

#### CLI интерфейс

```bash
# Показать информацию
python scripts/cli.py info

# Показать для конкретного пользователя
python scripts/cli.py info --name "John"

# Показать только навыки
python scripts/cli.py skills

# Вывод в JSON
python scripts/cli.py json
```

#### Демонстрация

```bash
# Запуск интерактивной демонстрации
python scripts/demo.py
```

## 🧪 Тестирование

```bash
# Установка зависимостей для разработки
pip install -r requirements-dev.txt

# Запуск тестов
pytest

# Запуск с покрытием
pytest --cov=kgrv --cov-report=html

# Запуск конкретного теста
python -m pytest tests/test_about.py -v
```

## 📦 Публикация на PyPI

```bash
# Сборка пакета
python -m build

# Проверка пакета
twine check dist/*

# Загрузка на Test PyPI
twine upload --repository testpypi dist/*

# Загрузка на PyPI
twine upload dist/*
```

## 🛠️ Разработка

### Настройка окружения

```bash
# Установка зависимостей для разработки
pip install -r requirements-dev.txt

# Установка pre-commit хуков
pre-commit install
```

### Инструменты качества кода

```bash
# Форматирование кода
black kgrv/ scripts/ tests/

# Проверка типов
mypy kgrv/

# Линтинг
flake8 kgrv/ scripts/ tests/
```

## 📚 Документация

Подробная документация доступна в папке [docs/](docs/):
- [Установка и настройка](docs/installation.md)
- [API документация](docs/api.md)
- [Главная страница](docs/index.md)

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.

## 👨‍💻 Автор

**kogriv** - [GitHub](https://github.com/kogriv)

## 🙏 Благодарности

- Python сообществу за отличные инструменты
- Всем, кто делает open source лучше
