import hashlib

password = "yanis"
password_hash = hashlib.md5(password.encode("UTF-8")).hexdigest()
print(f"The MD5 hash for 'yanis' is: {password_hash}")
