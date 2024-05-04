# Se importan Las librerias

import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from PIL import Image
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go

#token = open(".mapbox_token").read()

# Se crean las variables para ser insertadas en el Container de respuesta sísmica

Tituto1 = html.H3('Zonas de Respuesta Sismica')



Localidades = gpd.read_file('data\Localidades')
ZonaSismica = gpd.read_file('data\Respuesta Sísmica')
DensidadPoblacional=gpd.read_file('data\Centroides_Manzanas.geojson')

def consultarLocalidad(localidad_consultada):

    localidad_buscada = Localidades.query(f"LocNombre == '{localidad_consultada}'")

    localidad_buscada_4326 = localidad_buscada.to_crs(epsg=4326)
    ZonaSismica_4326 = ZonaSismica.to_crs(epsg=4326)

    ZonaSismica_Localidad = gpd.overlay(
    localidad_buscada_4326, ZonaSismica_4326, how='intersection')
    




    # Genera mapa de localidades
    #fig = px.choropleth_mapbox(
     #   geojson=localidad_buscada_4326.geometry,
      #  locations=localidad_buscada_4326.index
    #)

    ZonaSismica_Localidad_grafica=px.ZonaSismica_Localidad.election()
    geojson = px.ZonaSismica_Localidad.election_geojson()

    fig = px.choropleth_mapbox(ZonaSismica_Localidad_grafica, geojson=geojson, color="Bergeron",
                            locations="district", featureidkey="properties.district",
                            center={"lat": 45.5517, "lon": -73.7073},
                            mapbox_style="carto-positron", zoom=9)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    def consultarZonaSismica(ZonaSismica_consultada):
        ZonaSismica_consultada = ZonaSismica_Localidad.query(f"RESSIS == '{ZonaSismica_consultada}'")
        DensidadPoblacional_4326=DensidadPoblacional.to_crs(epsg=4326)

        ZonaSismica_Poblacion= gpd.overlay(
            DensidadPoblacional_4326, ZonaSismica_consultada, how='intersection')
        
        Total_habitantes=  ZonaSismica_Poblacion["PER_S010"].sum()


        return 'El total de habitantes de la localidad de' + str(localidad_buscada) +'ubicados en una zonificación del suelo de respuesta sismica' + str(ZonaSismica_consultada) + 'es de' + str(Total_habitantes)
    return fig 



#Se crea espacio para la columna en blanca divisoria.
Division = ''

#Se crea espacio para la elección de la respuesta sismica del suelo titulo, menu y datos.
Suelos = html.Div([
        html.H3('Zonificación del suelo'),
        html.Hr()
    ],
    )

RespuestaSismica = dbc.Container(
    [
       html.H3('Localidad'),
       html.Hr(),
       html.Div([
           dcc.Dropdown(Localidades['LocNombre'].unique(), 'CIUDAD BOLIVAR' , id='localidad_consultada',
                        style={'background-color':'#FFCC80',"font-weight": "bold"}),
            html.Hr(),
            dcc.Graph(
                id="mapa",
                style={
                    'width': '100%', 
                    "height": "600px"
                    },
        ),
       ])
    ],
    fluid=True
)


Poblacion_RespuestaSismica = dbc.Container(
    [
        html.H3('Zonificación del suelo'),
        html.Hr(),
       html.Div([
           dcc.RadioItems(ZonaSismica['RESSIS'], id='ZonaSismica_consultada',
                        style={'background-color':'#FFCC80',"font-weight": "bold",'textAlign':'left'}),
            html.Hr(),
            html.H5('Cantidad de Habitantes'),
            html.Hr(),
            #dcc.Input(id='TotalHabitantes', type='number'),
            html.H5('Cantidad_Habitantes')
    
       ]),

    ]
)