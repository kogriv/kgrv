"""
Модуль About для вывода информации о разработчике и проекте.

Этот модуль содержит класс About, который предоставляет
информацию о разработчике, его навыках и проектах.
"""

from typing import List, Dict, Any
import datetime


class About:
    """
    Класс для вывода информации о разработчике.
    
    Attributes:
        name (str): Имя разработчика
        github (str): GitHub профиль
        skills (List[str]): Список навыков
        projects (List[str]): Список проектов
    """
    
    def __init__(self, name: str = "kogriv"):
        """
        Инициализация объекта About.
        
        Args:
            name (str): Имя разработчика, по умолчанию "kogriv"
        """
        self.name = name
        self.github = f"https://github.com/{name}"
        self.skills = [
            "Python",
            "JavaScript", 
            "Git",
            "Docker",
            "SQL",
            "MQL5"
        ]
        self.projects = [
            "kgrv - Python пакет для экспериментов",
            "Различные скрипты автоматизации",
            "Торговые роботы на MQL5"
        ]
        self.created_at = datetime.datetime.now()
    
    def get_info(self) -> Dict[str, Any]:
        """
        Получить полную информацию о разработчике.
        
        Returns:
            Dict[str, Any]: Словарь с информацией о разработчике
        """
        return {
            "name": self.name,
            "github": self.github,
            "skills": self.skills,
            "projects": self.projects,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def get_skills(self) -> List[str]:
        """
        Получить список навыков.
        
        Returns:
            List[str]: Список навыков разработчика
        """
        return self.skills.copy()
    
    def add_skill(self, skill: str) -> None:
        """
        Добавить новый навык.
        
        Args:
            skill (str): Новый навык для добавления
        """
        if skill not in self.skills:
            self.skills.append(skill)
    
    def get_projects(self) -> List[str]:
        """
        Получить список проектов.
        
        Returns:
            List[str]: Список проектов разработчика
        """
        return self.projects.copy()
    
    def add_project(self, project: str) -> None:
        """
        Добавить новый проект.
        
        Args:
            project (str): Новый проект для добавления
        """
        if project not in self.projects:
            self.projects.append(project)
    
    def print_info(self) -> None:
        """
        Вывести информацию о разработчике в консоль.
        """
        print(f"👨‍💻 Разработчик: {self.name}")
        print(f"🔗 GitHub: {self.github}")
        print(f"📅 Создано: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n🛠️ Навыки:")
        for skill in self.skills:
            print(f"  • {skill}")
        
        print("\n📂 Проекты:")
        for project in self.projects:
            print(f"  • {project}")
    
    def __str__(self) -> str:
        """
        Строковое представление объекта.
        
        Returns:
            str: Строковое представление информации о разработчике
        """
        return f"About({self.name}): {len(self.skills)} навыков, {len(self.projects)} проектов"
    
    def __repr__(self) -> str:
        """
        Представление объекта для отладки.
        
        Returns:
            str: Представление объекта для отладки
        """
        return f"About(name='{self.name}', skills={len(self.skills)}, projects={len(self.projects)})"
