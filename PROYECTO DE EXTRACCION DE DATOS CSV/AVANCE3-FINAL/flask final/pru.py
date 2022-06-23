from flask import Flask, render_template
app = Flask(__name__)
import numpy as np
import pandas as pd 
#from scipy.spatial.distance import euclidean
#from pandas import DataFrame

data = pd.read_csv ('ttt.csv')
n = data[data.columns[1:]].to_numpy()
m = data[data.columns[0]].to_numpy()

################################################################################
@app.route("/")
def principal():
    nom="🤖🔩PROYECTO FINAL DE IA🤖🔩"
    tem="SISTEMA RECOMENDADOR"
    inte="Realizado por:"
    a="/🌱Larico Yucra,Cristhian Denis"
    b="/🌱Llerena Pastor,Jhordan Alexander"
    c="/🌱Prieto Tito, Manuel Ismael "
    d="/🌱Challco Ancasi, Cesar Augusto"
    e="/🌱Mamani Alvarez, Rudy "
    com="Curso : Computacion1"
    prof="Profesor"
    pronom="Renzo Gustavo Bolivar Valdivia"
    gt="Los sistemas de recomendación forman parte de un sistema de filtrado de información, los cuales presentan distintos tipos de temas o ítems de información (películas, música, libros, noticias, imágenes, páginas web, regalos, etc.) que son del interés de un usuario en particular. Generalmente, un sistema recomendador compara el perfil del usuario con algunas características de referencia de los temas, y busca predecir el baremo o ponderación que el usuario le daría a un ítem que aún el sistema no ha considerado. Estas características pueden basarse en la relación o acercamiento del usuario con el tema o en el ambiente social del mismo usuario."
    nin="Nuestro  sistema recomendador se centra en los gustos por la comida , para ello se hizo una encuesta  y en esta se utilizo la escala de likert."
    kil=" La encuesta la realizamos en Google-Form donde la persona a encuestar nos dara una opinion acerca de los gustos que tiene sobre la COMIDAS PERUANA .Este respondera en una escala de 1 a 5 donde  :"
    lol="💡Si escoge 1, no le  gusta la comida propuesta."
    kol="💡Si escoge 5, si el encanta la comida propuesta."
    return render_template("inicio.html",nom=nom,a=a,b=b,c=c,d=d,e=e, inte=inte,com=com, prof=prof, pronom=pronom,tem=tem,gt=gt,nin=nin,kil=kil,lol=lol,kol=kol)

################################################################################

@app.route("/objetivo")
def objetivos():
    d="OBJETIVOS"
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
    
    ed="MATRIZ"
    coo="¿Qué es la Distancia Euclidiana?"
    caa="¿Qué es la Correlacion de Pearson?"
    man="La distancia euclidiana o euclídea, es la distancia ordinaria entre dos puntos de un espacio euclídeo, la cual se deduce a partir del teorema de Pitágoras."
    vee="Para hallar la matriz es necesario la utilización de dos formulas , una de ellas es la Distancia Euclidiana  y también la Correlación de Pearson."
    naa="El coeficiente de correlación de Pearson es una medida de dependencia lineal entre dos variables aleatorias cuantitativas.  El coeficiente de correlación puede tomar un rango de valores de +1 a -1. Un valor de 0 indica que no hay asociación entre las dos variables. Un valor mayor que 0 indica una asociación positiva y Un valor menor que 0 indica una asociación negativa."
    inte="Realizado por:"
    rel="🏁 RESULTADOS"
    res="Los resultados de similitud obtenidos en Comidas del Perú según la tabla de Correlación con los siguientes encuestados:"
    pof="hendersonwido@gmail.com ----------  aapazatt@unsa.edu.pe=====>0.231662"
    pra="aapazatt@unsa.edu.pe    ----------     hendersonwido@gmail.com=====>0.231662"
    pif="ruizcruza9@gmail.com     ----------    cchallcoa@unsa.edu.pe=====>0.210897"
    pin="cchallcoa@unsa.edu.pe    ----------    ruizcruza9@gmail.com =====>0.210897"
    gor="kmejiah@unsa.edu.pe       ----------   madelyquispe793@unsa.edu.pe =====> 0.205213"
    into="madelyquispe793@unsa.edu.pe ---------- kmejiah@unsa.edu.pe   =====>   0.205213"
    trr="Validacion-matriz de correlacion"
    pinta="hendersonwido@gmail.com  ----------    aapazatt@unsa.edu.pe   =====>   0.184527"
    mela="aapazatt@unsa.edu.pe     ----------    hendersonwido@gmail.com  =====>   0.184527"
    cris="cchallcoa@unsa.edu.pe     ----------   ruizcruza9@gmail.com   =====>   0.137099"
    hhh="ruizcruza9@gmail.com      ----------   cchallcoa@unsa.edu.pe   =====>   0.137099"
    kkk="kmejiah@unsa.edu.pe     ----------     madelyquispe793@unsa.edu.pe  =====> 0.121538"
    ooo="madelyquispe793@unsa.edu.pe ---------- kmejiah@unsa.edu.pe    =====>   0.121538"
    cpp="dtype: float64"
    a="/🌱Larico Yucra,Cristhian Denis"
    b="/🌱Llerena Pastor,Jhordan Alexander"
    c="/🌱Prieto Tito, Manuel Ismael "
    d="/🌱Challco Ancasi, Cesar Augusto"
    e="/🌱Mamani Alvarez, Rudy "
    return render_template("datos.html",ooo=ooo,kkk=kkk,hhh=hhh,trr=trr,cpp=cpp,cris=cris,mela=mela,pinta=pinta,into=into,gor=gor,pin=pin,pra=pra,pif=pif,pof=pof,ed=ed,a=a,b=b,c=c,d=d,e=e, inte=inte, vee=vee,coo=coo, naa=naa,caa=caa,man=man,rel=rel,res=res)

