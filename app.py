print(">>> Cargando app.py v3")

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, html, dcc
import numpy as np
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
import seaborn as sns

# === Carga de datos (ajusta la ruta y el formato) ===
#lectores = pd.read_csv("/Users/arturo/Desktop/Datos/lectores.csv")

#Esto está cargando los lectores (porque el notebook ya lo ha preparado)
lectores = pd.read_csv("lectores_preparado.csv")

#GRAFICO 1: #GRÁFICO DE LECTORES GENERAL
nombre="fig_"
#lectores=pd.read_csv("/Users/arturo/Pruebas/repoArturo/EDA/data/Datos_noviembre_2024_lectura.csv")
lectores = pd.read_csv("data/Datos_noviembre_2024_lectura.csv")


lectores[["p5"]].count()
libros_leidos=lectores.groupby("p5")[["id"]].count()
libros_leidos.index.name="respuesta"
df=libros_leidos.reset_index()
df.columns=["respuesta","lectores"]

#grafico
colores_flat9_a = [
    "#2ecc71",  # Verde esmeralda
    "#e67e22",  # Naranja intenso
    "#34495e",  # Azul gris oscuro
    "#16a085"   # Verde azulado oscuro
    "#1abc9c",  # Turquesa
    "#3498db",  # Azul claro
    "#f39c12",  # Naranja dorado
    "#e74c3c",  # Rojo
    "#9b59b6",  # Violeta
]

verde_naranja = {
    "#2ecc71",  # Verde esmeralda
    "#55d66b",  # Verde lima
    "#86d96a",  # Verde amarillento
    "#b5db5f",  # Amarillo verdoso
    "#e3d256",  # Amarillo mostaza
    "#f5b143",  # Amarillo anaranjado
    "#f89533",  # Naranja medio
    "#e67e22"   # Naranja intenso
}

colores_2 = {
   "Entre 16 y 20": "#e67e22",
   "Más de 20": "#f89533",
   "Entre 11 y 15": "#f5b143",
   "Entre 7 y 10": "#e3d256",
   "Ninguno": "#b5db5f",
   "Uno": "#86d96a",
   "Entre 4 y 6": "#55d66b",
    "Entre 2 y 3":"#2ecc71"   # Azul petróleo
}

azules_flat_b = [
    "#EBF5FB",  # Azul hielo
    "#D6EAF8",
    "#AED6F1",
    "#85C1E9",
    "#5DADE2",
    "#3498DB",
    "#2E86C1",
    "#2874A6",
    "#21618C"   # Azul petróleo
]

azules_flat_c = {
   "Entre 16 y 20": "#D6EAF8",
   "Más de 20": "#AED6F1",
   "Entre 11 y 15": "#85C1E9",
   "Entre 7 y 10": "#5DADE2",
   "Ninguno": "#3498DB",
   "Uno": "#2E86C1",
   "Entre 4 y 6": "#2874A6",
    "Entre 2 y 3":"#21618C"   # Azul petróleo
}

rojos_flat = [
    "#FDEDEC",  # Rosa pastel
    "#FADBD8",  # Rosa salmón
    "#F5B7B1",  # Rojo suave
    "#EC7063",  # Rojo medio
    "#E74C3C",  # Rojo clásico (Flat UI)
    "#CB4335",  # Rojo fuerte
    "#B03A2E",  # Rojo oscuro
    "#943126",  # Rojo vino
    "#78281F"   # Rojo borgoña
]


colores= colores_flat9_a

fig_pie1 = go.Figure(
    go.Pie(
        labels=df.respuesta,
        values=df.lectores,
        textinfo="label+percent",
        hole=0.3,
        #marker=dict(colors=[colores[val] for val in df["respuesta"]])
        marker=dict(colors=colores)
    )
)
fig_pie1.update_layout(
    title="<b>Hipótesis 1: Se lee poco.</b><br><span style='font-size:14px;color:gray;'>¿Cuántos libros has leído en los últimos 12 meses?</span>",
    title_x=0,
        annotations=[
        dict(
            text="14,3%",          # el número grande
            x=-0.1, y=1,          # posición (centro del gráfico)
            showarrow=False,
            font=dict(size=80, color="gray", family="Arial")
        )
        ],
    template="plotly_white"
)
#fig_pie1.show()

