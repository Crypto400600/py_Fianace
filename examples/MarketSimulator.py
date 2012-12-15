from datetime import datetime
from finance.utils.BasicUtils import *
from finance.sim import MarketSimulator

sim = MarketSimulator()
sim.set_initial_cash(1000000)
sim.load_trades("MarketSimulator_orders.csv")
sim.simulate()
portfolio = sim.get_portfolio()
#print(portfolio.ix[0:10])
#print(portfolio.ix[datetime(2011, 2, 18)])

print('Total Return:', total_return(portfolio))
print(sharpe_ratio(portfolio, extraAnswers=True))

print('Total Return:', total_return(portfolio, 'Portfolio'))
print(sharpe_ratio(portfolio, 'Portfolio', extraAnswers=True))