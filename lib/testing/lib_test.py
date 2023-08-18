#!/usr/bin/env python3

import io
import sys
from functions import greet_programmer, greet, greet_with_default, add, halve

class TestGreetProgrammer:
    def test_greet_programmer(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_programmer()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello, programmer!"

class TestGreet:
    def test_greet(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet("Guido")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello, Guido!"

class TestGreetWithDefault:
    def test_greet_with_default(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_with_default()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello, programmer!"

    def test_greet_with_default_with_param(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_with_default("Guido")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello, Guido!"

class TestAdd:
    def test_add(self):
        assert add(45, 55) == 100

class TestHalve:
    def test_halve_int(self):
        assert halve(100) == 50

    def test_halve_float(self):
        assert halve(99.0) == 49.5
