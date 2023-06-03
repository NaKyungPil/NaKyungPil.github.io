import FinanceDataReader as fd
import plotly.graph_objects as go
from datetime import datetime
from dateutil.relativedelta import relativedelta

start_date = datetime.today()-relativedelta(years=2)
end_date = datetime.today()
df = fd.DataReader('KS11',start_date,end_date)
latest_price = df['Close'][-1]
previous_price = df['Close'][-2]
price_change = latest_price - previous_price
price_change_percentage = (price_change / previous_price) * 100




# https://plotly.com/python/statistical-charts/ 참조

fig = go.Figure(data=go.Scatter(x=df.index,y=df['Close']))
fig.update_layout(xaxis=dict(title=None,tickmode='array',tickvals=[]),yaxis=dict(title=None,tickmode='array',tickvals=[]))
fig.update_layout(margin=dict(l=0,r=0,t=0,b=0))

html = 'C:/Users/ktf98/OneDrive/바탕 화면/웹프/G.I/코스피.html'
fig.write_html(html)