#GRÁFICO 2
#GRÁFICO DE LECTORES AGRUPADO. <= 3 LIBROS
a_agrupar=["Ninguno","Uno","Entre 2 y 3"]

file_resumen=pd.DataFrame([{
    "respuesta":"3 o menos",
    "lectores": df.loc[df["respuesta"].isin(a_agrupar),"lectores"].sum()
}])
df_filtrado = df[~df["respuesta"].isin(a_agrupar)]
df_final = pd.concat([df_filtrado, file_resumen], ignore_index=True)
df_final = df_final.sort_values("lectores", ascending=False).reset_index(drop=True)
#grafico

colores_graf_2 = [
    "#34495e",  # Azul gris oscuro
    "#e74c3c",  # Rojo
    "#e89c59",  # Naranja suave
    "#16a085"   # Verde azulado oscuro
    "#1abc9c",  # Turquesa
    "#3498db",  # Azul claro
    "#2ecc71",  # Verde esmeralda
    "#9b59b6",  # Violeta    
]

fig_pie2 = go.Figure(
    go.Pie(
        labels=df_final["respuesta"],
        values=df_final["lectores"],
        textinfo="label+percent",
        hole=0.3,
        marker=dict(colors=colores_graf_2)
    )
)
fig_pie2.update_layout(
    title="<b>Distribución agrupada</b><br><span style='font-size:14px;color:gray;'>¿Cuántos libros has leído en los últimos 12 meses?</span>",
    title_x=0,
        annotations=[
        dict(
            text="56,6%",          # el número grande
            x=-0.099, y=1,          # posición (centro del gráfico)
            showarrow=False,
            font=dict(size=80, color="gray", family="Arial")
        )
        ],
    template="plotly_white"
    
    
)
#fig_pie2.show()

#GRÁFICO 3
#¿Con qué frecuencia haces la siguiente actividad en tu tiempo libre? p4_1: Leer un libro
nombre="fig_generaciones"

#lectores = lectores[["gen_r", "sexo","p4_1"]]
lectores_T=lectores.groupby("p4_1")["p4_1"].count().sort_values(ascending=False)
lectores_T_pct = (lectores_T / lectores_T.sum()*100).round(2)
lectores_GZ=lectores[lectores["gen_r"]=="Generacion Z"].groupby("p4_1")["p4_1"].count().sort_values(ascending=False)
lectores_GZ_pct = (lectores_GZ / lectores_GZ.sum()*100).round(2)
lectores_MIL=lectores[lectores["gen_r"]=="Millennials"].groupby("p4_1")["p4_1"].count().sort_values(ascending=False)
lectores_MIL_pct = (lectores_MIL / lectores_MIL.sum()*100).round(2)
lectores_GX=lectores[lectores["gen_r"]=="Generacion X"].groupby("p4_1")["p4_1"].count().sort_values(ascending=False)
lectores_GX_pct = ((lectores_GX / lectores_GX.sum())*100).round(2)
lectores_BB=lectores[lectores["gen_r"]=="Baby Boomers - Silent Generation"].groupby("p4_1")["p4_1"].count().sort_values(ascending=False)
lectores_BB_pct = (lectores_BB / lectores_BB.sum()*100).round(2)

trace1={
    "x":lectores_GZ_pct.index,
    "y":lectores_GZ_pct.values,
    "name":"GZ",
    "type":"bar",
    "text": [f"" for v in lectores_GZ.values],
    "textposition":"outside",
    "marker":dict(color="teal"),
}
trace2={
    "x":lectores_MIL_pct.index,
    "y":lectores_MIL_pct.values,
    "name":"Millennials",
    "type":"bar"
    }
trace3={
    "x":lectores_GX_pct.index,
    "y":lectores_GX_pct.values,
    "name":"GX",
    "type":"bar"
}
trace4={
    "x":lectores_BB_pct.index,
    "y":lectores_BB_pct.values,
    "name":"Boomers",
    "type":"bar"
}
data=[trace1, trace2, trace3, trace4]
layout={
    "title": "LECTORES",    
    "xaxis":{"title":""},
    "yaxis": {"title": "Porcentaje %"},
}

