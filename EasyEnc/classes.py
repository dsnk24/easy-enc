import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


class KeyGenerator:
	"""The Key Generator class does what the name suggests. It generates random keys with which you can encrypt your messages."""

	def generate_key(self, key_object="ncof248tnp0q8yhndfouwlbUuigifebceiyVIibfoeQR44VD44biuwa"):
		"""generate_key() function takes one argument: key_object, which is required to make a custom randomized key"""
		"""I highly recommend not leaving this to the default key_object value if you use it for serious purposes, because anyone with this module would be able to decrypt the data you encrypt."""

		key_obj = key_object.encode()

		salt = b"\x8b\xa0\xe9Z4\xfbB`P\x95\xaf\xe1\xd4\x8bE\x04\x08\xce\xa1\x84\x95K\xdb\xa4>\x9a=/\xed'\xe0\x16"

		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=100000,
			backend=default_backend()
		)

		key = base64.urlsafe_b64encode(kdf.derive(key_obj))

		return key
	

	def generate_key_in_file(self, key_object="ncof248tnp0q8yhndfouwlbUuigifebceiyVIibfoeQR44VD44biuwa", filename="key.key"):
		"""generate_key_in_file() function serves the same purpose of the generate_key() function but it automatically stores the key in a file"""
		"""If no file name is included (make sure to include the extension you desire, as long as it's not a binary), then the module will automatically save it in a key.key file."""
	
		key_obj = key_object.encode()

		salt = b"\x8b\xa0\xe9Z4\xfbB`P\x95\xaf\xe1\xd4\x8bE\x04\x08\xce\xa1\x84\x95K\xdb\xa4>\x9a=/\xed'\xe0\x16"

		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=100000,
			backend=default_backend()
		)

		key = base64.urlsafe_b64encode(kdf.derive(key_obj))

		with open(f"{filename}", "wb") as f:
			f.write(key)


	def store_key(self, filename="key.key", key=None):
		"""store_key() function stores the key, you generate in the key.key file by default, if no filename is specified."""
		"""It takes 2 parameters: a filename, and a key object."""

		if key != None:
			file = open(filename, "wb")
			file.write(key)
			file.close()

			if filename == "key.key":
				print(f"Stored key in the '{filename}' file because no filename was specified.")
			else:
				print(f"Stored key in the '{filename}' file.")
		else:
			print("No key to store specified.")
	

	def get_key(self, filename="key.key"):
		"""get_key() function fetches the key from the key.key file by default, if no filename is specified."""
		"""It takes only one parameter: a filename."""

		file = open(filename, "rb")
		key = file.read()
		file.close()

		return key


class Encryptor:
	"""Similarly to the KeyGenerator class, this one also does exactly as the name suggests. It encrypts and decrypts messages and data."""
	
	def encrypt_message(self, msg_data="".encode(), key=None):
		"""encrypt_message() function uses a key you generated with the KeyGenerator class to encrypt a string you pass it."""
		"""It takes 2 parameters: a string and a key object."""

		if key != None:
			fernet = Fernet(key)
			enc_msg = fernet.encrypt(msg_data.encode())

			return enc_msg.decode()
		else:
			print("No key to encrypt with.")
	

	def decrypt_message(self, msg_data="".encode(), key=None):
		"""decrypt_message() function uses a key with which you have previously encrypted a message and tries to decrypt it. If it's the correct key, you will see your original message."""
		"""It also takes 2 parameters: a string and a key object."""

		if key != None:
			fernet = Fernet(key)
			dec_msg = fernet.decrypt(msg_data.encode())

			return dec_msg.decode()
		
		else:
			print("No key to decrypt with.")