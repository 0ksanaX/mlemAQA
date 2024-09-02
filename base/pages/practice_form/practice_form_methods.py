from idlelib.debugger_r import close_remote_debugger

import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
from src.config.expectations import Wait


class PracticeFormMethods:

    @staticmethod
    def fill_name_input(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)

        try:
            with allure.step("First and Last name, email"):
                practice_form.first_name.fill(practice_form.Name_text)
                practice_form.last_name.fill("Klinkova")
                practice_form.email.fill("help@mail.com")

            with allure.step("Gender"):
                practice_form.male.click()
                practice_form.female.click()
                practice_form.other.click()

            with allure.step("Date of Birth"):
                practice_form.date_of_birth.click()


            with allure.step("Mobile"):
                practice_form.mobile.fill("8800535353")

            with allure.step("Hobbies"):
                practice_form.sports.click()
                practice_form.reading.click()
                practice_form.music.click()

            with allure.step("Address"):
                practice_form.current_address.fill("str.Krasnaya")

            with allure.step("End"):
                practice_form.submit.click()

        except AssertionError as e:
            errors.append(str(e))



