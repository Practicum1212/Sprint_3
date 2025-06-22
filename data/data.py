import random


class PersonData:
    user_name = 'RomanPanichev_24'
    login = 'RomanPanichev_24_666@gmail.com'
    password = '1234qwerty'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@ygmail.com"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"


class ExpectedTexts:
    SAUCES = 'Соусы'
    FILLINGS = 'Начинки'
    BUNS = 'Булки'

