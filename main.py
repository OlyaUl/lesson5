#! env bin/python
# codding = utf-8
from abc import ABCMeta,abstractmethod

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
    def __new__(cls, *args, **kwargs):
        return AngryBot(*args, **kwargs)


evil = EvilBot("ha-ha")
print(evil.say_hi())


class Sayer:
    def say(self, message):
        pass


class HttpHandler(metaclass=ABCMeta):

    @abstractmethod
    def get(self, location):
        raise NotImplementedError()

    @abstractmethod
    def get(self, location, data):
        raise NotImplementedError()


class Memoize(HttpHandler):
    value = "default"
    def get(self, location):
        return self.value

    def post(self,location,data):
        self.value = data


