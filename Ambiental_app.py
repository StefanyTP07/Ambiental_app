importar  streamlit  como  st
importar  pandas  como  pd
importar  numpy  como  np

n  =  st . control deslizante ( "n" , 5 , 100 , paso = 1 )
chart_data  =  pd . DataFrame ( np . aleatorio . randn ( n ), columnas = [ 'datos' ])
st . line_chart ( chart_data )
