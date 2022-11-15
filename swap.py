


week_a = "a"
week_b = "b"

current_value = week_a
i = 2

for i in range(0, 10):
    print(current_value)
    if current_value == week_a:
        current_value = week_b
    elif current_value == week_b:
        current_value = week_a