fig_generaciones = go.Figure(data=data, layout=layout)
fig_generaciones.update_layout(
    title="<b>Hipótesis 2: Los jóvenes no leen. </b><br><span style='font-size:14px;color:gray;'>¿Con qué frecuencia sueles leer un libro en tu tiempo libre?</span></br>",
    title_x=0,
    template="plotly_white"
    
)
fig_generaciones.update_xaxes(tickangle=30)
#iplot(fig_generaciones)

#GRAFICO 4
nombre="fig_generaciones_agrupadas"
lectores_T.index.name = "respuesta"
df = lectores_T.reset_index()
df.columns = ["respuesta", "lectores"]
a_agrupar = ["Una o dos veces por semana","Tres o cuatro veces por semana","Todos o casi todos los días"]
fila_resumen = pd.DataFrame([{
    "respuesta": "Al menos dos veces por semana",
    "lectores": df.loc[df["respuesta"].isin(a_agrupar), "lectores"].sum()
}])
df_filtrado = df[~df["respuesta"].isin(a_agrupar)]
df_final = pd.concat([df_filtrado, fila_resumen], ignore_index=True)
df_final = df_final.sort_values("lectores", ascending=False).reset_index(drop=True)
#Lectores_GZ.
df_gz = lectores_GZ.rename_axis("respuesta").reset_index(name="lectores")
#a_agrupar = ["Una o dos veces por semana","Tres o cuatro veces por semana","Todos o casi todos los días"]
fila_resumen = pd.DataFrame([{
    "respuesta": "Al menos dos veces por semana",
    "lectores": df_gz.loc[df["respuesta"].isin(a_agrupar), "lectores"].sum()
}])
df_filtrado_gz = df_gz[~df_gz["respuesta"].isin(a_agrupar)]
df_final_gz = pd.concat([df_filtrado_gz, fila_resumen], ignore_index=True)
df_final_gz = df_final_gz.sort_values("lectores", ascending=False).reset_index(drop=True)
lectores_GZ_a_pct = (df_final_gz["lectores"] / df_final_gz["lectores"].sum() * 100).round(2)
df_final_gz["porcentaje"]=lectores_GZ_a_pct
#Lectores_ Millennials.
df_mil = lectores_MIL.rename_axis("respuesta").reset_index(name="lectores")
#a_agrupar = ["Una o dos veces por semana","Tres o cuatro veces por semana","Todos o casi todos los días"]
fila_resumen = pd.DataFrame([{
    "respuesta": "Al menos dos veces por semana",
    "lectores": df_mil.loc[df_mil["respuesta"].isin(a_agrupar), "lectores"].sum()
}])
df_filtrado_mil = df_mil[~df_mil["respuesta"].isin(a_agrupar)]
df_final_mil = pd.concat([df_filtrado_mil, fila_resumen], ignore_index=True)
df_final_mil = df_final_mil.sort_values("lectores", ascending=False).reset_index(drop=True)
lectores_mil_a_pct = (df_final_mil["lectores"] / df_final_mil["lectores"].sum() * 100).round(2)
df_final_mil["porcentaje"]=lectores_mil_a_pct
#Lectores_ X.
df_gx = lectores_GX.rename_axis("respuesta").reset_index(name="lectores")
#a_agrupar = ["Una o dos veces por semana","Tres o cuatro veces por semana","Todos o casi todos los días"]
fila_resumen = pd.DataFrame([{
    "respuesta": "Al menos dos veces por semana",
    "lectores": df_gx.loc[df_gx["respuesta"].isin(a_agrupar), "lectores"].sum()
}])
df_filtrado_gx = df_gx[~df_gx["respuesta"].isin(a_agrupar)]
df_final_gx = pd.concat([df_filtrado_gx, fila_resumen], ignore_index=True)
df_final_gx = df_final_gx.sort_values("lectores", ascending=False).reset_index(drop=True)
lectores_gx_a_pct = (df_final_gx["lectores"] / df_final_gx["lectores"].sum() * 100).round(2)
df_final_gx["porcentaje"]=lectores_gx_a_pct
#Lectores_ X.
df_bb = lectores_BB.rename_axis("respuesta").reset_index(name="lectores")
#a_agrupar = ["Una o dos veces por semana","Tres o cuatro veces por semana","Todos o casi todos los días"]
fila_resumen = pd.DataFrame([{
    "respuesta": "Al menos dos veces por semana",
    "lectores": df_bb.loc[df_bb["respuesta"].isin(a_agrupar), "lectores"].sum()
}])
df_filtrado_bb = df_bb[~df_bb["respuesta"].isin(a_agrupar)]
df_final_bb = pd.concat([df_filtrado_bb, fila_resumen], ignore_index=True)
df_final_bb = df_final_bb.sort_values("lectores", ascending=False).reset_index(drop=True)
lectores_bb_a_pct = (df_final_bb["lectores"] / df_final_bb["lectores"].sum() * 100).round(2)
df_final_bb["porcentaje"]=lectores_bb_a_pct
#grafico
trace1={
    "x": df_final_gz["respuesta"],
    "y": df_final_gz["porcentaje"],
    "name":"GZ",
    "type":"bar",
    #"text": [f"" for v in df_final_gz.values],
    #"text": [f"GZ" for v in lectores_gx_a_pct.values],  
    "text": "GZ",       
    "textposition":"outside",
    "marker":dict(color="teal")
}
trace2={
    "x": df_final_mil["respuesta"],
    "y": df_final_mil["porcentaje"],
    "name":"Millennials",
    "type":"bar",
    "text": "Mil",
    "textposition":"outside"
    }
