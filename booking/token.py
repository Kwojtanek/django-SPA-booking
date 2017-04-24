import string, random


class RandomTokenGenerator(object):
    def __init__(self, chars=None, random_generator=None):
        self.chars = chars or string.ascii_uppercase + string.ascii_lowercase + string.digits
        self.random_generator = random_generator or random.SystemRandom()

    def make_token(self,n):
        return ''.join(self.random_generator.choice(self.chars) for _ in range(n))

token_generator = RandomTokenGenerator()