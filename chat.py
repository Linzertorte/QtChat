from PySide.QtCore import *
from PySide.QtGui import *
import sys
import chatUi
import socket
import threading
import socket, select, string


class myThread(QObject, threading.Thread):
    punched = Signal(str)
    def __init__(self,nick):
        QObject.__init__(self)
        threading.Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nick = nick
        
    Slot(str)
    def send(self,msg):
        self.s.send(self.nick+': '+msg)
        
    def run(self):
        host = 'localhost'
        port = 5000
        self.s.settimeout(2)
        
        # connect to remote host
        try :
            self.s.connect((host, port))
        except :
            print 'Unable to connect'
            sys.exit()
         
        print 'Connected to remote host. Start sending messages'
         
        while 1:
            socket_list = [self.s]
             
            # Get the list sockets which are readable
            read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
             
            for sock in read_sockets:
                #incoming message from remote server
                if sock == self.s:
                    data = sock.recv(4096)
                    if not data :
                        print '\nDisconnected from chat server'
                        sys.exit()
                    else :
                        #print data
                        self.punched.emit(data)


class ChatMain(QWidget, chatUi.Ui_Form):
    def __init__(self, parent =None):
        super(ChatMain, self).__init__(parent)
        self.setupUi(self)
        self.text = ''
        self.connect(self.sendButton, SIGNAL('clicked()'), self.send)

    pressed = Signal(str)
    def send(self):
        self.pressed.emit(self.msgEdit.text()+'\n')
        self.say_punched('You: '+self.msgEdit.text()+'\n')
        self.msgEdit.setText('')
        
    Slot(str)
    def say_punched(self,data):
        self.text += data
        self.chatEdit.setText(self.text)

app = QApplication(sys.argv)
form = ChatMain()
form.show()
t=myThread(sys.argv[1])
t.punched.connect(form.say_punched)
form.pressed.connect(t.send)
t.start()
app.exec_()
