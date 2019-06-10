import random
import math


def isPrime(n):
	if n%2 == 0 : return False
	i = 3
	prime = True
	while i < n**0.5 :
		if n % i == 0 :
			prime = False
			break
		i += 2
	return prime


def primesUnder(M):
	primes = [2]+[i for i in range(3,M+1,2) if isPrime(i)]
	return primes


def choose(primes) :
	p,q = random.choice(primes),random.choice(primes)
	return p,q

def phi(p,q):
	return (p-1)*(q-1)

def generatePublicKey(p,q): 
	n = p*q
	for i in range(2,phi(p,q)) :
		if math.gcd(i,phi(p,q)) == 1 :
			e = i
			break
	return n,e

def generatePrivateKey(p,q,encryptor):
	k = 2
	while True :
		if (1+k*phi(p,q))%encryptor == 0 : 
			decryptor = (1+k*phi(p,q))//encryptor
			break
		else :
			k += 1
	return decryptor

def convertToNumbers(text):
	return [ord(ch) for ch in text ]

def convertToText(Numbers) :
	return ''.join([chr(num) for num in Numbers])

def RSA_encrypt(msg,n,encryptor):
	msg_num = convertToNumbers(msg)
	msg_encrypted = [(cypher**encryptor)%n for cypher in msg_num]
	return msg_encrypted

def RSA_decrypt(msg_encrypted,n,decryptor):
	msg_decrypted_num = [(cypher**decryptor)%n for cypher in msg_encrypted]
	msg_decrypted = convertToText(msg_decrypted_num)
	return msg_decrypted

#initiating RSA example :
p,q = choose(primesUnder(1000))
n,encryptor = generatePublicKey(p,q)
decryptor = generatePrivateKey(p,q,encryptor)
msg = 'Hello World'
msg_encrypted = RSA_encrypt(msg,n,encryptor)
msg_decrypted = RSA_decrypt(msg_encrypted,n,decryptor)

print('p = ',p,' q = ',q,' n = ',n,' encryptor = ',encryptor,' decryptor = ',decryptor)
print('message before encryption : ',msg)
print('message after encryption : ',msg_encrypted)
print('message decryption : ',msg_decrypted)
