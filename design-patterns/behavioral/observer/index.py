from abc import ABC, abstractmethod


class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)


class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, event):
        pass


class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channel, event):
        print(f'User {self.name} received notification from {channel}: {event}')


channel = YoutubeChannel("nice-channel")

channel.subscribe(YoutubeUser('user1'))
channel.subscribe(YoutubeUser('user2'))
channel.subscribe(YoutubeUser('user3'))

channel.notify('new video')
