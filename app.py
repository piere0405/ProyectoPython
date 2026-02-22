import streamlit as st
import pandas as pd 
st.set_page_config(page_title="Proyecto Python", layout="wide")

menu = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

if menu == "Home" :
    st.markdown("""
        <h1 style="text-align:center;">📌 Bienvenido al proyecto Python</h1>

        <div style="
            text-align:center;
            line-height: 1.6;
        ">

        <p><b>Título del proyecto:</b> Proyecto Python Fundamentals</p>

        <p><b>Nombre completo:</b> Jeampiere Manuel Pocomucha Toribio</p>

        <p><b>Curso o módulo:</b> Especialización en Python for Analytics</p>

        <p><b>Año:</b> 2026</p>

        <p><b>Objetivo del trabajo:</b><br>
        El objetivo de este trabajo es consolidar el aprendizaje de los fundamentos de Python,
        aplicando de manera práctica conceptos clave del lenguaje en una aplicación desarrollada
        con Streamlit.
        </p>

        <p><b>Tecnologías utilizadas:</b><br>
        Python, Streamlit, Pandas
        </p>

        </div>
         <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7af4X8L1bxX4SN6KUxzJL5r3wvxD9ZBrZbQ&s" width="400"> 
         <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStp37DY0hZuEV4QjkiUXSTy345MrM9YbvZTQ&s " width="400"> 
         <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSyk_NeHE7s3IVDEP1ZhtHTP3t9Mzk1rIH4g&s " width="350">           
        """, unsafe_allow_html=True)
    
elif menu == "Ejercicio 1" :
    st.title("Ejercicio 1 – Variables y Condicionales")
    presupuesto = st.number_input("INGRESA  PRESUPUESTO : ",step=1)
    gasto = st.number_input("INGRESA GASTO A REALIZAR : ",step=1)
    if st.button("calcular") :
        resta = presupuesto - gasto
        if resta == 0 :
            st.success("PRESUESTO ALCANZA EXACTO")
        elif resta > 0 :
            st.success(f"GASTO DENTRO DEL PRESUPUESTO CON SOBRANTE DE {resta}")
        else :
            st.warning(f"GASTO EXEDE PRESUPUESTO CON UN SOBREGITRO DE {gasto - presupuesto}") 


elif menu == "Ejercicio 2" :
    st.title("Ejercicio 2 – Registro de actividades financieras")

    if "actividades" not in st.session_state :
        st.session_state.actividades = []
    
    nombre = st.text_input("NOMBRE DE LA ACTIVIDAD")
    tipo = st.selectbox("TIPO DE ACTIVIDAD",["INVERSION" , "GASTOS PERSONALES" , "AHORRO"])
    presupuesto = st.number_input("INGRESE PRESUPUESTO")
    gasto = st.number_input("INGRESE GASTO")
    
    if st.button("AGREGAR ACTIVIDAD") :
        actividad = {
            "nombre" : nombre ,
            "tipo" : tipo,
            "presupuesto" : presupuesto,
            "gasto" : gasto
        }
        st.session_state.actividades.append(actividad)
        st.success("SE AGREGO ACTIVIDAD CORRECTAMENTE")

    if st.session_state.actividades :
        df = pd.DataFrame(st.session_state.actividades)
        estados = []
        for a in st.session_state.actividades :
            if a["gasto"] <= a["presupuesto"] :
               estados.append("Se encuentra dentro del presupuesto")
            else :
               estados.append("No esta dentro del presupuesto")
        df["estado"]=estados            
        st.write("ESTADOS DE LAS ACTIVIDADES")
        st.dataframe(df) 
           
elif menu == "Ejercicio 3" :
   st.subheader("3 – Funciones y Programación Funcional")

   actividad = {
        "nombre": "Actividad de prueba",
        "presupuesto": st.number_input(
            "Presupuesto de la actividad",
            min_value=0.0
        )
    }

   tasa = st.slider(
        "Tasa de retorno",
        min_value=0.0,
        max_value=1.0,
        step=0.01
    )
   meses = st.number_input("Meses", min_value=1, step=1)

   def calcular_retorno(actividad, tasa, meses):
            return actividad["presupuesto"] * tasa * meses

   if st.button("Calcular retorno"):
            retornos = list(
                map(
                    lambda act: calcular_retorno(act, tasa, meses),
                    [actividad]
                )
            )
            st.write(
                f"Retorno esperado: {retornos[0]:.2f}"
            )
elif menu == "Ejercicio 4" :
    st.title("Ejercicio 4 – Programación Orientada a Objetos (POO)")

    class Actividad:
      def __init__(self, nombre, tipo, presupuesto, gasto_real):
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = presupuesto
        self.gasto_real = gasto_real

      def esta_en_presupuesto(self):
            if self.gasto_real > self.presupuesto:
                return False
            else:
                return True

      def mostrar_info(self):
            return f"""
            Actividad: {self.nombre}
            Tipo: {self.tipo}
            Presupuesto: {self.presupuesto}
            Gasto real: {self.gasto_real}
            """

   
    nombre1 = st.text_input("NOMBRE DE LA ACTIVIDAD")
    tipo1 = st.selectbox("TIPO DE ACTIVIDAD", ["INVERSION", "GASTOS PERSONALES", "AHORRO"])
    presupuesto1 = st.number_input("INGRESE PRESUPUESTO", min_value=0.0)
    gasto1 = st.number_input("INGRESE GASTO", min_value=0.0)


    if st.button("CREAR ACTIVIDAD"):
        actividad = Actividad(nombre1, tipo1, presupuesto1, gasto1)

        st.write(actividad.mostrar_info())

        if actividad.esta_en_presupuesto():
            st.success("DENTRO DEL PRESUPUESTO ")
        else:
            st.error("FUERA DEL PRESUPUESTO ")  