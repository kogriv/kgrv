# Руководство по публикации Python пакета на PyPI

Пошаговое руководство по подготовке и публикации Python пакета на PyPI на примере пакета KGRV.

## 📋 Требования к структуре пакета

### Обязательные файлы

1. **Основной пакет** - папка с кодом:
   ```
   kgrv/
   ├── __init__.py      # Версия, метаданные, экспорты
   ├── about.py         # Основной функционал
   └── cli_click.py     # CLI интерфейс
   ```

2. **Конфигурационные файлы**:
   ```
   setup.py            # Конфигурация пакета
   pyproject.toml       # Современная конфигурация
   MANIFEST.in          # Файлы для включения в дистрибутив
   ```

3. **Документация**:
   ```
   README.md            # Описание проекта
   LICENSE              # Лицензия (обязательно!)
   CHANGELOG.md         # История изменений
   ```

4. **Зависимости**:
   ```
   requirements.txt     # Основные зависимости
   ```

5. **Исключения**:
   ```
   .gitignore          # Временные файлы для Git
   ```

### Структура __init__.py

```python
"""Описание пакета"""

__version__ = "0.1.0"           # Версия (обязательно!)
__author__ = "Your Name"        # Автор
__email__ = "email@example.com" # Email
__description__ = "Краткое описание"

# Экспорты
from .module import Class
__all__ = ['Class']
```

### Конфигурация setup.py

```python
from setuptools import setup, find_packages

setup(
    name="your-package-name",           # Уникальное имя на PyPI
    version="0.1.0",                    # Версия
    author="Your Name",                 # Автор
    author_email="email@example.com",   # Email
    description="Краткое описание",     # Краткое описание
    long_description=read_readme(),     # Полное описание из README
    long_description_content_type="text/markdown",
    url="https://github.com/user/repo", # URL репозитория
    
    # Пакеты для включения
    packages=find_packages(exclude=["tests*", "scripts*"]),
    
    # Зависимости
    install_requires=[
        "click>=8.0.0",
        "requests>=2.25.0",
    ],
    
    # Опциональные зависимости
    extras_require={
        "dev": ["pytest>=6.0.0"],
    },
    
    # Поддерживаемые версии Python
    python_requires=">=3.7",
    
    # Классификаторы
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    
    # CLI команды
    entry_points={
        "console_scripts": [
            "your-command=your_package.cli:main",
        ],
    },
)
```

### ⚠️ **КРИТИЧЕСКИ ВАЖНО: Синхронизация setup.py и pyproject.toml**

При использовании обоих файлов конфигурации **ОБЯЗАТЕЛЬНО** поддерживайте их синхронизацию!

#### **Проблема:**
- `setup.py` и `pyproject.toml` могут содержать **разные настройки**
- При сборке используется **только один из них** (обычно `pyproject.toml`)
- Несоответствие приводит к **неправильной сборке пакета**

#### **Примеры конфликтов:**

**1. Разные зависимости:**
```python
# setup.py
install_requires = ["click>=8.0.0", "requests>=2.25.0"]
```

```toml
# pyproject.toml - КОНФЛИКТ!
dependencies = []  # Пустые зависимости!
```

**2. Разные entry points:**
```python
# setup.py
entry_points = {
    "console_scripts": ["kgrv=kgrv.cli_click:cli"]
}
```

```toml
# pyproject.toml - КОНФЛИКТ!
[project.scripts]
kgrv-cli = "scripts.cli:main"  # Старый путь!
```

#### **Рекомендации:**

**Вариант 1: Использовать только pyproject.toml (рекомендуется)**
```toml
[project]
name = "kgrv"
version = "0.1.0"
dependencies = [
    "click>=8.0.0",
    "colorama>=0.4.0",
    "requests>=2.25.0",
]

[project.scripts]
kgrv = "kgrv.cli_click:cli"
```

**Вариант 2: Использовать только setup.py**
```python
setup(
    name="kgrv",
    version="0.1.0",
    install_requires=[
        "click>=8.0.0",
        "colorama>=0.4.0", 
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": ["kgrv=kgrv.cli_click:cli"],
    },
)
```

**Вариант 3: Синхронизировать оба файла**
- Всегда обновляйте **оба файла** при изменении конфигурации
- Используйте **одинаковые значения** для зависимостей, entry points, метаданных
- Регулярно **проверяйте соответствие** перед сборкой

#### **Чек-лист синхронизации:**
- [ ] Имя пакета одинаковое
- [ ] Версия одинаковая
- [ ] Зависимости идентичны
- [ ] Entry points соответствуют
- [ ] Классификаторы совпадают
- [ ] Автор и email одинаковые

#### **Проверка синхронизации:**
```bash
# Проверьте, что сборка использует правильные настройки
python -m build --verbose

# Проверьте entry points в собранном пакете
unzip -l dist/*.whl | grep entry_points
```

#### **Практический пример из проекта KGRV:**

