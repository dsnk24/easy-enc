import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


class KeyGenerator:
	def generate_key(self, key_object="ncof248tnp0q8yhndfouwlbUuigifebceiyVIibfoeQR44VD44biuwa"):
		key_obj = key_object.encode()

		salt = b"\x8b\xa0\xe9Z4\xfbB`P\x95\xaf\xe1\xd4\x8bE\x04\x08\xce\xa1\x84\x95K\xdb\xa4>\x9a=/\xed'\xe0\x16"

		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=64,
			salt=salt,
			iterations=100000,
			backend=default_backend()
		)

		key = base64.urlsafe_b64encode(kdf.derive(key_obj))

		return key
	

	def generate_key_in_file(self, key_object="ncof248tnp0q8yhndfouwlbUuigifebceiyVIibfoeQR44VD44biuwa"):
		key_obj = key_object.encode()

		salt = b"\x8b\xa0\xe9Z4\xfbB`P\x95\xaf\xe1\xd4\x8bE\x04\x08\xce\xa1\x84\x95K\xdb\xa4>\x9a=/\xed'\xe0\x16"

		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=64,
			salt=salt,
			iterations=100000,
			backend=default_backend()
		)

		key = base64.urlsafe_b64encode(kdf.derive(key_obj))

		with open("key.key", "wb") as f:
			f.write(key)


	def store_key(self, filename="key.key", key="null"):
		if key != "null":
			file = open(filename, "wb")
			file.write(key)
			file.close()
		else:
			print("No key specified. Saved key as null.")

		if filename == "key.key":
			print("Stored key in the key.key file because no filename was specified.")
		else:
			print(f"Stored key in the {filename} file.")
	

	def get_key(self, filename="key.key"):
		file = open(filename, "rb")
		key = file.read()
		file.close()

		return key


class Encryptor:
	def encrypt_message(self, msg_data="", key="null"):
		if key != "null":
			fernet = Fernet(key)
			enc_msg = fernet.encrypt(msg_data)

			return enc_msg
		else:
			print("No key to encrypt with.")
	

	def decrypt_message(self, msg_data="", key="null"):
		if key != "null":
			fernet = Fernet(key)
			dec_msg = fernet.decrypt(msg_data)

			return dec_msg
		
		else:
			print("No key to decrypt with.")