
num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jly", "Aug", "Sept", "Oct", "Nov", "Dec"]

new_dict = dict()

for i, j in zip(months, num_days):
    new_dict.update({i:j})

    if new_dict[i] < 29:
        continue

    else:
        print(i, "Month has", new_dict[i], "days")

        