**Проблема, которую мы обнаружили:**
```bash
# ❌ Неправильные entry points в pyproject.toml
[project.scripts]
kgrv-cli = "scripts.cli:main"  # Старый путь!

# ✅ Правильные entry points
[project.scripts]
kgrv = "kgrv.cli_click:cli"    # Новый путь!
```

**Результат проблемы:**
- CLI команда `kgrv` не работала после установки
- В `entry_points.txt` оставались старые настройки
- Пакет собирался с неправильной конфигурацией

**Решение:**
1. Обновили `pyproject.toml` с правильными entry points
2. Переустановили пакет в режиме разработки: `pip install -e .`
3. Пересобрали пакет: `python -m build`
4. CLI заработал корректно

## 🛠️ Подготовка к публикации

### 1. Проверка структуры проекта

```bash
# Структура должна выглядеть так:
your-project/
├── your_package/       # Основной пакет
│   ├── __init__.py
│   └── module.py
├── tests/             # Тесты
├── docs/              # Документация
├── setup.py           # Конфигурация
├── pyproject.toml     # Современная конфигурация
├── README.md          # Описание
├── LICENSE            # Лицензия
├── CHANGELOG.md       # История изменений
├── requirements.txt   # Зависимости
├── MANIFEST.in        # Файлы для дистрибутива
└── .gitignore         # Исключения Git
```

### 2. Установка инструментов для сборки
Где устанавливать build и twine?  
Рекомендация: В виртуальном окружении  
Преимущества:  
✅ Изолированные версии инструментов  
✅ Нет конфликтов с другими проектами  
✅ Воспроизводимая среда сборки  
✅ Легко переустановить при проблемах  
Недостатки:  
❌ Нужно активировать окружение каждый раз  
❌ Занимает место в каждом проекте  

Альтернатива: pipx (рекомендуется для инструментов)
```bash
# Установка pipx (если нет)
pip install pipx

# Установка инструментов через pipx
pipx install build
pipx install twine
```
Преимущества pipx:  
✅ Глобально доступны  
✅ Изолированы от других пакетов  
✅ Можно использовать из любого окружения  

🚀 Для проекта где есть ВО рекомендуется его активация и установка:
```bash
venv\Scripts\Activate.ps1

pip install build twine

# Проверьте установку
python -m build --version
twine --version
```

### 3. Создание виртуального окружения

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 4. Установка пакета в режиме разработки

```bash
pip install -e .
```

### 5. Тестирование функционала

```bash
# Запуск тестов
python -m pytest tests/ -v

# Тестирование CLI
your-command --help
your-command info
```

## 📦 Сборка пакета

### 1. Очистка старых сборок

```bash
rm -rf build/ dist/ *.egg-info/
```

Очистка репозитория:
```powershell
# Удаление временных файлов
Remove-Item -Recurse -Force build/ -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force dist/ -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force *.egg-info/ -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force htmlcov/ -ErrorAction SilentlyContinue
Remove-Item -Force .coverage -ErrorAction SilentlyContinue

# Удаление кэша Python
Get-ChildItem -Path . -Recurse -Directory -Name "__pycache__" | Remove-Item -Recurse -Force
```

### 2. Сборка дистрибутивов

```bash
python -m build
```

Эта команда создаст:
- `dist/your-package-0.1.0.tar.gz` - исходный дистрибутив
- `dist/your_package-0.1.0-py3-none-any.whl` - wheel дистрибутив

### 3. Проверка дистрибутивов

```bash
twine check dist/*
```

## 🧪 Публикация на Test PyPI

### 1. Регистрация на Test PyPI

1. Перейдите на https://test.pypi.org/
2. Создайте аккаунт
3. Подтвердите email

### 2. Создание API токена

1. Войдите в аккаунт Test PyPI
2. Перейдите в Account Settings → API tokens
3. Создайте токен с scope "Entire account"
4. Сохраните токен в безопасном месте

### 3. Настройка аутентификации

Создайте файл `~/.pypirc`:

```ini
[distutils]
index-servers =
    testpypi
    pypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-ваш-токен-test-pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-ваш-токен-pypi
```

### 4. Загрузка на Test PyPI

```bash
twine upload --repository testpypi dist/*
```

### 5. Проверка установки с Test PyPI

```bash
# Создайте новое виртуальное окружение
python -m venv test_env
test_env\Scripts\activate  # Windows

# Установите из Test PyPI
pip install --index-url https://test.pypi.org/simple/ your-package-name

# Тестируйте функционал
python -c "import your_package; print(your_package.__version__)"
your-command --help
```

## 🚀 Публикация на PyPI

### 1. Проверка на Test PyPI

Убедитесь, что:
- ✅ Пакет установился без ошибок
- ✅ Все команды работают
- ✅ Зависимости установились корректно
- ✅ Документация отображается правильно

### 2. Загрузка на PyPI

```bash
twine upload dist/*
```

### 3. Проверка установки с PyPI

```bash
# Новое окружение
python -m venv prod_test
prod_test\Scripts\activate

# Установка с PyPI
pip install your-package-name

# Тестирование
your-command --version
```

