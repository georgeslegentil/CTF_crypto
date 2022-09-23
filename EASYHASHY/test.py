import hashlib

password = "trololo"
md5 = hashlib.md5(password.encode())

print("The corresponding hash is : ")
print(md5.hexdigest());