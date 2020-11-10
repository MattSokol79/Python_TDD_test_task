# This is the code file

# Creating the code class for the modulus/non_zero task
class Modulus_Calc:

    # Function that output True if value1 / value 2 has NO remainder
    def modulus(self, value1, value2):
        if value1 % value2 == 0:
            return True
        else:
            return False

    # Function that outputs False if any value is < 0, True if it is above 0
    def not_zero(self, value1, value2):
        if value1 and value2 > 0:
            return True
        else:
            return False