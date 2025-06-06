# https://schedule.readthedocs.io/en/stable/examples.html#
# schedule.every().minute.at(":17").do(job)    # can i flip between (":00") and (":05") ???
# schedule.every().day.at("10:30").do(job)
# schedule.every().wednesday.at("13:15").do(job)

time_slot_list = [ "9:35", "9:40", "9:45", "9:50", "9:55", "10:00", 
                  "10:05", "10:10", "10:15", "10:20", "10:25", "10:30", "10:35", "10:40", "10:45", "10:50", "10:55", "11:00", 
                  "11:05", "11:10", "11:15", "11:20", "11:25", "11:30", "11:35", "11:40", "11:45", "11:50", "11:55", "12:00", 
                  "12:05", "12:10", "12:15", "12:20", "12:25", "12:30", "12:35", "12:40", "12:45", "12:50", "12:55", "13:00",
                  "13:05", "13:10", "13:15", "13:20", "13:25", "13:30", "13:35", "13:40", "13:45", "13:50", "13:55", "14:00", 
                  "14:05", "14:10", "14:15", "14:20", "14:25", "14:30", "14:35", "14:40", "14:45", "14:50", "14:55", "15:00", 
                  "15:05", "15:10", "15:15", "15:20", "15:25", "15:30", "15:35", "15:40", "15:45", "15:50", "15:55" ]

def order_status(trade, fill):
  # can i actually grab trade.orderstatus.status == "Filled" or not ?? I need to make sure I don't mess up my accounting with incomplete blocks of assets being accounted for..


def start_trading_loop():
  schedule.every().minute.at(":00").until("16:00").do(job)
  schedule.every().minute.at(":05").until("16:00").do(job)
  schedule.every().minute.at(":10").until("16:00").do(job)
  schedule.every().minute.at(":15").until("16:00").do(job)
  schedule.every().minute.at(":20").until("16:00").do(job)
  schedule.every().minute.at(":25").until("16:00").do(job)
  schedule.every().minute.at(":30").until("16:00").do(job)
  schedule.every().minute.at(":35").until("16:00").do(job)
  schedule.every().minute.at(":40").until("16:00").do(job)
  schedule.every().minute.at(":45").until("16:00").do(job)
  schedule.every().minute.at(":50").until("16:00").do(job)
  schedule.every().minute.at(":55").until("16:00").do(job)


# Schedule the task to start every day at 9:44AM
schedule.every().day.at("09:44").do(start_trading_loop)
while True:
    schedule.run_pending()  


# Each code.py is tied to a unique user account # ( so that it cannot be infinitely shared with friends )
# Max of 4 on-going trades at a time with a max of $2500 USD per trade [ max $10,000 USD at any time ]
# Excess funds are redirected into divvy stocks
