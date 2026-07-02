import streamlit as st

def procesar_archivo(archivo):
    """Procesa el archivo subido y lo convierte en un diccionario para búsqueda rápida."""
    datos_dict = {}
    # Decodificar el archivo subido a texto
    stringio = archivo.getvalue().decode("utf-8", errors='replace')
    
    for linea in stringio.splitlines():
        if len(linea) > 15:
            f_id = linea[0:15].strip()
            datos_dict[f_id] = {
                "Nombre": linea[15:76].strip(),
                "Fed": linea[76:80].strip(),
                "Título": linea[84:89].strip() or "N/A",
                "Elo": linea[113:119].strip() or "N/A"
            }
    return datos_dict

# Configuración de la App
st.set_page_config(page_title="Buscador FIDE", page_icon="♚")
st.title("♚ Buscador de Jugadores FIDE")

# 1. Widget para subir el archivo
archivo_subido = st.file_uploader("Sube tu archivo 'standard_rating_list.txt'", type=['txt'])

if archivo_subido is not None:
    # Procesar el archivo subido
    data = procesar_archivo(archivo_subido)
    st.success("Archivo cargado correctamente.")
    
    # 2. Input de búsqueda
    input_usuario = st.text_input("IDs a buscar (separados por comas):")

    if st.button("Buscar"):
        if input_usuario:
            lista_ids = [i.strip() for i in input_usuario.split(',')]
            resultados = []
            
            for f_id in lista_ids:
                if f_id in data:
                    res = data[f_id]
                    resultados.append({"ID": f_id, **res})
                else:
                    resultados.append({"ID": f_id, "Nombre": "No encontrado", "Fed": "-", "Título": "-", "Elo": "-"})
            
            st.table(resultados)
        else:
            st.warning("Por favor, introduce al menos un ID.")
else:
    st.info("Por favor, sube el archivo de texto (.txt) para comenzar la búsqueda.")
