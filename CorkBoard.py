import datetime

class Message(object):

    def __init__(self, sender, message):
        self.sender = sender
        self.message = message
        self.date = datetime.datetime.now()

    def __repr__(self):
        return "Date: "+self.date.strftime("%Y-%m-%d %H:%M")+" From: "+self.sender+" Message: "+self.message



class CorkBoard(object):
    def __init__(self):
        self.messages = []

    def postMessage(self, message):
        self.messages.append(message)

    def getMessages(self):
        return self.messages

    def getMessagesFromFilter(self, lst):
        return lst

    def clear(self):
        del(self.messages[0:len(self.messages)])

def addMessages(newmessage):
    message1 = Message("Mystery Person", "Hi how are you.")
    newmessage.postMessage(message1)
    # message2 = new Message("Online Friend", "What's up")
    # newmessage.postMessage(message2)

    message1 = Message("Online Friend", "What's up")
    newmessage.postMessage(message1)


if __name__ == '__main__':
    corkboard = CorkBoard()
    addMessages(corkboard)
    print(str(corkboard.getMessages()))
