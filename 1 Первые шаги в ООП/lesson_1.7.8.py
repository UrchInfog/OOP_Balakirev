from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits + " "

    @classmethod
    def check_card_number(cls, number):
        if re.match("^\d{4}-\d{4}-\d{4}-\d{4}$", number):
            return True
        else:
            return False

    @classmethod
    def check_name(cls, name):
        if len(name.split()) == 2 and set(name).issubset(set(cls.CHARS_FOR_NAME)):
            return True
        else:
            return False


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV SSS")

print(is_number)
print(is_name)
