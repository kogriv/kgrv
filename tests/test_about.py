"""
Тесты для модуля about.py

Содержит unit-тесты для класса About и его методов.
"""

import unittest
import sys
import os
from datetime import datetime

# Добавляем путь к пакету kgrv для тестирования
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from kgrv.about import About


class TestAbout(unittest.TestCase):
    """
    Тестовый класс для About.
    """
    
    def setUp(self):
        """
        Настройка перед каждым тестом.
        """
        self.about = About("TestUser")
    
    def test_init_default(self):
        """
        Тест инициализации с параметрами по умолчанию.
        """
        about_default = About()
        self.assertEqual(about_default.name, "kogriv")
        self.assertEqual(about_default.github, "https://github.com/kogriv")
        self.assertIsInstance(about_default.skills, list)
        self.assertIsInstance(about_default.projects, list)
        self.assertIsInstance(about_default.created_at, datetime)
    
    def test_init_custom_name(self):
        """
        Тест инициализации с пользовательским именем.
        """
        self.assertEqual(self.about.name, "TestUser")
        self.assertEqual(self.about.github, "https://github.com/TestUser")
    
    def test_initial_skills(self):
        """
        Тест начальных навыков.
        """
        expected_skills = ["Python", "JavaScript", "Git", "Docker", "SQL", "MQL5"]
        self.assertEqual(self.about.skills, expected_skills)
    
    def test_initial_projects(self):
        """
        Тест начальных проектов.
        """
        self.assertIn("kgrv", self.about.projects[0])
        self.assertTrue(len(self.about.projects) >= 3)
    
    def test_get_info(self):
        """
        Тест метода get_info.
        """
        info = self.about.get_info()
        
        self.assertIsInstance(info, dict)
        self.assertIn("name", info)
        self.assertIn("github", info)
        self.assertIn("skills", info)
        self.assertIn("projects", info)
        self.assertIn("created_at", info)
        
        self.assertEqual(info["name"], "TestUser")
        self.assertEqual(info["github"], "https://github.com/TestUser")
        self.assertIsInstance(info["skills"], list)
        self.assertIsInstance(info["projects"], list)
        self.assertIsInstance(info["created_at"], str)
    
    def test_get_skills(self):
        """
        Тест метода get_skills.
        """
        skills = self.about.get_skills()
        
        # Проверяем, что возвращается копия
        self.assertIsNot(skills, self.about.skills)
        self.assertEqual(skills, self.about.skills)
        
        # Изменение копии не должно влиять на оригинал
        skills.append("TestSkill")
        self.assertNotIn("TestSkill", self.about.skills)
    
    def test_add_skill(self):
        """
        Тест метода add_skill.
        """
        initial_count = len(self.about.skills)
        
        # Добавление нового навыка
        self.about.add_skill("Machine Learning")
        self.assertIn("Machine Learning", self.about.skills)
        self.assertEqual(len(self.about.skills), initial_count + 1)
        
        # Попытка добавить дубликат
        self.about.add_skill("Machine Learning")
        self.assertEqual(len(self.about.skills), initial_count + 1)
        
        # Добавление еще одного навыка
        self.about.add_skill("Data Science")
        self.assertIn("Data Science", self.about.skills)
        self.assertEqual(len(self.about.skills), initial_count + 2)
    
    def test_get_projects(self):
        """
        Тест метода get_projects.
        """
        projects = self.about.get_projects()
        
        # Проверяем, что возвращается копия
        self.assertIsNot(projects, self.about.projects)
        self.assertEqual(projects, self.about.projects)
        
        # Изменение копии не должно влиять на оригинал
        projects.append("TestProject")
        self.assertNotIn("TestProject", self.about.projects)
    
    def test_add_project(self):
        """
        Тест метода add_project.
        """
        initial_count = len(self.about.projects)
        
        # Добавление нового проекта
        self.about.add_project("ML проект")
        self.assertIn("ML проект", self.about.projects)
        self.assertEqual(len(self.about.projects), initial_count + 1)
        
        # Попытка добавить дубликат
        self.about.add_project("ML проект")
        self.assertEqual(len(self.about.projects), initial_count + 1)
        
        # Добавление еще одного проекта
        self.about.add_project("Web приложение")
        self.assertIn("Web приложение", self.about.projects)
        self.assertEqual(len(self.about.projects), initial_count + 2)
    
    def test_str_representation(self):
        """
        Тест строкового представления.
        """
        str_repr = str(self.about)
        self.assertIn("TestUser", str_repr)
        self.assertIn("навыков", str_repr)
        self.assertIn("проектов", str_repr)
        
        # Проверяем формат
        expected_pattern = f"About(TestUser): {len(self.about.skills)} навыков, {len(self.about.projects)} проектов"
        self.assertEqual(str_repr, expected_pattern)
    
    def test_repr_representation(self):
        """
        Тест представления для отладки.
        """
        repr_str = repr(self.about)
        self.assertIn("About", repr_str)
        self.assertIn("name='TestUser'", repr_str)
        self.assertIn(f"skills={len(self.about.skills)}", repr_str)
        self.assertIn(f"projects={len(self.about.projects)}", repr_str)
    
    def test_print_info(self):
        """
        Тест метода print_info (проверяем, что не возникает ошибок).
        """
        try:
            # Перенаправляем вывод для тестирования
            import io
            from contextlib import redirect_stdout
            
            f = io.StringIO()
            with redirect_stdout(f):
                self.about.print_info()
            
            output = f.getvalue()
            self.assertIn("TestUser", output)
            self.assertIn("github.com/TestUser", output)
            self.assertIn("Навыки:", output)
            self.assertIn("Проекты:", output)
            
        except Exception as e:
            self.fail(f"print_info() вызвал исключение: {e}")
    
    def test_created_at_timestamp(self):
        """
        Тест создания временной метки.
        """
        now = datetime.now()
        about_new = About("TimeTest")
        
        # Время создания должно быть близко к текущему
        time_diff = abs((about_new.created_at - now).total_seconds())
        self.assertLess(time_diff, 1.0)  # Разница меньше секунды


class TestAboutEdgeCases(unittest.TestCase):
    """
    Тесты граничных случаев для класса About.
    """
    
    def test_empty_name(self):
        """
        Тест с пустым именем.
        """
        about = About("")
        self.assertEqual(about.name, "")
        self.assertEqual(about.github, "https://github.com/")
    
    def test_special_characters_in_name(self):
        """
        Тест со специальными символами в имени.
        """
        about = About("user-name_123")
        self.assertEqual(about.name, "user-name_123")
        self.assertEqual(about.github, "https://github.com/user-name_123")
    
    def test_unicode_name(self):
        """
        Тест с Unicode символами в имени.
        """
        about = About("Иван")
        self.assertEqual(about.name, "Иван")
        self.assertEqual(about.github, "https://github.com/Иван")
    
    def test_add_empty_skill(self):
        """
        Тест добавления пустого навыка.
        """
        about = About()
        initial_count = len(about.skills)
        
        about.add_skill("")
        self.assertIn("", about.skills)
        self.assertEqual(len(about.skills), initial_count + 1)
    
    def test_add_empty_project(self):
        """
        Тест добавления пустого проекта.
        """
        about = About()
        initial_count = len(about.projects)
        
        about.add_project("")
        self.assertIn("", about.projects)
        self.assertEqual(len(about.projects), initial_count + 1)


if __name__ == "__main__":
    # Запуск тестов
    unittest.main(verbosity=2)