trace3={
    "x": df_final_gx["respuesta"],
    "y": df_final_gx["porcentaje"],
    "name":"GX",
    "type":"bar",
    "text": "GX",       
    "textposition":"outside"
}
trace4={
    "x": df_final_bb["respuesta"],
    "y": df_final_bb["porcentaje"],
    "name":"Boomers",
    "type":"bar",
    "text": "GX",       
    "textposition":"outside"
}
data=[trace1, trace2, trace3, trace4]
layout={
    "xaxis":{"title":""},
    "title": "LECTORES AGRUPADOS",
    "yaxis": {"title": "Porcentaje %"},
}
fig_generaciones_agrupadas=go.Figure(data=data, layout=layout)
fig_generaciones_agrupadas.update_xaxes(tickangle=30)
#iplot(fig_generaciones_agrupadas)


#GRÁFICO 5
nombre="fig_motivos"

# --- Datos (mismo cálculo que uso en el bucle)
# 1) Construimos una tabla con los datos del bucle
cols = [f"p7b_{i}" for i in range(1, 10)]
resumen = []

for col in cols:
    conteos = lectores[col].value_counts()
    total = conteos.sum()
    selected = conteos.get("Selected", 0)
    porcentaje = (selected / total) * 100 if total > 0 else 0
    resumen.append({"pregunta": col, "Selected": selected, "Total": total, "% Selected": porcentaje})

df_pct = pd.DataFrame(resumen).sort_values("% Selected", ascending=True)  # orden para ranking horizontal

# Nombres personalizados para las etiquetas del eje Y
map_y = {
    "p7b_1":"Dispongo de menos tiempo libre para ocio", "p7b_2":"Me resulta más difícil encontrar libros que me gusten", "p7b_3":"Paso más tiempo jugando juegos con el móvil",
    "p7b_4":"Paso más tiempo jugando videojuegos (en el ordenador, con consolas, etc)",  "p7b_5":"Dedico más tiempo a las redes sociales (Instagram, YouTube, TikTok, etc.)","p7b_6":"Veo más series y películas",
    "p7b_7":"Ha empeorado mi salud (visión, etc.)","p7b_8":"Por mi momento vital, ahora disfruto menos de la lectura", "p7b_9":"Otros motivos"
}

# df_pct ya está ORDENADO por % Selected
df_pct["etiqueta_y"] = df_pct["pregunta"].map(map_y).fillna(df_pct["pregunta"])

