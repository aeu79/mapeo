import folium
import branca
import os

print(folium.__version__)

# Para que quede clarinete: El explicao'

# Primero el mapa grande, así queda más clarito
mapote = folium.Map([-46.9831296, -70.7979096], zoom_start=7)

# Truncado (ahora dos). Se crean "figuras" que son los "lienzos" en los que va cualquier cosa. En realidad es un
# documento html, en el que obviamente puede ir cualquier cosa.
# En este coso van a ser los minimapas. Este branca parece ser un extra para agregar cualquier cosa a los
# mapas de folium.
# Ejemplos: https://nbviewer.jupyter.org/github/python-visualization/branca/blob/master/examples/Elements.ipynb
fig_a = branca.element.Figure()
fig_b = branca.element.Figure()
# Ahora crear un mapita dentro de las dos figuras. El mismo, pero con diferente configuración en "tiles".
folium.Map([-46.7952743,-67.9582257],tiles='Stamen Toner', zoom_start=13).add_to(fig_a)
folium.Map([-46.7952743,-67.9582257], zoom_start=13).add_to(fig_b)


# Esta parte se pone redundante. Pero ahora pone las figuras (que ya contienen los minimapas) dentro de un iframe.
# Más info sobre iframes: https://es.wikipedia.org/wiki/Iframe
# Si estás en Firefox y apretás F12, ves la información de cualquier página web. Por ejemplo, un iframe a veces
# contiene un video de youtube. Son "marcos" en los que se separan las páginas web (en realidad es un documento html
# completo, que se inserta dentro de otro). O sea que si le podés poner un
# iframe a un mapa, le podés poner cualquier cosa.

# Entonces, creamos los iframes (vacíos, con un tamaño epecífico):
iframe = branca.element.IFrame(width=600, height=300)
iframe_dos = branca.element.IFrame(width=600, height=300)

# Y se agregan las figuras con los mapitas a los iframes
fig_a.add_to(iframe)
fig_b.add_to(iframe_dos)

# Y ahora sigue siguiendo... Crear los popups con cada iframe.
popup = folium.Popup(iframe, max_width=2650)
popup_dos = folium.Popup(iframe_dos, max_width=2650)

# Ah, pero qué pesadilla. Ahora hay que asignarle esos popus a marcadores en el mapa.
# Let's put the Popup on a marker, in the second map.

folium.Marker([-46.7952743,-67.9122257], popup=popup,icon=folium.Icon(icon='home')).add_to(mapote)
folium.Marker([-46.7952743,-67.8582257], popup=popup_dos).add_to(mapote)

# los mismo iframes se podrían reciclar para varios popups. Pero no se pueden reciclar los popus (ya lo probé),
#  así que hay que crear uno para cada marker.
popup3 = folium.Popup(iframe, max_width=2650)
folium.Marker([-46.2952743,-67.1582257], popup=popup3).add_to(mapote)
popup4 = folium.Popup(iframe, max_width=2650)
# Y con otro íconos:
folium.Marker([-46.3952743,-67.5582257], popup=popup4,icon=folium.Icon(icon='camera')).add_to(mapote)
popup5 = folium.Popup(iframe, max_width=2650)
# Colores dipsonibles: {'red', 'black', 'beige', 'darkpurple', 'lightred', 'purple', 'cadetblue', 'lightgreen', 'pink', 'lightgray', 'darkblue', 'darkred', 'darkgreen', 'blue', 'orange', 'green', 'lightblue', 'white', 'gray'}
# íconos disponibles (si usar fuentes externas): https://getbootstrap.com/docs/3.3/components/#glyphicons-glyphs
folium.Marker([-46.4952743,-67.3582257], popup=popup5,icon=folium.Icon(color='green')).add_to(mapote)
popup6 = folium.Popup(iframe, max_width=2650)
folium.Marker([-46.8002,-67.9571], popup=popup6,icon=folium.Icon(color='red')).add_to(mapote)
# ahora reuso el iframe_dos
popup7 = folium.Popup(iframe_dos, max_width=2650)
folium.Marker([-46.5952743,-67.9582257], popup=popup7,icon=folium.Icon(color='pink')).add_to(mapote)
popup8 = folium.Popup(iframe_dos, max_width=2650)
folium.Marker([-46.4952743,-66.2582257], popup=popup8,icon=folium.Icon(icon='leaf', color="green")).add_to(mapote)
popup9 = folium.Popup(iframe_dos, max_width=2650)
folium.Marker([-46.4952743,-67.2582257], popup=popup9,icon=folium.Icon(icon='fire',color='red')).add_to(mapote)
popup10 = folium.Popup(iframe_dos, max_width=2650)
folium.Marker([-46.2952743,-67.1582257], popup=popup10,icon=folium.Icon(icon='tint')).add_to(mapote)

# GeoJson
# folium.GeoJson(
#     'Camp.geojson',
#     name='punto_geojson',
# ).add_to(mapote)

popup11 = folium.Popup(iframe_dos, max_width=2650)
folium.GeoJson('AreAprox.geojson',name='area_geojson',popup=popup11).add_to(mapote)

folium.LayerControl().add_to(mapote)

# Add the option to allow the user to add markers on the fly (al tiro!)
mapote.add_child(folium.ClickForMarker())

# We get a map in a Popup. Not really useful, but powerful.
mapote.save(os.path.join('./', 'pt_tres_popups.html'))
