import streamlit as st

def buscar_en_archivo(ids_input):
    archivo_path = "standard_rating_list.txt"
    lista_ids = [i.strip() for i in ids_input.split(',')]
    resultados = []
    
    try:
        with open(archivo_path, 'r', encoding='utf-8', errors='replace') as f:
            lineas = f.readlines()
            
        for f_id in lista_ids:
            encontrado = False
            for linea in lineas:
                if linea.startswith(f_id.ljust(15)):
                    nombre = linea[15:76].strip()
                    fed = linea[76:80].strip()
                    titulo = linea[84:89].strip()
                    elo = linea[113:119].strip()
                    
                    resultados.append({
                        "ID": f_id, "Nombre": nombre, "Fed": fed, 
                        "Título": titulo if titulo.strip() else "N/A", 
                        "Elo": elo if elo.strip() else "N/A"
                    })
                    encontrado = True
                    break
            if not encontrado:
                resultados.append({"ID": f_id, "Nombre": "No encontrado", "Fed": "-", "Título": "-", "Elo": "-"})
    except FileNotFoundError:
        st.error("Error: El archivo 'standard_rating_list.txt' no se encuentra en la carpeta.")
        
    return resultados

# Configuración de la App
st.set_page_config(page_title="Buscador FIDE", page_icon="♚")
st.title("♚ Buscador de Jugadores FIDE")
st.write("Introduce los IDs separados por comas para obtener sus datos.")

input_usuario = st.text_input("IDs (ej: 537001345, 10245154):")

if st.button("Buscar"):
    if input_usuario:
        datos = buscar_en_archivo(input_usuario)
        st.table(datos)
    else:
        st.warning("Por favor, introduce al menos un ID.")
