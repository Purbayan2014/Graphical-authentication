import hashlib

def dc():
   h = hashlib.new('sha512_256')
   h.update(b"1234")
   password = h.hexdigest()
   print(password)



if __name__ == "__main__":
	dc()
# 3bb20e367b1a988158e3dbbed06bf6415beea23f56bbb15dbf346505edc7e7df purbayan cat 1234