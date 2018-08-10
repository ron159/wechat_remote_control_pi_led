import itchat
import led

#itchat框架，关注TEXT消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    #得到任何text消息就打开流水灯，最后原消息返回
    led.openLed()
    print(msg.text)
    return msg.text

itchat.auto_login(enableCmdQR=2)
itchat.run() 
