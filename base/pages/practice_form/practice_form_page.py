from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Форма"""
        self.first_name = Input(page, locator='//*[@id="firstName"]', name='Имя')
        self.last_name = Input(page, locator='//*[@id="lastName"]', name='Фамилия')
        self.email = Input(page, locator='//*[@id="userEmail"]',name='Email')
        self.male = Button(page, locator='//*[@for="gender-radio-1"]', name='Male')
        self.female = Button(page, locator='//*[@for="gender-radio-2"]', name='Female')
        self.other = Button(page, locator='//*[@for="gender-radio-3"]', name='Other')
        self.mobile = Input(page, locator='//*[@id="userNumber"]', name='User mobile')
        self.sports = Button(page, locator='//*[@for="hobbies-checkbox-1"]', name='checkbox1')
        self.reading = Button(page, locator='//*[@for="hobbies-checkbox-2"]', name='checkbox2')
        self.music = Button(page, locator='//*[@for="hobbies-checkbox-3"]', name='checkbox3')
        self.upload_picture = Button(page, locator='//*[@id="uploadPicture"]', name='File Upload')
        self.current_address = Input(page, locator='//*[@id="currentAddress"]', name='adress')
        self.date_of_birth = Button(page, locator='//*[@id="dateOfBirthInput"]', name='birth')
        self.submit = Button(page, locator='//*[@id="submit"]', name='Submit')



        """Ожидания"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'
        self.Wait_email = '//*[@id="userEmail"]'


        """Текст"""
        self.Name_text = 'ksenia'
