
days =  {
    "1: Sunday",
    "2: Monday",
    "3: Tuesday",
    "4: Wednesday",
    "5: Thursday",
    "6: Friday",
    "7: Saturday"
}
print(len(days))
days_inp = int(input("what day is it: "))

if days_inp > len(days):
     print("wrong input")
else:
    print(f" you picked {days.get(str(days_inp))}")
