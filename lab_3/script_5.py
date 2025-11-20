class AuthManager:
    MAX_AGE = 150
    MIN_AGE = 0

    def valid_age(self, age):
        return self.MIN_AGE <= age <= self.MAX_AGE
