from plates import is_valid
def main():
    test_lenght()
    test_letters()
    test_invalid_char()
    test_alphanum()
def test_letters():
    assert is_valid("HI") == True
    assert is_valid("CS") == True
    assert is_valid("485") == False
def test_lenght():
    assert is_valid("OUTATIME") == False
    assert is_valid("CSMIMOM") == False
def test_invalid_char():
    assert is_valid("AA*/*22") == False
    assert is_valid("MAM.MAM") == False
    assert is_valid("Hi, john") == False
def test_alphanum():
    assert is_valid("MM48")==True
    assert is_valid("AAA28")==True
    assert is_valid("AA24A")==False
    assert is_valid("MM48 U")==False
    assert is_valid("CAR05")==False
    assert is_valid("CS50")==True

if __name__ == "__main__":
    main()