import streamlit as st
from datetime import datetime
from supabase import create_client, Client

# CONEXIÓN A TU BASE PERMANENTE DE SUPABASE
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# FUNCIÓN PARA CARGAR LO ÚLTIMO GUARDADO
def cargar_stock():
    try:
        res = supabase.table("stock_actual").select("*").execute()
        return {fila["producto"]: fila["cantidad"] for fila in res.data}
    except Exception as e:
        st.error(f"Error al cargar: {e}")
        return {}

# FUNCIÓN PARA GUARDAR CAMBIOS AUTOMÁTICOS
def guardar_cambio(nombre, cantidad):
    supabase.table("stock_actual").upsert({
        "producto": nombre,
        "cantidad": cantidad
    }).execute()

# CARGA INICIAL AL ABRIR LA PÁGINA
datos_base = cargar_stock()
st.success("✅ CONECTADO — TUS DATOS SE GUARDAN PARA SIEMPRE!")

# Configuración general
st.set_page_config(page_title="Stock Organizado por Fecha", layout="wide")
st.title("📦 STOCK Y PEDIDOS - GUARDADO POR MES Y DÍA")
st.caption("Cada día se guarda en su carpeta del mes, puedes consultar el historial cuando quieras")
st.markdown("---")


# Seleccionar día
dia = st.selectbox(
    "Elige el día de la semana",
    ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO"]
)
st.subheader(f"Día seleccionado: {dia}")
st.info(f"📂 Se guardará en: {CARPETA_RAIZ}/{nombre_mes}/{fecha_archivo}.json")
st.markdown("---")

# Colores
VERDE = ":green["
ROJO = ":red["
FIN = "]"


