import FinanceDataReader as fd
import plotly.graph_objects as go
from datetime import datetime
from dateutil.relativedelta import relativedelta

start_date = datetime.today()-relativedelta(years=2)
end_date = datetime.today()
df = fd.DataReader('005930',start_date,end_date)
latest_price = df['Close'][-1]
previous_price = df['Close'][-2]
price_change = latest_price - previous_price
price_change_percentage = (price_change / previous_price) * 100




# https://plotly.com/python/statistical-charts/ 참조

fig = go.Figure(data=go.Scatter(x=df.index,y=df['Close']))
fig.update_layout(title='삼성전자 현재가: {:.2f} ( {:.2f}%)'.format(latest_price,price_change_percentage),xaxis_title='날짜',yaxis_title='주가')

html = 'C:/Users/ktf98/OneDrive/바탕 화면/웹프/G.I/삼성전자.html'
fig.write_html(html)
