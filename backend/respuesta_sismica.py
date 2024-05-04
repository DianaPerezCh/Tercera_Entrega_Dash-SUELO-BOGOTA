# Se importan Las librerias

import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from PIL import Image
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

#token = open(".mapbox_token").read()

# Se crean las variables para ser insertadas en el Container de respuesta sísmica

Tituto1 = html.H3('Zonas de Respuesta Sismica')



Localidades = gpd.read_file('data\Localidades')
#Localidades = Localidades.to_crs("WGS84")
#Localidades_index=Localidades.set_index("RESSIS")
ZonaSismica = gpd.read_file('data\Respuesta Sísmica')
#ZonaSismica = ZonaSismica.to_crs("WGS84")
DensidadPoblacional=gpd.read_file('data\Centroides_Manzanas.geojson')

def consultarLocalidad(localidad_consultada):

    localidad_buscada = Localidades.query(f"LocNombre == '{localidad_consultada}'")
    

    #ZonaSismica_RESSIS=ZonaSismica.set_index("RESSIS")

    #localidad_buscada_4326 = localidad_buscada.to_crs(epsg=4326)

    ZonaSismica_4686 = ZonaSismica.to_crs(epsg=4686)
    #ZonaSismica_buscada = ZonaSismica_4686.query(f"LocNombre == '{localidad_consultada.upper()}'")




    ZonaSismica_Localidad = gpd.overlay(
    localidad_buscada, ZonaSismica_4686, how='intersection')
    ZonaSismica_Localidad=ZonaSismica_Localidad.set_index("RESSIS")


    
   # ZonaSismica_Localidad['randNumCol']= np.random.randint(0, 10, ZonaSismica_Localidad.shape[0]).astype('str')

       
    # Genera mapa de localidades

    fig = px.choropleth_mapbox(
        geojson=ZonaSismica_Localidad.geometry,
        locations=ZonaSismica_Localidad.index,
        #legend=True,
        #legend_kwds={"loc":"upper left"}
    )

    




        #data_frame = ZonaSismica_Localidad.set_index("RESSIS"), # Usar el ID como índice de los datos
        #geojson = ZonaSismica_Localidad.geometry,                # La geometría
        #locations = ZonaSismica_Localidad.index,                 # El índice de los datos
        #color = 'unemp_rate',
        #mapbox_style = 'open-street-map',
        #center = dict(lat = 4.33, lon = -74.08),
        #zoom = 4)

    
        #geojson=ZonaSismica_Localidad.geometry,
        #locations=ZonaSismica_Localidad.index,

        #data_frame = ZonaSismica_Localidad.set_index("RESSIS")
    

    #fig.add_trace(
     #   go.Scattermapbox(
      #      lat=localidad_buscada_4326.y,
       #     lon=localidad_buscada_4326.x,
        #    mode='markers',
         #   marker=go.scattermapbox.Marker(
          #      size=9,
           #     color='red'
            #),
            #text=localidad_buscada_4326['LocNombre'],
            #hoverinfo='text'
   #     )

    #)

    fig.update_layout(
        #ZonaSismica_Localidad=ZonaSismica_Localidad.set_index("RESSIS"),
        #color = 'unemp_rate',
        mapbox_style="open-street-map",
        #showlegend=False,
        #margin={"r":0,"t":0,"l":0,"b":0},
        #color="randNumCol",
        mapbox_zoom=8,
        mapbox_center = {"lat": 4.33, "lon": -74.08},
    
    )

    #ZonaSismica_Localidad_grafica=px.ZonaSismica_Localidad.election()
    #geojson = px.ZonaSismica_Localidad.election_geojson()

    #fig = px.choropleth_mapbox(ZonaSismica_Localidad_grafica, geojson=geojson, color="Bergeron",
     #                       locations="district", featureidkey="properties.district",
      #                      center={"lat": 45.5517, "lon": -73.7073},
       #                     mapbox_style="carto-positron", zoom=9)
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    #def consultarZonaSismica(ZonaSismica_consultada):
     #   ZonaSismica_consultada = ZonaSismica_Localidad.query(f"RESSIS == '{ZonaSismica_consultada}'")
      #  DensidadPoblacional_4326=DensidadPoblacional.to_crs(epsg=4326)

       # ZonaSismica_Poblacion= gpd.overlay(
        #    DensidadPoblacional_4326, ZonaSismica_consultada, how='intersection')
        
       # Total_habitantes=  ZonaSismica_Poblacion["PER_S010"].sum()

        #return 'El total de habitantes de la localidad de' + str(localidad_buscada) +'ubicados en una zonificación del suelo de respuesta sismica' + str(ZonaSismica_consultada) + 'es de' + str(Total_habitantes)
   
    return fig



#Se crea espacio para la columna en blanca divisoria.
Division = ''




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
                    "height": "600px",'background-color':'#FFCC80'
                    },
        )
       ])
    ],
    fluid=True
)

ConsultaZonaSismica_Localidad=consultarLocalidad


def consultarZonaSismica(ZonaSismica_consultada):
    ZonaSismica_buscada = ConsultaZonaSismica_Localidad.query(f"RESSIS == '{ZonaSismica_consultada}'")
    DensidadPoblacional_4686 = ZonaSismica.to_crs(epsg=4686)
    ZonaSismica_Densidad = gpd.overlay(
    ZonaSismica_buscada, DensidadPoblacional_4686, how='intersection')
    Total_Habitantes=ZonaSismica_Densidad["PER_S010"].sum()



    return 'El total de habitantes de la localidad de' +Total_Habitantes



Poblacion_RespuestaSismica = dbc.Container(
    [
        html.H3('Zonificación del suelo'),
        html.Hr(),
       html.Div([
           dcc.RadioItems(ZonaSismica['RESSIS'].unique(), id='ZonaSismica_consultada',
                        style={'background-color':'#FFCC80',"font-weight": "bold",'textAlign':'left'}),
            html.Hr(),
            html.H3('Cantidad de Habitantes'),
            html.Hr(),
            html.H5(id ='PoblacionTotal')
    
       ]),

    ]
)