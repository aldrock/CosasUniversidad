#!/usr/bin/python
import pdb

def auth(username):
	if len(username) < 6:
		print("El nombre de usuario debe contener al menos 6 caracteres")
		return False
	if len(username) > 12:
		print("El nombre de usuario no puede contener más de 12 caracteres")
		return False
	if not username.isalnum():
		print("El nombre de usuario puede contener solo letras y números")
		return False
	return True

def pwd(passwd):
	if len(passwd) < 8:
		print("La contraseña elegida no es segura")
		return False
	caps, low, num, noalpha = False, False, False, False
	pdb.set_trace()
	for i in passwd:
		if not i.isalnum():
			noalpha = True
			continue
		if i.isnumeric():
			num = True
			continue
		if not i.islower():
			caps = True
			continue
		if i.islower():
			low = True
			continue
		break

	is_secure = caps and low and num and noalpha
	if not is_secure:
		print("La contraseña elegida no es segura")
		return False
	return True
