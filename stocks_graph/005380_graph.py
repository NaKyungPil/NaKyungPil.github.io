import FinanceDataReader as fd
import plotly.graph_objects as go
from datetime import datetime
from dateutil.relativedelta import relativedelta

start_date = datetime.today()-relativedelta(years=2)
end_date = datetime.today()
df = fd.DataReader('005380',start_date,end_date)


# https://plotly.com/python/statistical-charts/ 참조

fig = go.Figure(data=go.Scatter(x=df.index,y=df['Close']))
fig.update_layout(title='현대차',xaxis_title='날짜',yaxis_title='주가')

html = 'C:/Users/ktf98/OneDrive/바탕 화면/웹프/G.I/현대차.html'
fig.write_html(html)
