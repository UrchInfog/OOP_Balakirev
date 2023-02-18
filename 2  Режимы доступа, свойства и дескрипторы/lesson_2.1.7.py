from string import digits, ascii_lowercase
from random import sample, randint


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    true_chars = digits + ascii_lowercase + "_."

    @classmethod
    def get_random_email(cls):
        """"генерация случайного email-адреса по формату: xxxxxxx...xxx@gmail.com"""
        mail = "".join(sample(cls.true_chars, randint(6, 10))) + "@gmail.com"
        return mail

    @classmethod
    def check_email(cls, email):
        cls.__is_email_str(email)
        if not set(email).issubset(cls.true_chars + "@"):
            return False
        if len(email.split("@")[0]) > 100 or len(email.split("@")[1]) > 50:
            return False
        if email.split("@")[1].count(".") == 0:
            return False
        if email.count(".."):
            return False
        return True

    @classmethod
    def __is_email_str(cls, email):
        return type(email) == str


# res = EmailValidator.check_email("sc_lib@list.ru")
res = EmailValidator()
mail = EmailValidator.get_random_email()
print(res)
print(mail)
