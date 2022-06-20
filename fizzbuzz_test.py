import pytest
from unittest import TestCase

from fizzbuzz import FizzBuzz


class FizzBuzzTest(TestCase):

   @pytest.fixture(autouse=True)
   def fizzBuzz(self):
        self._fizzBuzz = FizzBuzz()
        yield

   def test_it_should_return_a_number(self):
        assert  self._fizzBuzz.of(1) == "1"
        assert  self._fizzBuzz.of(2) == "2"
        assert  self._fizzBuzz.of(4) == "4"
        assert  self._fizzBuzz.of(7) == "7"
        assert  self._fizzBuzz.of(8) == "8"
        assert  self._fizzBuzz.of(11) == "11"
        assert  self._fizzBuzz.of(13) == "13"
        assert  self._fizzBuzz.of(14) == "14"


   def test_it_should_returns_Fizz(self):
        assert  self._fizzBuzz.of(3) == "Fizz"
        assert  self._fizzBuzz.of(6) == "Fizz"
        assert  self._fizzBuzz.of(9) == "Fizz"
   
   def test_it_should_returns_Buzz(self):
        assert  self._fizzBuzz.of(5) == "Buzz"
        assert  self._fizzBuzz.of(10) == "Buzz"

   def test_it_should_returns_FizzBuzz(self):
        assert  self._fizzBuzz.of(15) == "FizzBuzz"