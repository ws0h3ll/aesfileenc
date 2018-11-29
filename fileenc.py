from Crypto.Cipher import AES # import AES :D
key = input("What is the key i am using senpai? it must be a multiple of 16 bytes or else ! : ") # you better set this as a 16 multiple or i will not be a happy bunny
iv = input("What is the iv senpai? again must be a multiple of 16") # if this is not a multiple of 16 im going to be very mad
mode = AES.MODE_CBC # sets the encwypt mode
encryptor = AES.new(key, mode, IV=iv) # setsies the encwypt mode 
filetoopen = input("What file am i opening ?") # where are you storing the fanfics you dont want mummy to read
fr = open(filetoopen, "r") # let me read the file
text = fr.read() # i have readeded the file
while len(text) % 16 != 0: # if youre input string isnt 16 bytes i will correct it for you, you can thank me later with huggles
  text = text + '.' # lets make it 16 for you
ciphertext = encryptor.encrypt(text) # i have encwypted the fan fics
fw = open(filetoopen, "w") # lemme just overwite everyfing for you
fw.write(ciphertext) # moohahaha
print(ciphertext) # lets see what you get
print("Thankies for using uwu") #thankies senpai
# huggles from mmeeeeee :D
