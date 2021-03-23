import sys 

class Fatball:
    def __init__(self, key):
        self.key = key
        
    def enfatball(self, msg):
        keyList = list(self.key)
        msgList = list(msg)
        keyLen = len(keyList)
        msgLen = len(msgList)
        cipherText = [''] * msgLen
        for i in range(msgLen):
            cipherText[i] = chr(ord(msgList[i]) ^ ord(keyList[i % keyLen]))   
        return''.join(cipherText)

    def defatball(self, msg):
        keyList = list(self.key)
        msgList = list(msg)
        keyLen = len(keyList)
        msgLen = len(msgList)
        cipherText = [''] * msgLen
        for i in range(msgLen):
            cipherText[i] = chr(ord(msgList[i]) ^ ord(keyList[i % keyLen]))   
        return''.join(cipherText)

if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) > 2:
        if sys.argv[1] == '-e':
            f=Fatball("123")
            print(f.enfatball("hhh"))
        elif sys.argv[1] == '-d':  
            f=Fatball("123")
            print(f.defatball("yyy")) 
