# This is the code file

# Creating the code class for the modulus/non_zero task
class Modulus_Calc:

    # Function that outputs True if value1 / value 2 has NO remainder i.e. == 0
    def modulus(self, value1, value2):
        if value1 % value2 == 0:
            return True
        else:
            return False

    # Function that outputs True if both values are > 0, False if < 0
    def not_zero(self, value1, value2):
        if value1 and value2 > 0:
            return True
        else:
            return False