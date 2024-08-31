class Smartphone:
    def __init__(self, memory, apps=None, is_on=False):
        self.memory = memory
        self.apps = apps if apps else []
        self.is_on = is_on

    def power(self):
        self.is_on = 0 if self.is_on else 1
        return "Phone is on" if self.is_on else "Phone is off"

    def install(self, app, app_memory):
        if self.is_on:
            if self.memory >= app_memory:
                self.apps.append(app)
                self.memory -= app_memory
                return f"{app} installed"
            else:
                return f"Insufficient memory to install {app}"
        else:
            return f"Phone is off, {app} can't be installed"

    def uninstall(self, app, app_memory):
        if self.is_on:
            self.apps.append(app)
            self.memory += app_memory
            return f"{app} uninstalled"
        else:
            return f"Phone is off, {app} can't be uninstalled"
    def status(self):
        return f"Apps installed: {self.apps.__len__()}. Remaining memory: {self.memory}"

iphone = Smartphone(memory=8192)
print(iphone.install("Duolingvo", 100))
print(iphone.status())
print(iphone.power())
print(iphone.install("Chrome Browser", 1000))
print(iphone.install("Civ 6", 5000))
print(iphone.install("Math practice", 50))
print(iphone.install("PUBG Mobile", 7000))
print(iphone.status())




