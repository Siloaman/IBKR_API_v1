def outstanding_orders():
    
    # testing
    current_time = datetime.datetime.now()
    testing_details.append("Getting Time OO: ")
    testing_details.append(str(current_time))  # so we know if the schedule is on point with minute starts!!
    
    trads = ib.trades()
    ords = ib.orders()
    
    testing_details.append("current list of open orders: ")
    testing_details.append(ords)
    testing_details.append("current list of trades: ")
    testing_details.append(trads)
    
    for order_entry in pending_stop_loss_orders:
        
        if(order_entry[4] == "SELL"):
            
            trad_num = -404
            ords = len(trads)
            
            for x in range(ords):
                if(trads[x].order.orderId == order_entry[2]):
                    trad_num = x
            
            
            if(trad_num != -404):
                
                contract = Stock(order_entry[0], 'SMART', 'USD')
                ib.qualifyContracts(contract)
                data = ib.reqMktData(contract)
                ib.sleep(2)
                current_price = round(data.marketPrice(), 2)           
            
                # WONT THESE +10% activate every 5 minutes all day????
                
                # testing
                current_time = datetime.datetime.now()
                testing_details.append("Attempting stock SL updating\n")
                testing_details.append(str(current_time) + "\n\n") 
            
                # current price OVER average buy price
                if((current_price / order_entry[3]) > 1.5):
                    trads[trad_num].order.auxPrice = round((order_entry[3] * 1.32), 2)
                    trads[trad_num].order.lmtPrice = round((order_entry[3] * 1.30), 2)
                    return
                elif((current_price / order_entry[3]) > 1.3):
                    trads[trad_num].order.auxPrice = round((order_entry[3] * 1.12), 2)
                    trads[trad_num].order.lmtPrice = round((order_entry[3] * 1.10), 2)
                    return
                elif((current_price / order_entry[3]) > 1.12):
                    trads[trad_num].order.auxPrice = round((order_entry[3] * 1.06), 2)
                    trads[trad_num].order.lmtPrice = round((order_entry[3] * 1.04), 2)
                    # testing
                    current_time = datetime.datetime.now()
                    testing_details.append("Stock has surpassed +10% - grabbing profit stop loss\n")
                    testing_details.append(str(order_entry[0]) + " has its SL moved to: " + str(trads[trad_num].order.auxPrice))
                    testing_details.append(str(current_time) + "\n\n") 
                    return
                else:
                    return



def order_status(trade, fill):
    
    # I should probably still check if the status is FILLED before moving forward with a stop order to sell them!!!
    # fill in the orderstatus part after I confirm the rest of this stuff works...
    
    for order_entry in pending_stop_loss_orders:
        if(order_entry[2] == fill.execution.orderId):
            
            contract = Stock(fill.contract.symbol, 'SMART', 'USD')
            # stop limit with limit at 1.5 percent below Marubozu "low" and stop at the "low" .... not sure i like this...
            stopOrder = StopLimitOrder('SELL', fill.execution.shares, round((order_entry[3] - 0.03), 2), order_entry[3])
            stopOrderTrade = ib.placeOrder(contract, stopOrder)




'''
['KDLY', 50, 1862, 2.23, 'BUY'],
 ['KDLY', 1.0, 1932, 3.36, 'SELL'],
 ['NXU', 1.0, 2035, 0.42, 'SELL'],
 ['SPGC', 1.0, 2094, 0.58, 'SELL'],
 ['MYNA', 1.0, 2167, 0.39, 'SELL'],
 ['SPGC', 1.0, 2233, 0.73, 'SELL'],
 ['MYNA', 1.0, 2323, 0.38, 'SELL'],
 ['NKGN', 1.0, 2339, 0.54, 'SELL'],
 ['YHC', 1.0, 2340, 1.1, 'SELL'],
 ['KDLY', 1.0, 2545, 3.72, 'SELL'],
 ['MYNA', 270, 2593, 0.44, 'BUY'],
 ['NKGN', 1.0, 2600, 0.69, 'SELL'],
 ['XLO', 80, 2658, 1.56, 'BUY'],
 ['MYNA', 1.0, 2668, 0.61, 'SELL']
'''