# Lista completa de productos igual que antes
productos_por_dia = {
    "LUNES": [
        ("Ají Catalán Dulce x kilo", 4), ("Ají Catalán Picante x kilo", 0), ("Anana Imp x unidad", 2),
        ("Banana Brasil x kilo", 0), ("Banana Ecuador x kilo", 6), ("Berenjena x kilo", 26),
        ("Boniato criollo mediano x kilo", 0), ("Boniato Criollo x kilo", 14), ("Boniato zanahoria mediano x kilo", 0),
        ("Boniato zanahoria x kilo", 8), ("Cebolla Especial x kilo", 18), ("Cebolla roja x kilo", 0), ("Cebolla segunda x kilo", 2),
        ("Chaucha comun x kilo", 0), ("Frutilla x kilo", 0), ("Jengibre Imp x kilo", 22),
        ("Kiwi Importado x kilo", 10), ("Lima importada x kilo", 0), ("Limón nacional x kilo", 36),
        ("Limón x kilo Goddard", 2), ("Mandarina Afurer x kilo", 0), ("Mandarina Clementina x kilo", 60),
        ("Mandarina Criolla x kilo", 10), ("Mango importado x unidad (3u)", 2), ("Manzana Crispin x kilo", 0),
        ("Manzana Granny Smith x kilo", 4), ("Manzana Red 2ª x kilo", 0), ("Manzana Red x kilo", 20),
        ("Morron Amarillo x kilo", 6), ("Morron Rojo 2ª x Kilo", 0), ("Morron Rojo x Kilo", 38),
        ("Morron Verde x kilo", 36), ("Naranja esp x kilo", 42), ("Naranja Navel 2da x kilo", 0),
        ("Papa Blanca Especial x kilo", 6), ("Papa Rosada Esp premium x kilo", 10), ("Papaya importada x kilo (3u)", 0),
        ("Pepino x kilo", 22), ("Pera Francesa x kilo", 22), ("Pera x kilo Goddard", 0),
        ("Platano importado x kilo", 0), ("Pomelo rosado x kilo", 0), ("Sandia americana x kilo", 44),
        ("Tomate americano Redondo x kilo", 0), ("Tomate Cherry Redondo x kilo", 4), ("Tomate Esp Sur larga vida x kilo", 26),
        ("Tomate perita x kilo", 0), ("Tomate x kilo Goddard", 14), ("Zanahoria x kilo", 38), ("Zapallito x kilo", 8)
    ],
    "MARTES": [
        ("Ají Catalán Dulce x kilo", 0), ("Ají Catalán Picante x kilo", 6), ("Anana Imp x unidad", 4),
        ("Banana Brasil x kilo", 0), ("Banana Ecuador x kilo", 30), ("Berenjena x kilo", 24),
        ("Boniato criollo mediano x kilo", 0), ("Boniato Criollo x kilo", 36), ("Boniato zanahoria mediano x kilo", 0),
        ("Boniato zanahoria x kilo", 34), ("Cebolla Especial x kilo", 30), ("Cebolla roja x kilo", 4), ("Cebolla segunda x kilo", 0),
        ("Chaucha comun x kilo", 6), ("Frutilla x kilo", 0), ("Jengibre Imp x kilo", 12),
        ("Kiwi Importado x kilo", 6), ("Lima importada x kilo", 0), ("Limón nacional x kilo", 14),
        ("Limón x kilo Goddard", 0), ("Mandarina Afurer x kilo", 0), ("Mandarina Clementina x kilo", 46),
        ("Mandarina Criolla x kilo", 30), ("Mango importado x unidad (3u)", 4), ("Manzana Crispin x kilo", 10),
        ("Manzana Granny Smith x kilo", 4), ("Manzana Red 2ª x kilo", 0), ("Manzana Red x kilo", 20),
        ("Morron Amarillo x kilo", 0), ("Morron Rojo 2ª x Kilo", 0), ("Morron Rojo x Kilo", 46),
        ("Morron Verde x kilo", 34), ("Naranja esp x kilo", 30), ("Naranja Navel 2da x kilo", 0),
        ("Papa Blanca Especial x kilo", 12), ("Papa Rosada Esp premium x kilo", 12), ("Papaya importada x kilo (3u)", 0),
        ("Pepino x kilo", 4), ("Pera Francesa x kilo", 6), ("Pera x kilo Goddard", 0),
        ("Platano importado x kilo", 0), ("Pomelo rosado x kilo", 0), ("Sandia americana x kilo", 0),
        ("Tomate americano Redondo x kilo", 0), ("Tomate Cherry Redondo x kilo", 0), ("Tomate Esp Sur larga vida x kilo", 36),
        ("Tomate perita x kilo", 0), ("Tomate x kilo Goddard", 0), ("Zanahoria x kilo", 38), ("Zapallito x kilo", 38)
    ],
    "MIÉRCOLES": [
        ("Ají Catalán Dulce x kilo", 0), ("Ají Catalán Picante x kilo", 6), ("Anana Imp x unidad", 4),
        ("Banana Brasil x kilo", 0), ("Banana Ecuador x kilo", 18), ("Berenjena x kilo", 38),
        ("Boniato criollo mediano x kilo", 0), ("Boniato Criollo x kilo", 18), ("Boniato zanahoria mediano x kilo", 0),
        ("Boniato zanahoria x kilo", 30), ("Cebolla Especial x kilo", 12), ("Cebolla roja x kilo", 0), ("Cebolla segunda x kilo", 2),
        ("Chaucha comun x kilo", 6), ("Frutilla x kilo", 4), ("Jengibre Imp x kilo", 16),
        ("Kiwi Importado x kilo", 8), ("Lima importada x kilo", 4), ("Limón nacional x kilo", 28),
        ("Limón x kilo Goddard", 0), ("Mandarina Afurer x kilo", 66), ("Mandarina Clementina x kilo", 0),
        ("Mandarina Criolla x kilo", 10), ("Mango importado x unidad (3u)", 15), ("Manzana Crispin x kilo", 20),
        ("Manzana Granny Smith x kilo", 4), ("Manzana Red 2ª x kilo", 0), ("Manzana Red x kilo", 8),
        ("Morron Amarillo x kilo", 8), ("Morron Rojo 2ª x Kilo", 0), ("Morron Rojo x Kilo", 48),
        ("Morron Verde x kilo", 50), ("Naranja esp x kilo", 66), ("Naranja Navel 2da x kilo", 0),
        ("Papa Blanca Especial x kilo", 14), ("Papa Rosada Esp premium x kilo", 10), ("Papaya importada x kilo (3u)", 0),
        ("Pepino x kilo", 6), ("Pera Francesa x kilo", 28), ("Pera x kilo Goddard", 0),
        ("Platano importado x kilo", 0), ("Pomelo rosado x kilo", 0), ("Sandia americana x kilo", 0),
        ("Tomate americano Redondo x kilo", 0), ("Tomate Cherry Redondo x kilo", 0), ("Tomate Esp Sur larga vida x kilo", 80),
        ("Tomate perita x kilo", 6), ("Tomate x kilo Goddard", 0), ("Zanahoria x kilo", 22), ("Zapallito x kilo", 24)
    ],
    "JUEVES": [
        ("Ají Catalán Dulce x kilo", 0), ("Ají Catalán Picante x kilo", 0), ("Anana Imp x unidad", 0),
        ("Banana Brasil x kilo", 0), ("Banana Ecuador x kilo", 0), ("Berenjena x kilo", 12),
        ("Boniato criollo mediano x kilo", 0), ("Boniato Criollo x kilo", 20), ("Boniato zanahoria mediano x kilo", 0),
        ("Boniato zanahoria x kilo", 38), ("Cebolla Especial x kilo", 11), ("Cebolla roja x kilo", 8), ("Cebolla segunda x kilo", 0),
        ("Chaucha comun x kilo", 0), ("Frutilla x kilo", 8), ("Jengibre Imp x kilo", 12),
        ("Kiwi Importado x kilo", 6), ("Lima importada x kilo", 2), ("Limón nacional x kilo", 50),
        ("Limón x kilo Goddard", 0), ("Mandarina Afurer x kilo", 56), ("Mandarina Clementina x kilo", 0),
        ("Mandarina Criolla x kilo", 10), ("Mango importado x unidad (3u)", 0), ("Manzana Crispin x kilo", 0),
        ("Manzana Granny Smith x kilo", 6), ("Manzana Red 2ª x kilo", 10), ("Manzana Red x kilo", 0),
        ("Morron Amarillo x kilo", 0), ("Morron Rojo 2ª x Kilo", 0), ("Morron Rojo x Kilo", 30),
        ("Morron Verde x kilo", 18), ("Naranja esp x kilo", 26), ("Naranja Navel 2da x kilo", 0),
        ("Papa Blanca Especial x kilo", 0), ("Papa Rosada Esp premium x kilo", 0), ("Papaya importada x kilo (3u)", 0),
        ("Pepino x kilo", 0), ("Pera Francesa x kilo", 6), ("Pera x kilo Goddard", 0),
        ("Platano importado x kilo", 0), ("Pomelo rosado x kilo", 0), ("Sandia americana x kilo", 18.5),
        ("Tomate americano Redondo x kilo", 0), ("Tomate Cherry Redondo x kilo", 0), ("Tomate Esp Sur larga vida x kilo", 20),
        ("Tomate perita x kilo", 0), ("Tomate x kilo Goddard", 40), ("Zanahoria x kilo", 42), ("Zapallito x kilo", 0)
    ],
    "VIERNES": [
        ("Ají Catalán Dulce x kilo", 0), ("Ají Catalán Picante x kilo", 0), ("Anana Imp x unidad", 4),
        ("Banana Brasil x kilo", 10), ("Banana Ecuador x kilo", 10), ("Berenjena x kilo", 10),
        ("Boniato criollo mediano x kilo", 20), ("Boniato Criollo x kilo", 20), ("Boniato zanahoria mediano x kilo", 20),
        ("Boniato zanahoria x kilo", 20), ("Cebolla Especial x kilo", 20), ("Cebolla roja x kilo", 18), ("Cebolla segunda x kilo", 2),
        ("Chaucha comun x kilo", 0), ("Frutilla x kilo", 0), ("Jengibre Imp x kilo", 20),
        ("Kiwi Importado x kilo", 6), ("Lima importada x kilo", 2), ("Limón nacional x kilo", 26),
        ("Limón x kilo Goddard", 0), ("Mandarina Afurer x kilo", 50), ("Mandarina Clementina x kilo", 0),
        ("Mandarina Criolla x kilo", 0), ("Mango importado x unidad (3u)", 0), ("Manzana Crispin x kilo", 0),
        ("Manzana Granny Smith x kilo", 0), ("Manzana Red 2ª x kilo", 0), ("Manzana Red x kilo", 4),
        ("Morron Amarillo x kilo", 10), ("Morron Rojo 2ª x Kilo", 6), ("Morron Rojo x Kilo", 34),
        ("Morron Verde x kilo", 22), ("Naranja esp x kilo", 20), ("Naranja Navel 2da x kilo", 0),
        ("Papa Blanca Especial x kilo", 4), ("Papa Rosada Esp premium x kilo", 12), ("Papaya importada x kilo (3u)", 0),
        ("Pepino x kilo", 14), ("Pera Francesa x kilo", 8), ("Pera x kilo Goddard", 0),
        ("Platano importado x kilo", 0), ("Pomelo rosado x kilo", 0), ("Sandia americana x kilo", 0),
        ("Tomate americano Redondo x kilo", 0), ("Tomate Cherry Redondo x kilo", 0), ("Tomate Esp Sur larga vida x kilo", 6),
        ("Tomate perita x kilo", 0), ("Tomate x kilo Goddard", 80), ("Zanahoria x kilo", 20), ("Zapallito x kilo", 22)
    ],
    "SÁBADO": [
        ("Ají Catalán Dulce x kilo", 0), ("Ají Catalán Picante x kilo", 0), ("Anana Imp x unidad", 2),
        ("Banana Brasil x kilo", 20), ("Banana Ecuador x kilo", 0), ("Berenjena x kilo", 16),
        ("Boniato criollo mediano x kilo", 0), ("Boniato Criollo x kilo", 56), ("Boniato zanahoria mediano x kilo", 0),
        ("Boniato zanahoria x kilo", 24), ("Cebolla Especial x kilo", 22), ("Cebolla roja x kilo", 10), ("Cebolla segunda x kilo", 0),
        ("Chaucha comun x kilo", 0), ("Frutilla x kilo", 0), ("Jengibre Imp x kilo", 16),
        ("Kiwi Importado x kilo", 10), ("Lima importada x kilo", 2), ("Limón nacional x kilo", 6),
        ("Limón x kilo Goddard", 0), ("Mandarina Afurer x kilo", 40), ("Mandarina Clementina x kilo", 0),
        ("Mandarina Criolla x kilo", 20), ("Mango importado x unidad (3u)", 3), ("Manzana Crispin x kilo", 0),
        ("Manzana Granny Smith x kilo", 0), ("Manzana Red 2ª x kilo", 0), ("Manzana Red x kilo", 0),
        ("Morron Amarillo x kilo", 0), ("Morron Rojo 2ª x Kilo", 0), ("Morron Rojo x Kilo", 46),
        ("Morron Verde x kilo", 40), ("Naranja esp x kilo", 26), ("Naranja Navel 2da x kilo", 10),
        ("Papa Blanca Especial x kilo", 0), ("Papa Rosada Esp premium x kilo", 22), ("Papaya importada x kilo (3u)", 2),
        ("Pepino x kilo", 10), ("Pera Francesa x kilo", 0), ("Pera x kilo Goddard", 20),
        ("Platano importado x kilo", 4), ("Pomelo rosado x kilo", 2), ("Sandia americana x kilo", 0),
        ("Tomate americano Redondo x kilo", 6), ("Tomate Cherry Redondo x kilo", 0), ("Tomate Esp Sur larga vida x kilo", 12),
        ("Tomate perita x kilo", 0), ("Tomate x kilo Goddard", 120), ("Zanahoria x kilo", 34), ("Zapallito x kilo", 74)
    ]
}

