#!/usr/bin/env python3
"""
CLI интерфейс для пакета kgrv.

Предоставляет командную строку для взаимодействия с функциональностью пакета kgrv.
"""

import sys
import os
import argparse
import json

# Добавляем путь к пакету kgrv для локальной разработки
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kgrv import About, __version__
except ImportError:
    print("❌ Ошибка: Не удалось импортировать пакет kgrv")
    sys.exit(1)


def create_parser():
    """
    Создает парсер командной строки.
    
    Returns:
        argparse.ArgumentParser: Настроенный парсер
    """
    parser = argparse.ArgumentParser(
        description="CLI интерфейс для пакета kgrv",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python cli.py info                    # Показать информацию о разработчике
  python cli.py info --name "John"      # Показать информацию для John
  python cli.py skills                  # Показать только навыки
  python cli.py projects                # Показать только проекты
  python cli.py json                    # Вывести в JSON формате
  python cli.py --version               # Показать версию пакета
        """
    )
    
    parser.add_argument(
        '--version', 
        action='version', 
        version=f'kgrv {__version__}'
    )
    
    parser.add_argument(
        '--name', 
        type=str, 
        default='kogriv',
        help='Имя разработчика (по умолчанию: kogriv)'
    )
    
    parser.add_argument(
        '--output', 
        choices=['text', 'json'],
        default='text',
        help='Формат вывода (по умолчанию: text)'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')
    
    # Команда info
    info_parser = subparsers.add_parser('info', help='Показать полную информацию')
    info_parser.add_argument(
        '--add-skill', 
        action='append',
        help='Добавить дополнительный навык'
    )
    info_parser.add_argument(
        '--add-project', 
        action='append',
        help='Добавить дополнительный проект'
    )
    
    # Команда skills
    subparsers.add_parser('skills', help='Показать только навыки')
    
    # Команда projects
    subparsers.add_parser('projects', help='Показать только проекты')
    
    # Команда json
    subparsers.add_parser('json', help='Вывести всю информацию в JSON формате')
    
    return parser


def handle_info_command(args, about):
    """
    Обрабатывает команду info.
    
    Args:
        args: Аргументы командной строки
        about: Объект About
    """
    # Добавляем дополнительные навыки если указаны
    if args.add_skill:
        for skill in args.add_skill:
            about.add_skill(skill)
    
    # Добавляем дополнительные проекты если указаны
    if args.add_project:
        for project in args.add_project:
            about.add_project(project)
    
    if args.output == 'json':
        print(json.dumps(about.get_info(), ensure_ascii=False, indent=2))
    else:
        about.print_info()


def handle_skills_command(args, about):
    """
    Обрабатывает команду skills.
    
    Args:
        args: Аргументы командной строки
        about: Объект About
    """
    skills = about.get_skills()
    
    if args.output == 'json':
        print(json.dumps({"skills": skills}, ensure_ascii=False, indent=2))
    else:
        print(f"🛠️ Навыки {about.name}:")
        for skill in skills:
            print(f"  • {skill}")


def handle_projects_command(args, about):
    """
    Обрабатывает команду projects.
    
    Args:
        args: Аргументы командной строки
        about: Объект About
    """
    projects = about.get_projects()
    
    if args.output == 'json':
        print(json.dumps({"projects": projects}, ensure_ascii=False, indent=2))
    else:
        print(f"📂 Проекты {about.name}:")
        for project in projects:
            print(f"  • {project}")


def handle_json_command(args, about):
    """
    Обрабатывает команду json.
    
    Args:
        args: Аргументы командной строки
        about: Объект About
    """
    print(json.dumps(about.get_info(), ensure_ascii=False, indent=2))


def main():
    """
    Основная функция CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
    
    # Если команда не указана, показываем help
    if not args.command:
        parser.print_help()
        return
    
    # Создаем объект About
    about = About(args.name)
    
    # Обрабатываем команды
    if args.command == 'info':
        handle_info_command(args, about)
    elif args.command == 'skills':
        handle_skills_command(args, about)
    elif args.command == 'projects':
        handle_projects_command(args, about)
    elif args.command == 'json':
        handle_json_command(args, about)
    else:
        print(f"❌ Неизвестная команда: {args.command}")
        parser.print_help()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
