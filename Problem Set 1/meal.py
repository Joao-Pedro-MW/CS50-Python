def main():
    tempo = str(input("Informe a hora: "))
    return convert(tempo)
def convert(time):
    time = time.rsplit(":")
    HH,MM = int(time[0]),int(time[1])
    #Morning
    if HH == 7 or (HH == 8 and MM == 0):
        return print("breakfast time")
    #MidDay
    elif HH == 12 or (HH == 13 and MM == 0):
        return print("lunch time")
    #Night
    elif HH == 18 or (HH == 19 and MM == 0):
        return print("dinner time")
    else:
        pass
if __name__ == "__main__":
    main()