## ✅ Чек-лист перед публикацией

### Код и структура
- [ ] Корректная структура пакета
- [ ] `__init__.py` с версией и экспортами
- [ ] Все импорты работают
- [ ] CLI команды функционируют
- [ ] Тесты проходят

### Документация
- [ ] README.md с описанием и примерами
- [ ] LICENSE файл
- [ ] CHANGELOG.md с историей изменений
- [ ] Docstrings в коде

### Конфигурация
- [ ] setup.py правильно настроен
- [ ] pyproject.toml корректен
- [ ] **setup.py и pyproject.toml синхронизированы** ⚠️
- [ ] MANIFEST.in включает нужные файлы
- [ ] .gitignore исключает временные файлы

### Зависимости
- [ ] install_requires содержит только необходимые зависимости
- [ ] Версии зависимостей указаны корректно
- [ ] Опциональные зависимости в extras_require

### Сборка и тестирование
- [ ] `python -m build` проходит без ошибок
- [ ] `twine check dist/*` проходит проверку
- [ ] Пакет устанавливается и работает в чистом окружении

## 🔍 Диагностика проблем с конфигурацией

### Проверка синхронизации файлов

**1. Проверка зависимостей:**
```bash
# Извлечь зависимости из setup.py
python -c "import setup; print('setup.py dependencies:', setup.install_requires)"

# Извлечь зависимости из pyproject.toml
python -c "import tomllib; data=tomllib.load(open('pyproject.toml', 'rb')); print('pyproject.toml dependencies:', data['project']['dependencies'])"
```

**2. Проверка entry points:**
```bash
# Проверить entry points в собранном пакете
python -m build
unzip -l dist/*.whl | grep entry_points
cat kgrv.egg-info/entry_points.txt
```

**3. Проверка метаданных:**
```bash
# Показать метаданные пакета
python -c "import kgrv; print('Version:', kgrv.__version__)"
python -c "import pkg_resources; print('Installed version:', pkg_resources.get_distribution('kgrv').version)"
```

### Признаки проблем с конфигурацией

**❌ Проблемы:**
- CLI команда не работает после установки
- Зависимости не устанавливаются автоматически
- Разные версии в разных местах
- Предупреждения при сборке о переопределении настроек

**✅ Решение:**
- Проверьте синхронизацию setup.py и pyproject.toml
- Убедитесь, что используется правильный файл конфигурации
- Пересоберите пакет после исправлений

## ⚠️ Частые ошибки

### 1. Неправильное имя пакета
```python
# ❌ Неправильно
name="My-Package"  # Имя уже занято

# ✅ Правильно  
name="my-unique-package-name"  # Уникальное имя
```

### 2. Отсутствие зависимостей
```python
# ❌ Забыли указать зависимости
install_requires=[]

# ✅ Указали все необходимые
install_requires=["click>=8.0.0", "requests>=2.25.0"]
```

### 3. Неправильный MANIFEST.in
```ini
# ❌ Включили тесты
include tests/*

# ✅ Исключили тесты
recursive-exclude tests *
```

### 4. Отсутствие лицензии
```python
# ❌ Нет лицензии
# "License :: ???"

# ✅ Есть LICENSE файл и классификатор
"License :: OSI Approved :: MIT License"
```

### 5. Несоответствие setup.py и pyproject.toml
```python
# ❌ Разные зависимости в файлах
# setup.py: install_requires = ["click>=8.0.0"]
# pyproject.toml: dependencies = []

# ✅ Одинаковые зависимости
# setup.py: install_requires = ["click>=8.0.0"]
# pyproject.toml: dependencies = ["click>=8.0.0"]
```

```python
# ❌ Разные entry points
# setup.py: "kgrv=kgrv.cli_click:cli"
# pyproject.toml: "kgrv-cli=scripts.cli:main"

# ✅ Одинаковые entry points
# setup.py: "kgrv=kgrv.cli_click:cli"
# pyproject.toml: "kgrv=kgrv.cli_click:cli"
```

## 🔄 Обновление пакета

### 1. Обновите версию
В `__init__.py` и `setup.py`:
```python
__version__ = "0.1.1"  # Увеличьте версию
```

### 2. Обновите CHANGELOG.md
```markdown
## [0.1.1] - 2025-08-25
### Fixed
- Исправлена ошибка в CLI
```

### 3. Пересоберите и опубликуйте
```bash
rm -rf dist/
python -m build
twine upload dist/*
```

## 📚 Полезные ссылки

- [PyPI](https://pypi.org/) - основной репозиторий
- [Test PyPI](https://test.pypi.org/) - тестовый репозиторий  
- [Python Packaging Guide](https://packaging.python.org/)
- [setuptools документация](https://setuptools.pypa.io/)
- [twine документация](https://twine.readthedocs.io/)

Это руководство основано на реальном опыте публикации пакета KGRV и содержит все необходимые шаги для успешной публикации вашего Python пакета!
