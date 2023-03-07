class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if not any([obj.name == app.name for obj in self.apps]):
            self.apps.append(app)

    def remove_app(self, app):
        for obj in self.apps:
            if app.name == obj.name:
                self.apps.remove(obj)


class AppVK:
    def __init__(self, name="ВКонтакте"):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max, name="YouTube"):
        self.name = name
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone, name="Phone"):
        self.phone = phone
        self.name = name


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
sm.remove_app(AppVK())
for a in sm.apps:
    print(a.name)

a1 = AppVK()
a2 = AppVK()

print(type(a1) == AppVK, type(a2))