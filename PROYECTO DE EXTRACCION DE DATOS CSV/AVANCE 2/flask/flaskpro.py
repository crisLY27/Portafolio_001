from flask import Flask, render_template, request
app = Flask(__name__)
import numpy as np
import pandas as pd
#from scipy.spatial.distance import euclidean
#from pandas import DataFrame

data = pd.read_csv ('tt.csv')
n = data[data.columns[1:]].to_numpy()
m = data[data.columns[0]].to_numpy()

################################################################################
@app.route("/")
def principal():
    nom="🤖🔩PROYECTO FINAL DE IA🤖🔩"
    tem="🥩 Comidas Peruanas 🥩"
    inte="Realizado por:"
    a="/🌱Larico Yucra,Cristhian Denis"
    b="/🌱Llerena Pastor,Jhordan Alexander"
    c="/🌱Prieto Tito, Manuel Ismael "
    d="/🌱Challco Ancasi, Cesar Augusto"
    e="/🌱Mamani Alvarez, Rudy "
    com="Curso : Computacion1"
    prof="Profesor"
    pronom="Renzo Gustavo Bolivar Valdivia"
    gt="Bienvenido a nuestra primera pagina hecha con un poquito de todo.En esta página encontraras la similitud que hay en 30 encuestados, para esto es necesario hallar principalmente la distancia euclidiana."
    nin="Esta distancia Euclidiana costa en tomar los dos resultados que sale entre los encuestados y restarlos entre sí, así sucesivamente hasta terminar con cada una de las preguntas propuestas."
    kil="Seguro te preguntaras y esto para que es necesario, pues esto muy necesario ya que gracias a ello podremos hallar la Similitud de Pearson."
    lol="Esta Similitud de Pearson o (Coeficiente de Correlación) nos sirve para hallar la similitud que tienen los encuestados, para saber que gustos tan parecidos tienen (Gustos=por lo de comida, nuestro tema)."
    kol="Para un mejor entendimiento   en la parte superior podrás ver de una mejor manera todo lo que el Grupo 3 hizo en su proyecto de computación."
    return render_template("inicio.html",nom=nom,a=a,b=b,c=c,d=d,e=e, inte=inte,com=com, prof=prof, pronom=pronom,tem=tem,gt=gt,nin=nin,kil=kil,lol=lol,kol=kol)


################################################################################

@app.route("/objetivo")
def objetivos():
    d="**Objetivos**"
    g= "Competencia Comunicativa"
    i="-Para esto nosotros utilizamos el lenguaje de programación de Python utilizando los archivos de Jupyter Notebook Llegando asi a mostrar nuestros resultados."
    k="Competencia de aprendizaje"
    l="-Para esto nosotros usamos las aptitudes  en Descomposición.Esto quiere decir que el trabajo se dividió en diversas  partes las cuales tenías que avanzar una para continuar con la otra .Llegando así a resolver todo el problema que se nos propuso"
    e="-Reconocimos  los patrones (hallando la similitud  entre los encuestados ),abstracción (omitiendo la información innecesaria , en los casos de NaN), creando algoritmos (para que  se cree así una tabla con  los correos de cada encuestados )"
    o="Competencia de trabajo en Equipo"
    p="-Contamos con la habilidad de cada uno de ellos integrantes , resolviendo los problemas  y  fallas que se nos atravesará en el camino Llegando a cumplir la tarea propuesta"
    n="-Finalmente llegando a sincronizar con el servidos GitLab  con los comandos Git."
    inte="Realizado por:"
    a="/🌱Larico Yucra,Cristhian Denis"
    b="/🌱Llerena Pastor,Jhordan Alexander"
    c="/🌱Prieto Tito, Manuel Ismael "
    de="/🌱Challco Ancasi, Cesar Augusto"
    el="/🌱Mamani Alvarez, Rudy "
    return render_template("objetivo.html", d=d , g=g , i=i ,k=k ,l=l ,e=e ,o=o ,p=p,n=n,a=a,b=b,c=c,de=de,el=el, inte=inte)
