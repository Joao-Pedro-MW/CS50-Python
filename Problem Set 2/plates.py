def check_numbers(txt):
    numbersCount = 0
    numbersList = list()
    for char in txt:
        if char.isnumeric() == True:
            #count the numbers in the input
            numbersCount += 1
            #get numbers from the input
            numbersList.append(int(char))
        #check if the plate has a number
        #check 6 and 2 numbers
    if numbersCount == 0: return True
    else:
        if (numbersCount >= 2)  and  (numbersCount <= 6):
            #check for the middle numbers
            s = txt[0:-2]
            if s.isalpha() == True:
                #check if the first input equals 0
                if numbersList[0] == 0: return False
                else: return True
        else: return False
def has_char(txt):
    #start with at least two letters
    txt_ = txt[0:2]
    if len(txt_) == 2:
        if txt_.isalpha() == True:
            if (" " in txt) or ("," in txt) or ("." in txt): return False
            else: return True
def chk_len(txt):
    #check input length
    len_txt = len(txt)
    if (len_txt < 2) or (len_txt > 6): return False
    else: return True
def is_valid(s):
    if chk_len(s):
        if has_char(s):
            if check_numbers(s): return True
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
main()
#made by mw.jao