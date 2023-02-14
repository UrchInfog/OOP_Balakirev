class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:
    lst_msg = []

    @classmethod
    def add_message(self, msg):
        self.lst_msg.append(msg)

    @classmethod
    def remove_message(self, msg):
        if msg in self.lst_msg:
            self.lst_msg.remove(msg)

    @classmethod
    def set_like(self, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(self, n):
        for idx in range(n):
            print(self.lst_msg[idx].text)

    @classmethod
    def total_messages(self):
        return len(self.lst_msg)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)

Viber.show_last_message(2)
print(msg.__dict__)