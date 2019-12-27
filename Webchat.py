import tornado.ioloop
import tornado.web

import CorkBoard

corkboard = CorkBoard.CorkBoard()
CorkBoard.addMessages(corkboard)

class Chat(tornado.web.RequestHandler):
    def get(self):
        sender = self.get_argument("sender",None)
        message = self.get_argument("message",None)
        if(sender and message):
            msg = CorkBoard.Message(sender, message)
            corkboard.postMessage(msg)

        if(not sender):
            sender = " "

        self.write("""
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <title>Chat</title>
          </head>
          <body>
            <H1>Web Chat</H1>
            <table>
              <tr>
                <th>Date</th>
                <th>Name</th>
                <th>Message</th>
              </tr>
        """)

        for mesg in corkboard.getMessages():
            self.write("<tr><td>"+mesg.date.strftime("%Y-%m-%d %H:%M")+"</td><td>"+mesg.sender+"</td><td>"+mesg.message+"</td></tr>")

        self.write("""</table>
        <p>
        <p>
        <form action="/chat">
      Sender: <input type="text" name="sender" value='"""+sender+"""'>
      Message:<input type="text" name="message">
      <input type="Submit">
    </form>
    """)

handlers = [
    ("/chat", Chat)
]

if __name__ == "__main__":
    app = tornado.web.Application(handlers)
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
