# Se importan Las librerias
import dash
from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from PIL import Image

# Se importa el franted
from frontend.Presentacion import presentacion, Finalizacion
from backend.respuesta_sismica import Tituto1, RespuestaSismica, Division, Poblacion_RespuestaSismica
from backend.respuesta_sismica import DensidadPoblacional, consultarLocalidad
from frontend.Zonificacion_Geotecnica import zonificacionGeotecnica
from frontend.Geologia_Urbana import GeologiaUrbana
from frontend.Geologia_Rural import Geologiarural


# Cuerpo de la aplicación
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    presentacion,
            dbc.Row([
            dbc.Col(Tituto1, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(RespuestaSismica, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(Poblacion_RespuestaSismica, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr()
    ]
    )

@app.callback(
    Output("mapa", "figure"),
    Input("localidad_consultada", "value")
)

def update_map(localidad_consultada):
    return consultarLocalidad(localidad_consultada)


if __name__ == '__main__' :
    app.run_server(debug=True)
