class FizzBuzz:
    def of(self, number):  # sourcery skip: assign-if-exp, reintroduce-else
        if(number % 3 == 0 and number % 5 == 0):
            return "FizzBuzz"
        elif(number % 3 == 0):
            return "Fizz"
        elif(number % 5 == 0):
            return "Buzz"

        return str(number)
