import datetime
hnow = datetime.datetime.now().hour
mnow = datetime.datetime.now().minute
nowtime = hnow, mnow 

dhou = {0:["двенадцать часов", "первого"], 1:["один час", "второго"], 2:["два часа", "третьего"], 
      3:["три  часа", "четвёртого"], 4:["четыре часа", "пятого"], 5:["пять часов", "шестого"], 
      6:["шесть часов", "седьмого"], 7:["семь часов", "восьмого"], 8:["восемь часов", "девятого"], 
      9:["девять часов", "десятого"], 10:["десять часов", "одиннадцатого"], 11:["одиннадцать часов", "двенадцатого"], 
      12:["двенадцать часов", "первого"], 13:["один час", "второго"], 14:["два часа", "третьего"], 
      15:["три часа", "четвертого"], 16:["четыре часа", "пятого"], 17:["пять часов", "шестого"], 
      18:["шесть часов", "седьмого"], 19:["семь часов", "восьмого"], 20:["восемь часов", "девятого"], 
      21:["девять часов", "десятого"], 22:["десять часов", "одиннадцатого"], 23:["одиннадцать часов", "двенадцатого"]}
dmin = {0:["ровно"], 1: ["одна минута"], 2: ["две минуты"], 3: ["три минуты"], 4: ["четыре минуты"], 5: ["пять минут"], 6: ["шесть минут"], 7: ["семь минут"], 8: ["восемь минут"], 
      9: ["девять минут"], 10: ["десять минут"], 11: ["одиннадцать минут"], 12: ["двенадцать минут"], 13:["тринадцать минут"], 14:["четырнадцать минут"], 
      15:["пятнадцать минут"], 16:["шестнадцать минут"], 17:["семнадцать минут"], 18:["восемнадцать минут"], 19:["девятнадцать минут"], 20:["двадцать минут"], 
      21:["двадцать одна минута"], 22:["двадцать две минуты"], 23:["двадцать три минуты"], 24:["двадцать четыре минуты"], 25:["двадцать пять минут"], 26:["двадцать шесть минут"], 
      27:["двадцать семь минут"], 28:["двадцать восемь минут"], 29:["двадцать девять минут"], 30:["половина"], 31:["тридцать одна минута"], 32:["тридцать две минуты"], 
      33:["тридацать три минуты"], 34:["тридцать четыре минуты"], 35:["тридцать пять минут"], 36:["тридцать шесть минут"], 37:["тридцать семь минут"], 38:["тридцать восемь минут"], 
      39:["тридцать девять минут"], 40:["сорок минут"], 41:["сорок одна минута"], 42:["сорок две минуты"], 43:["сорок три минуты"], 44: ["сорок четыре"], 
      45: ["без петнадцати минут"], 46:["без четырнадцати минут"], 47:["без тринадцати минут"], 48:["без двенадцати минут"], 49:["без одиннадцати минут"], 50:["без десяти минут"], 
      51:["без девяти минут"], 52:["без восьми минут"], 53:["без семи минут"], 54:["без шести минут"], 55:["без пяти минут"], 56:["без четырёх минут"], 57:["без трёх минут"], 58:["без двух минут"], 59:["без одной минуты"]}

enter = input("what time are you interested now or your?\n Enter 'now time' or 'hh:mm'\n")

hhmm = enter.split(':')
hh = int()
mm = int()


if enter == ("now time"):
      h = dhou[hnow]
      m = dmin[mnow]
      if m == dmin[0]:
            print(f"{h[0]} {m[0]}")
      if m < dmin[30]:
            print(f"{m[0]} {h[1]}")
      if m == dmin[30]:
            print(f"{m[0]} {h[1]}")
      if m > dmin[30] and m < dmin[45]:
            print(f"{m[0]} {h[1]}")
      if m >= dmin[45]:
            print(f"{m[0]} {h[1]}")
else:
      enter == (hhmm)
      hhy = dhou[hh]
      z = dmin[mm]
      if z == dmin[0]:
            print(f"{hhy[0]} часа {z[0]}")
      if z < dmin[30]:
            print(f"{z[0]} {hhy[1]}")
      if z == dmin[30]:
            print(f"{z[0]} {hhy[1]}")
      if z > dmin[30] and z < dmin[45]:
            print(f"{z[0]} {hhy[1]}")
      if z >= dmin[45]:
            print(f"{z[0]} {hhy[1]}")
      print("sorry")