################################################################################
@app.route('/datos')
def datos():
    ed="Datos  y tablas de nuestra encuesta 📄📝✏️"
    inte="Realizado por:"
    a="/🌱Larico Yucra,Cristhian Denis"
    b="/🌱Llerena Pastor,Jhordan Alexander"
    c="/🌱Prieto Tito, Manuel Ismael "
    d="/🌱Challco Ancasi, Cesar Augusto"
    e="/🌱Mamani Alvarez, Rudy "
    return render_template("datos.html",ed=ed,a=a,b=b,c=c,d=d,e=e, inte=inte)

################################################################################
@app.route('/resultados')
def resultado():
    gu="❔📝Nuestra encuesta utilizada 📝❔"
    inte="Realizado por:"
    a="/🌱Larico Yucra,Cristhian Denis"
    b="/🌱Llerena Pastor,Jhordan Alexander"
    c="/🌱Prieto Tito, Manuel Ismael "
    d="/🌱Challco Ancasi, Cesar Augusto"
    e="/🌱Mamani Alvarez, Rudy "
    return render_template("resultado.html",gu=gu,a=a,b=b,c=c,d=d,e=e, inte=inte)

################################################################################
@app.route('/referencias')
def referencia():
    ñl="🌱Analyticslane:"
    lo="Inicialización de arrays con ceros con np.zeros() https://www.analyticslane.com/2019/10/09/numpy-basico-inicializacion-de-arrays-en-numpy/"
    ju="🌱Stackoverflow:"
    de="Los pares de correlación más altos de una matriz de correlación .unstack( ) https://stackoverflow.com/questions/17778394/list-highest-correlation-pairs-from-a-large-correlation-matrix-in-pandas"
    jo="🌱Youtube:"
    ko="🚩Python y la librería Pandas. https://www.youtube.com/watch?v=aoQtF_-rhTI"
    lp="🚩Valores NaN (nulo) https://www.youtube.com/watch?v=PAU92GUyEt4"
    ki="🚩Valores perdidos en pandas https://www.youtube.com/watch?v=fCMrO_VzeL8"
    kl="🌱Pandas:"
    ji="pandas.DataFrame.sort_values https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.sort_values.html"
    pñ="Para la realización de nuestro trabajo utilizamos varias Paginas Web y videos de Youtube , son las siguientes:"
    inte="Realizado por:"
    a="/🌱Larico Yucra,Cristhian Denis"
    b="/🌱Llerena Pastor,Jhordan Alexander"
    c="/🌱Prieto Tito, Manuel Ismael "
    d="/🌱Challco Ancasi, Cesar Augusto"
    e="/🌱Mamani Alvarez, Rudy "
    ac="Referencia Utilizadas ✏️📤"
    return render_template("referencia.html",ñl=ñl,lo=lo,ju=ju,de=de,jo=jo,ko=ko,lp=lp,ki=ki,kl=kl,ji=ji,pñ=pñ,a=a,b=b,c=c,d=d,e=e, inte=inte,ac=ac)
################################################################################
@app.route('/tabla')
def tabla():
    data = pd.read_csv('tt.csv')
    
    return data.to_html()

@app.route('/validacion')
def validacion():
    return render_template("validacion.html")

@app.route('/data')
def data():
    vector=len(m)
    matriz= np.zeros((vector,vector))

    for i in range(vector):
        for j in range(vector):
            if j and i== np.NaN:
                continue
            else:
                dist=np.sqrt(np.nansum((n[i]-n[j])**2))
                simil=(1/(1+dist))
                matriz[i][j] = simil
        
    da = pd.DataFrame(matriz,columns=m,index=m)
    da.round(decimals=4)
    return (da.to_html())
if __name__ == "__main__":
	app.run(debug=True)