import random, string

size = 16

chars = string.ascii_letters + string.digits + '!@#$%*()_=+çßüäå§жбой '

rnd = random.SystemRandom() # os.urandom

print(''.join(rnd.choice(chars) for i in range(size)))