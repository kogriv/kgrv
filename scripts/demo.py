#!/usr/bin/env python3
"""
Демонстрационный скрипт для пакета kgrv.

Этот скрипт показывает основные возможности пакета kgrv,
включая использование класса About и его методов.
"""

import sys
import os

# Добавляем путь к пакету kgrv для локальной разработки
# В продакшене будет использоваться установленный пакет
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kgrv import About
except ImportError:
    print("❌ Ошибка: Не удалось импортировать пакет kgrv")
    print("Убедитесь, что пакет установлен или запускаете скрипт из корневой папки проекта")
    sys.exit(1)


def main():
    """
    Основная функция демонстрации.
    """
    print("🚀 Демонстрация пакета KGRV")
    print("=" * 50)
    
    # Создаем объект About
    about = About()
    
    print("\n📋 Базовая информация:")
    about.print_info()
    
    print(f"\n🔍 Строковое представление: {about}")
    print(f"🐛 Отладочное представление: {repr(about)}")
    
    # Демонстрация добавления навыков
    print("\n➕ Добавляем новый навык...")
    about.add_skill("Machine Learning")
    print(f"Обновленные навыки: {', '.join(about.get_skills())}")
    
    # Демонстрация добавления проекта
    print("\n➕ Добавляем новый проект...")
    about.add_project("ML модель для анализа данных")
    
    # Получение полной информации в виде словаря
    print("\n📊 Полная информация (JSON-формат):")
    import json
    info = about.get_info()
    print(json.dumps(info, ensure_ascii=False, indent=2))
    
    print("\n✅ Демонстрация завершена!")


def interactive_demo():
    """
    Интерактивная демонстрация с пользовательским вводом.
    """
    print("\n🎮 Интерактивная демонстрация")
    print("-" * 30)
    
    # Создание объекта с пользовательским именем
    name = input("Введите ваше имя (или нажмите Enter для 'kogriv'): ").strip()
    if not name:
        name = "kogriv"
    
    about = About(name)
    print(f"\n👋 Привет, {name}!")
    
    # Добавление пользовательских навыков
    print("\nДобавим ваши навыки (введите 'stop' для завершения):")
    while True:
        skill = input("Введите навык: ").strip()
        if skill.lower() == 'stop' or not skill:
            break
        about.add_skill(skill)
        print(f"✅ Добавлен навык: {skill}")
    
    # Итоговая информация
    print(f"\n🎯 Итоговая информация:")
    about.print_info()


if __name__ == "__main__":
    # Запуск основной демонстрации
    main()
    
    # Запрос на интерактивную демонстрацию
    while True:
        choice = input("\nХотите запустить интерактивную демонстрацию? (y/n): ").strip().lower()
        if choice in ['y', 'yes', 'д', 'да']:
            interactive_demo()
            break
        elif choice in ['n', 'no', 'н', 'нет']:
            print("👋 До свидания!")
            break
        else:
            print("Пожалуйста, введите 'y' или 'n'")