################################################################################
@app.route('/encuesta')
def resultado():
    cone="El proyecto de Investigación tiene como finalidad de hallar la similitud de gustos entre los encuestados en el área de comida, a través de una google forms donde se sustrajo los datos en el cual se recopiló la cantidad de 30 encuestados, por consiguiente se realizó la extracción de datos en una hoja de cálculo,luego se hizo una limpieza de datos de manera manual y se convirtió en números simples y se procedio a descargar un csv separado por comas."
    pru="A continuación puede visualizar la encuesta realizada y los resultados en una tabla."
    gu="ENCUESTA "
    inte="Realizado por:"
    a="/🌱Larico Yucra,Cristhian Denis"
    b="/🌱Llerena Pastor,Jhordan Alexander"
    c="/🌱Prieto Tito, Manuel Ismael "
    d="/🌱Challco Ancasi, Cesar Augusto"
    e="/🌱Mamani Alvarez, Rudy "
    return render_template("resultado.html",gu=gu,a=a,b=b,c=c,d=d,e=e, inte=inte , cone=cone,pru=pru)

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
@app.route('/conclusiones')
def conclu():
    ccc="Realizado por:"
    aaa="/🌱Larico Yucra,Cristhian Denis"
    bbb="/🌱Llerena Pastor,Jhordan Alexander"
    ddd="/🌱Prieto Tito, Manuel Ismael "
    eee="/🌱Challco Ancasi, Cesar Augusto"
    fff="/🌱Mamani Alvarez, Rudy "
    titu2= "Conclusiones"
    conlu1 ="📌 Podemos concluir que con este proyecto de Inteligencia Artificial, se pudo poner a prueba los conocimientos adquiridos como el aprendizaje del lenguaje PYTHON, así también como el manejo de la plataforma GITLAB para evidenciar cada avance y todo el manejo desde el sistema operativo LINUX."
    conlu2 ="📌 Para el desarrollo del presente proyecto se hizo uso de jupyter notebook y de librerias como numpy y pandas, también se hizo uso spyder para poder crear la pagina en flask y poder plasmar los resultados finales del proyecto de inteligencia articial."
    conlu3 ="📌 La participación, planificación y el trabajo en equipo fue determinante para poder ver avances del proyecto donde cada integrante aporto con sus conocimientos y aptitudes."
    return render_template("conclusiones.html" ,titu2=titu2, conlu1=conlu1 , conlu2=conlu2, conlu3=conlu3 ,ccc=ccc,aaa=aaa,bbb=bbb,ddd=ddd,eee=eee,fff=fff)
################################################################################
@app.route('/tabla')
def tabla():
    data = pd.read_csv('ttt.csv')
    
    return data.to_html()

@app.route('/validacion')
def validacion():
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
    nampa_matriz=np.corrcoef(da)
    correlacion=pd.DataFrame(nampa_matriz,columns=m,index=m)
    correlacion.round(decimals=4)
    return (correlacion.to_html())

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