#SELECCIONAMOS EL DÍA
dia = st.selectbox("📅 Selecciona el día", list(productos_por_dia.keys()))
productos = productos_por_dia.get(dia, [])
datos_finales = {}

# ✅ 3. CARGAMOS TU STOCK GUARDADO
st.subheader("🔄 RECUPERAR STOCK GUARDADO")
archivo_subido = st.file_uploader("Sube aquí tu archivo .json guardado", type="json", key="carga_archivo_unico")

if archivo_subido:
    try:
        datos_cargados = json.load(archivo_subido)
        st.session_state.datos_stock = datos_cargados.get("productos", {})
        st.success("✅ ¡TUS NÚMEROS YA ESTÁN CARGADOS!")
    except Exception as e:
        st.error(f"❌ Archivo inválido: {e}")

# === RECORREMOS TODOS LOS PRODUCTOS ===
for indice, (nombre, cantidad_pedir) in enumerate(productos):
    # 1. CARGA LO ÚLTIMO GUARDADO EN LA BASE (si no existe pone 0)
    valor_guardado = datos_base.get(nombre, 0)
    
    # 2. DEFINE EL PASO: 2 para kilos, 1 para unidades
    if "x kilo" in nombre.lower():
        paso = 2
    else:
        paso = 1
    
    # 3. RECUADRO PARA MODIFICAR (usa el valor seguro)
    cantidad = st.number_input(nombre, value=valor_guardado, min_value=0, step=paso, key=f"prod_{indice}")
    
    # 4. SI CAMBIA EL NÚMERO → LO GUARDA AUTOMÁTICAMENTE EN LA BASE
    if cantidad != valor_guardado:
        guardar_cambio(nombre, cantidad)
    
    # === SIGUEN TUS CUENTAS Y COLORES (NO BORRES ESTO) ===
    falta = cantidad_pedir - cantidad
    if falta > 0:
        st.write(f"⚠️ Pedir: {cantidad_pedir} | Tienes: {cantidad} | :red[FALTAN: {falta}]")
    else:
        st.write(f"✅ Pedir: {cantidad_pedir} | Tienes: {cantidad} | :green[COMPLETO: {abs(falta)} DE SOBRANTE]")


# 📥 BOTÓN PARA DESCARGAR RESPALDO (OPCIONAL)
st.subheader("📂 DESCARGAR RESPALDO DE STOCK")
if st.button("GUARDAR Y DESCARGAR COPIA"):
    # Traemos todos los datos frescos de la base
    todos_los_datos = supabase.table("stock_actual").select("*").execute().data
    fecha_archivo = datetime.now().strftime("%d-%m-%Y_%H-%M")
    nombre_archivo = f"stock_respaldo_{fecha_archivo}.json"
    
    # Convertimos a formato descargable
    import json
    contenido_json = json.dumps(todos_los_datos, indent=2, ensure_ascii=False)
    
    st.download_button(
        label="📥 BAJAR ARCHIVO",
        data=contenido_json,
        file_name=nombre_archivo,
        mime="application/json"
    )
    st.success("✅ RESPALDO DESCARGADO CON ÉXITO!")
