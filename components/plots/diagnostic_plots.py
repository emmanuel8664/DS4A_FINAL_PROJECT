import plotly.express as px

def get_bar(df, eje_x, eje_y):
    fig = px.bar(df, x=eje_x, y=eje_y)
    #fig = px.box(df, x=eje_x, y = eje_y, title = 'SC'+' - '+'Alicia')
    #print(type(df.plot()    ))
    #print(type(fig))
    return fig#df.plot(x=eje_x, y = eje_y, figsize=(15,7), title = 'SC'+' - '+'Alicia')
def get_boxplot(df, eje_x, eje_y):
    print(df.columns)
    print(eje_x)
    print(eje_y)
    fig = px.box(df, x=eje_x, y="mean")
    
    
    #fig = px.box(df, x=eje_x, y = eje_y, title = 'SC'+' - '+'Alicia')
    #print(type(df.plot()    ))
    #print(type(fig))
    return fig#df.plot(x=eje_x, y = eje_y, figsize=(15,7), title = 'SC'+' - '+'Alicia')
def get_scatter(df, eje_x, eje_y):
    fig = px.scatter(df, x=eje_x, y=eje_y)
    #fig = px.box(df, x=eje_x, y = eje_y, title = 'SC'+' - '+'Alicia')
    #print(type(df.plot()    ))
    #print(type(fig))
    return fig#df.plot(x=eje_x, y = eje_y, figsize=(15,7), title = 'SC'+' - '+'Alicia')