class AppStore:
    all_apps = []

    def add_application(self, app):
        """добавление нового приложения app в магазин"""
        self.all_apps.append(app)

    def remove_application(self, app):
        """удаление приложения app из магазина"""
        if app in self.all_apps:
            self.all_apps.remove(app)
            return True
        else:
            return False

    def block_application(self, app):
        """блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True)"""
        app.blocked = True

    def total_apps(self):
        """возвращает общее число приложений в магазине"""
        return len(self.all_apps)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.all_apps)
# store.remove_application(app_youtube)
