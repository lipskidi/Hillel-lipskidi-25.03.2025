time = int(input("Enter time in seconds (0 - 8640000): "))
day, remaining = divmod(time, 86400)
hour, remaining = divmod(remaining, 3600)
minut, sec = divmod(remaining, 60)
hour_str = str(hour).zfill(2)
minut_str = str(minut).zfill(2)
sec_str = str(sec).zfill(2)
if day == 1:
    day_word = "День"
elif 2 <= day <=4:
    day_word = "Дні"
else:
    day_word = "Днів"
print(f"{day} {day_word} {hour_str}:{minut_str}:{sec_str}")
