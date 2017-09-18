#! env bin/python
# codding = utf-8


class Bot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("My name is {self.name}".format(**locals()))

myBot = Bot('test')
myBot.say_hi()
Bot("ddd").say_hi()
# print(myBot)


class AngryBot(Bot):
    def say_hi(self):
        print("angry test")

a_bot = AngryBot("The bad")
a_bot.say_hi()


class EvilBot(Bot):

    @staticmethod
    def __new__(self, *args, **kwargs):
        return AngryBot(*args, **kwargs)
