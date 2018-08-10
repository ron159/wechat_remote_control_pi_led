import itchat
import led


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg['Text'] == "闪一闪":
    #led.openLed()
    #print(msg.text)
        reply_content = "正在闪一闪"
        itchat.send(reply_content,toUserName=msg['FromUserName'])
    else:
        pass


itchat.auto_login(enableCmdQR=2)
itchat.run() 
