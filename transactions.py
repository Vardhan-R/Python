import datetime, matplotlib.pyplot as plt, numpy as np, time

fp = open("transactions.txt", 'r')
raw_data = fp.readlines()
fp.close()

dates = [raw_data[x][:-1] for x in range(0, len(raw_data), 2)]
amt = [(2 * int(raw_data[x].split(" ")[0] == "Received") - 1) * float(raw_data[x].split(" ")[1][3:]) for x in range(1, len(raw_data), 2)]

e = time.mktime(datetime.datetime(int(dates[0][:4]), int(dates[0][4:6]), int(dates[0][6:])).timetuple())
s = time.mktime(datetime.datetime(int(dates[-1][:4]), int(dates[-1][4:6]), int(dates[-1][6:])).timetuple())
n_dates = np.linspace(s, e, round((e - s) / 86400 + 1))
n_amt = np.zeros(n_dates.size)

for i in range(len(dates)):
    unix_tm = time.mktime(datetime.datetime(int(dates[i][:4]), int(dates[i][4:6]), int(dates[i][6:])).timetuple())
    n_amt[round((unix_tm - s) / 86400)] += amt[i]

# print((n_dates - s) / 86400 + 1)
# print(n_amt)

tm_tpl = datetime.datetime.now().timetuple()
days_till_nxt_month = np.ceil((time.mktime(datetime.datetime(tm_tpl.tm_year + tm_tpl.tm_mon // 12, tm_tpl.tm_mon % 12 + 1, 1).timetuple()) - time.mktime(tm_tpl)) / 86400)
days_from_prev_month = round(np.ceil((time.mktime(tm_tpl) - time.mktime(datetime.datetime(tm_tpl.tm_year, tm_tpl.tm_mon, 1).timetuple())) / 86400))
money_remaining = round(3000 + np.sum(n_amt[-days_from_prev_month:]), 2)
print(f"You have Rs. \033[38;2;255;0;0m{money_remaining}\033[0m to spend for the rest of this month.")
print(f"You can spend Rs. \033[38;2;0;255;0m{round(money_remaining / days_till_nxt_month, 2)}\033[0m, on average, each day for the rest of this month.")
print(f"Your net gain since the start is Rs. \033[38;2;100;200;250m{np.sum(n_amt)}\033[0m.")

plt.plot((n_dates - s) / 86400 + 1, n_amt)
plt.title("Transactions")
plt.xlabel("Day")
plt.ylabel("Amount")
plt.show()