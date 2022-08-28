def main():
    txt = str(input())
    convert(txt)
def convert(text):
    text = text.replace(":(","🙁")
    text = text.replace(":)","🙂")
    return print(text)
main()