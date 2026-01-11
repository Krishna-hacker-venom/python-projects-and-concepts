class C1:
    def __init__(self, name, age):
        self._name = name      # protected
        self._age = age        # protected

    def get_age(self):
        return self._age

obj = C1("krishna", 20)

print(obj.get_age())  # ✔ correct way
print(obj._age)       # ⚠ allowed but discouraged
