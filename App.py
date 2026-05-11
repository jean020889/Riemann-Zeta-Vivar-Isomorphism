import streamlit as st
import pandas as pd

# Configuración visual
st.set_page_config(page_title="Cotizador Alumetal - Perfil Nacional", page_icon="🪟")

@st.cache_data
def cargar_datos():
    # Intenta leer el archivo local del repositorio clonado
    return pd.read_csv('precios.csv')

try:
    df = cargar_datos()
    
    st.title("🪟 Cotizador: Ventana Perfil Nacional")
    st.info("Cálculo basado en 4 perfiles principales y vidrio claro.")

    with st.sidebar:
        st.header("Ajustes de Cotización")
        margen = st.slider("Margen de Utilidad (%)", 10, 100, 35)
        mano_obra = st.number_input("Costo Mano de Obra ($)", value=15.0)

    # Entradas de Medidas
    col1, col2 = st.columns(2)
    with col1:
        ancho = st.number_input("Ancho de la ventana (m)", min_value=0.1, value=1.0, step=0.01)
    with col2:
        alto = st.number_input("Alto de la ventana (m)", min_value=0.1, value=1.0, step=0.01)

    if st.button("CALCULAR PRECIO FINAL"):
        # 1. [span_2](start_span)[span_3](start_span)Obtener precios desde el CSV[span_2](end_span)[span_3](end_span)
        # Perímetro para el Marco (Jamba de marco ventana Blanco)
        p_marco = df.loc[df['item'] == 'Jamba de marco de ventana Blanco', 'precio_unitario'].values[0]
        # Perímetro para la Hoja (Horizontal para hoja de ventana Blanco)
        p_hoja = df.loc[df['item'] == 'Horizontal para hoja de ventana Blanco', 'precio_unitario'].values[0]
        # [span_4](start_span)Vidrio Claro 6mm[span_4](end_span)
        p_vidrio = df.loc[df['item'] == 'Vidrio Claro 6mm', 'precio_unitario'].values[0]
        # [span_5](start_span)Kit de accesorios básico[span_5](end_span)
        p_kit = df.loc[df['item'] == 'Rueda doble ventana', 'precio_unitario'].values[0] * 2

        # 2. Lógica de cálculo (Estimación de tramos de 6m)
        metros_perfil = (ancho * 4) + (alto * 4) # Estimación para 4 perfiles
        costo_aluminio = (metros_perfil / 6) * ((p_marco + p_hoja) / 2)
        costo_vidrio = (ancho * alto) * p_vidrio
        
        costo_total_base = costo_aluminio + costo_vidrio + p_kit + mano_obra
        precio_final = costo_total_base * (1 + (margen / 100))

        # 3. Mostrar Resultados
        st.success(f"## Precio de Venta: ${precio_final:,.2f}")
        
        with st.expander("Ver Desglose de Costos"):
            st.write(f"**Costo Aluminio (Nacional):** ${costo_aluminio:.2f}")
            st.write(f"**Costo Vidrio (6mm):** ${costo_vidrio:.2f}")
            st.write(f"**Accesorios e Insumos:** ${p_kit:.2f}")
            st.write(f"**Mano de Obra:** ${mano_obra:.2f}")

except Exception as e:
    st.error(f"Error al cargar 'precios.csv': {e}")
    st.warning("Asegúrate de que el archivo CSV esté en la raíz de tu repositorio.")
  
