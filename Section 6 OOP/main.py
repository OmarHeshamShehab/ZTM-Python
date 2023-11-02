class PlayerCharecter:
    """
    declaring a class
    """

    # class object attributre something that doesn't change
    membership = True

    def __init__(self, name="", age=0):
        self._name = name  # means it is private
        self.age = age

    def shout(self):
        print(f"my name is {self._name}")

        return "done"

    # you can access the main class method and mopdify something and then instentiate
    @classmethod
    def addition(cls, n1, n2):
        return n1 + n2

    @staticmethod
    def multiply(n1, n2):
        return n1 * n2

    def run(self):
        return self


# player2 = PlayerCharecter("Omar", 31)

# print(player1.run())
# print(player2.run())

# player1 = PlayerCharecter("Omar", 31)
# player1.shout()
# print(PlayerCharecter.multiply(3, 3))


# class User:
#     def __init__(self, email):
#         self.email = email

#     def sign_in(self):
#         print("you are logged in")


# class Wizard(User):
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"attacking with power of {self.power}")


# class Archer(User):
#     def __init__(self, name, num_arrows, email):
#         super().__init__(email)
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f"attacking with arrows: arrows left -{self.num_arrows}")


# wizzard1 = Wizard("merlin", 50, "wizard@test.test")
# archer1 = Archer("oliver", 50, "archer@test.test")

# wizzard1.attack()
# archer1.attack()
# print(wizzard1.email)
# print(archer1.email)


class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
