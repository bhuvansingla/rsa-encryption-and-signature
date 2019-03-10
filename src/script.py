import rsa
def main():

    message = input("Type your message:\n>").encode('utf8')
    
    (pubKey1, privKey1) = rsa.newkeys(512)
    (pubKey2, privKey2) = rsa.newkeys(512)
    
    encryptedMsg = rsa.encrypt(message, pubKey2)
    
    signature = rsa.sign(encryptedMsg, privKey1, 'SHA-1')
    print("\nENCRYPTED MESSAGE:\n{0}\n\nSIGNATURE:\n{1}".format(list(encryptedMsg), list(signature)))
    
    inMsg = input("\nENTER THE ENCRYPTED MESSAGE:\n>")
    inSign = input("\nENTER THE SIGNATURE:\n>")

    try:
        inMsg = bytearray(list(map(int, inMsg[1:-1].split(','))))
        inSign = bytearray(list(map(int, inSign[1:-1].split(','))))
    except:
        print("\nINVALID INPUT FORMAT\n")
        return

    try:
        rsa.verify(inMsg, inSign, pubKey1)
        print("\nVERIFICATION SUCCESSFUL")
    except(rsa.pkcs1.VerificationError):
        print("\nVERIFICATION FAILED\n")
        return

    try:
        print("\nMESSAGE:", (rsa.decrypt(inMsg, privKey2)).decode('utf8'))
    except(rsa.pkcs1.DecryptionError):
        print("\nDECRYPTION FAILED\n")
        return

cont = 1
while(cont):
    main()
    cont = int(input("\nEnter 1 to continue or 0 to quit.\n>"))
