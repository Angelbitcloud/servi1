import pandas as pd

#ejemplo datos=pd.read_excel('libroe.xlsx')
datos=pd.read_excel('aqui va el nomnbre del archivo xlsx')
#seleccionar las columbas que deseo agrupar 
columnas = ['candidato','partido','nombre_puesto','municipio','departamento']
#crear variable para almacenar las columbas
df_seleccionados = datos[columnas]
#ordena segun el candidato
salida=df_seleccionados.sort_values('candidato')
#genera el excel con la agrupacion
nuevo=salida.to_excel('df_excel.xlsx')  
