import FinanceDataReader as fd
import plotly.graph_objects as go
from datetime import datetime
from dateutil.relativedelta import relativedelta

start_date = datetime.today()-relativedelta(years=2)
end_date = datetime.today()
df = fd.DataReader('006400',start_date,end_date)


# https://plotly.com/python/statistical-charts/ 참조

fig = go.Figure(data=go.Scatter(x=df.index,y=df['Close']))
fig.update_layout(title='삼성SDI',xaxis_title='날짜',yaxis_title='주가')

html = 'C:/Users/ktf98/OneDrive/바탕 화면/웹프/G.I/삼성SDI.html'
fig.write_html(html)