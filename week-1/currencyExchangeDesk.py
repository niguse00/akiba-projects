exchange_rate = 150
usdAmount = float(input("enter usd amount: "))
etbAmount = usdAmount * exchange_rate
line = "=============================="
title = "CURRENCY EXCHANGE"

print(f"""
{line}
        {title}
{line}

USD Amount: {usdAmount}

Exchange Rate: 1 USD = {exchange_rate} ETB

ETB Amount: {etbAmount} ETB
{line}

""")