# 2) Gráfico con trace (go.Bar)
trace = go.Bar(
    x=df_pct["% Selected"].values,           # porcentaje en X
    y=df_pct["etiqueta_y"].values,   # ← usa la etiqueta mapeada TRAS ordenar
    orientation="h",
    text=[f"{v:.1f}%" for v in df_pct["% Selected"].values],
    textposition="outside",
    marker=dict(color="teal"),
    name="% Selected"
)

layout = go.Layout(
    title="<b>Hipótesis 3: Los móviles son los culpables. </b><br><span style='font-size:14px;color:gray;'>¿Por qué lees menos que hace 10 años?</span></br>",
    xaxis=dict(title="% sobre total", range=[0, 60]),  # ejes en 0–80%
    yaxis=dict(title="Motivos"),
    template="plotly_white",
    height=500
)
#cambiar los nombre de las etiquetas
fig_motivos = go.Figure(data=[trace], layout=layout)


#fig_motivos.show()

# === APP DASH ===
app = Dash(__name__)
app.title = "ENCUESTA A LECTORES"

app.layout = html.Div(
    [
        # CABECERA
        html.Div(
            [
                html.H2("Encuesta a lectores - Resultados"),
                html.P(
                    "2000 entrevistas realizadas en España en noviembre de 2024",
                    style={"margin": "6px 0 0 0", "color": "#555"},
                ),
            ],
            style={
                "padding": "18px 24px",
                "backgroundColor": "#f7f7f7",
                "borderBottom": "1px solid #eee",
            },
        ),

# --- CUERPO ---
        html.Div(
            [
                #GRAFICO 1
                html.Div(
                    [
                        dcc.Graph(
                            id="grafico-pie1",
                            figure=fig_pie1,
                            config={"displayModeBar": True, "responsive": True},
                            style={"height": "560px"},
                        )
                    ],
                    style={"width": "100%", "padding": "20px 10px"},
                ),
                
                html.Div(style={"height": "150px", "backgroundColor": "#f7f7f7"}),  # Espaciador vertical
                
                #GRAFICO 2
                html.Div(
                    [
                        dcc.Graph(
                            id="grafico-pie12",
                            figure=fig_pie2,
                            config={"displayModeBar": True, "responsive": True},
                            style={"height": "560px"},
                        ),              
                        dcc.Markdown(
                            """
                            **Intepretación:**
                            Efectivamente, se lee poco.
                            """,
                            style={
                                "lineHeight": "1.7",
                                "color": "#333",
                                "padding": "10px 20px",
                                "texAlign": "left",
                            },
                        ),
                    ],
                    style={"width": "100%", "padding": "20px 10px"},
                ),
            
                html.Div(style={"height": "150px", "backgroundColor": "#f7f7f7"}),  # Espaciador vertical

                # GRÁFICO 3
                html.Div(
                    [
                        dcc.Graph(
                            id="grafico-2",
                            figure=fig_generaciones,
                            config={"displayModeBar": True, "responsive": True},
                            style={"height": "560px"},
                        )
                    ],
                    style={"width": "100%", "padding": "20px 10px"},
                ),

                html.Div(style={"height": "150px"}),  # Espaciador vertical
                
                #GRÁFICO 4
                html.Div(
                    [
                        dcc.Graph(
                            id="grafico-2",
                            figure=fig_generaciones_agrupadas,
                            config={"displayModeBar": True, "responsive": True},
                            style={"height": "560px"},
                        )
                    ],
                    style={"width": "100%", "padding": "20px 10px"},
                ),

                html.Div(
                    [
                        dcc.Markdown(
                            """
                            **Interpretación**
                            El 52,8% de los jóvenes (G.Z) contesta que al menos 2 veces por semana dedican parte de su tiempo libre a la lectura. Supone el menor porcentaje de respuesta respecto al resto de grupos: Millennial, X o Baby Boomers. Pero solo 2 puntos por debajo de la media (55,84%).
                            No podemos afirmar que la generación Z sea la responsable de que se lea poco.
                            Conclusión: la edad no es factor determinante.
                            """,
                            style={
                                "lineHeight": "1.7",
                                "color": "#333",
                                "padding": "10px 20px",
                            },
                        ),
                    ],
                ),
                html.Div(style={"height": "150px", "backgroundColor": "#f7f7f7"}),  # Espaciador vertical

                #GRÁFICO 5
                html.Div(
                    [      
                        dcc.Graph(
                            id="grafico-p7b",
                            figure=fig_motivos,
                            config={"displayModeBar": True, "responsive": True},
                            style={"height": "560px"},
                        ),
                    ],
                    style={"width": "100%", "padding": "20px 10px"},
                ),

                html.Div(style={"height": "10px", "backgroundColor": "#f7f7f7"}),  # Espaciador vertical

                # Texto intermedio
                html.Div(
                    [
                        dcc.Markdown(
                            """
                            **Interpretación del gráfico**
                            EL 47,2% (casi la mitad) de los encuestados confiesa que el motivo por el que leen menos ahora que hace 10 años es porque consumen más series y películas.
                            Las plataformas con su oferta de cine son el mayor (gran) ladrón de lectores, seguido de lejos (un 35,8%) por la falta de tiempo libre y, en tercer lugar, por el móvil; entendido como herramienta para el consumo de tiempo dedicado a las RRSS: Instagram, YouTube, TikTok (que aparece en el 31,8% de las respuestas).
                            """,
                            style={
                                "lineHeight": "1.7",
                                "color": "#333",
                                "padding": "10px 20px",
                            },
                        ),
                    ],
                ),
                html.Div(style={"height": "150px", "backgroundColor": "#f7f7f7"}),  # Espaciador vertical
                
                # CONCLUSIONES Y RECOMENDACIONES
                
                html.Div([
                    html.H2("Conclusión: “El lector se ha ido al cine”… o mejor dicho, a Netflix.",
                            style={
                            "color": "#4c5054",     # ← color en formato HEX (puede ser 'red', 'blue', etc.)
                            "textAlign": "center",  # ← centrado opcional
                            "fontWeight": "600",    # ← grosor de la letra
                            "fontSize": "26px"      # ← tamaño
                        }
                            
                            ),
                    
                    html.Img(
                            src="/assets/image.avif",          # Ruta relativa a la carpeta assets
                            style={"width": "600px", "margin": "40px auto", "display": "block"}
                        ),
                ]),
                
                                html.Div(style={"height": "150px"}),  # Espaciador vertical
                html.Div([
                    html.H2(
                        "¿Qué podemos hacer para fomentar la lectura / venta de libros?",
                        style={
                            "color": "#1a4f84",     # ← color en formato HEX (puede ser 'red', 'blue', etc.)
                            "textAlign": "center",  # ← centrado opcional
                            "fontWeight": "600",    # ← grosor de la letra
                            "fontSize": "26px"      # ← tamaño
                        }
                    )
                ]),               
                html.Div(style={"height": "50px"}),  # Espaciador vertical
                
                html.Div([
                    html.H2("Libros basados en series y películas"),
                    html.Img(
                    src="/assets/series5.png",          # Ruta relativa a la carpeta assets
                    style={"width": "900px", "margin": "20px auto", "display": "block"}
                    ),
                ]),
                html.Div(style={"height": "150px", "backgroundColor": "#f7f7f7"}),  # Espaciador vertical

            ],
            style={
                "display": "block",
                "textAlign": "center",
            },
        ),

        # --- PIE DE PÁGINA ---
        html.Div(
            [
                html.P(
                    "Fuente: Radiografía de la lectura en el siglo XXI - noviembre 2024 - 40db - España (https://ladespensa.40db.es/)",
                    style={
                        "margin": 0,
                        "color": "#666",
                        "fontStyle": "italic",
                        "fontSize": "14px",
                    },
                )
            ],
            style={
                "padding": "12px 24px",
                "borderTop": "1px solid #eee",
                "textAlign": "right",
            },
        ),
    ],
    style={
        "fontFamily": "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
        "backgroundColor": "#fff",
    },
)
# === Ejecutar la app ===
if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=8050,          # <— fuerza este puerto
        use_reloader=True,        # evita dos procesos
        dev_tools_hot_reload=False # evita autorecarga que re-ejecuta todo
    )