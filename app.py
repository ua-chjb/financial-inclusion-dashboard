from dash import Dash


from index import lyt
from callbacks import callbacks_baby

app = Dash(__name__)

app.layout = lyt

callbacks_baby(app)

server = app.server

if __name__=="__main__":
    app.run(debug=True, port="8888")