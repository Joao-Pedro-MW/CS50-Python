from twttr import shorten
def test_twttr():
    assert shorten("Hi") == "H"
    assert shorten("MAke Me Fall") == "Mk M Fll"
    assert shorten("041 Hi, from mom") == "041 H, frm mm"
if __name__ == "__main__":
    main()