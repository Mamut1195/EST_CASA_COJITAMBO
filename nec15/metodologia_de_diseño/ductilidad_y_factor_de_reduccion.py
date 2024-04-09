from jinja2 import Template

latex_template = r"""
\section{Factor de reducci\'on de respuesta R}
La NEC nos indica que el valor del factor de reducci\'on debe ser escogido de acuerdo a criterios relacionados con aspectos de agrupamiento de 
estructuraci\'on, diferencias entre realidades constructivas y de calidad entre los materiales y la construcci\'on, penalizaciones dirigidas hacia cierto tipo de estructuras 
que no permiten 
disponer de ductilidad global apropiada para soportar las deformaciones inel\'asticas requeridas por el sismo de dise\~{n}o. As\'i
tambi\'en depende del tipo de suelo, periodo de vibraci\'on considerado, factores de ductilidad, sobre resistencia, 
redundancia y amortiguamiento de una estructura en condiciones l\'imite.

Inicialmente el valor de R se escoge de la tabla 11 de la NEC-SE-DS, para posteriormente reducirlo de acuerdo a las irregularidades
presentes en la estructura.

\section{Irregularidades estructurales}
Las irregularidades estructurales son desviaciones o caracter\'isticas no deseables en la geometr\'ia, la distribuci\'on 
de masa o la rigidez de un edificio o estructura que pueden afectar su comportamiento s\'ismico y su capacidad para resistir fuerzas laterales, como las producidas por un terremoto. Estas irregularidades pueden influir en la distribuci\'on de las fuerzas y las deformaciones dentro de la estructura 
durante un evento s\'ismico, lo que a su vez puede afectar la seguridad y la estabilidad del edificio. Se clasifiacan en dos tipos,
irregularidades en planta, irregularidades en elevaci\'on.

\subsection{Irregularidades en planta}
\subsubsection{Irregularidad Torsional }
Existe irregularidad por torsi\'on, cuando la m\'axima deriva de piso de un extremo de la estructura calculada incluyendo la torsi\'on accidental y medida perpendicularmente a un eje determinado, es mayor que 1,2 veces la 
deriva promedio de los extremos de la estructura con respecto al mismo eje de referencia.
$$\vartriangle = 1.2 \cdot \dfrac{\vartriangle 1 + \vartriangle 2}{2}$$

\begin{figure}[h]
    \centering
    \includegraphics[width=0.15\textwidth]{imagenes/irregularidad_torsional.png}
\end{figure}

\subsubsection{Retrocesos excesivos en las esquinas }
La configuraci\'on de una estructura se considera irregular cuando presenta entrantes excesivos en sus esquinas. 
Un entrante en una esquina se considera excesivo cuando las proyecciones de la estructura, a ambos lados del entrante, 
son mayores que el 15\% de la dimensi\'on de la planta de la estructura en la direcci\'on del entrante.
$$A > 0.15B y C > 0.15D$$

\begin{figure}[h]
    \centering
    \includegraphics[width=0.15\textwidth]{imagenes/retrocesos_excesivos_en_las_esquinas.png}
\end{figure}

\subsubsection{Discontinuidades en el sistema de piso }
La configuraci\'on de la estructura se considera irregular cuando el sistema de piso tiene discontinuidades apreciables o variaciones 
significativas en su rigidez, incluyendo las causadas por aberturas, entrantes o huecos, con \'areas mayores al 50\% del 
\'area total del piso o con cambios en la rigidez en el plano del sistema de piso de m\'as del 50\% entre niveles consecutivos.
$$CxD > 0.5AxB $$
$$[CxD + CxE] > 0.5AxB$$

\begin{figure}[h]
    \centering
    \includegraphics[width=0.15\textwidth]{imagenes/discontinuidades_en_el_sistema_de_piso.png}
\end{figure}

\subsubsection{Ejes estrucutrales no paralelos }
La estructura se considera irregular cuando los ejes estructurales no son paralelos o sim\'etricos 
con respecto a los ejes ortogonales principales de la estructura.

\begin{figure}[h]
    \centering
    \includegraphics[width=0.15\textwidth]{imagenes/ejes_estructurales_no_paralelos.png}
\end{figure}

\subsection{Irregularidades en elevaci\'on }

\subsubsection{Piso flexible }
La estructura se considera irregular cuando la rigidez lateral de un piso es menor que el 70\% de la rigidez 
lateral del piso superior o menor que el 80 \% del promedio de la rigidez lateral de los tres pisos superiores.
$$K_C < 0.70K_D$$
$$K_C < 0.80 \cdot \dfrac{K_D + K_E + K_F}{3}$$

\begin{figure}[h]
    \centering
    \includegraphics[width=0.15\textwidth]{imagenes/piso_flexible.png}
\end{figure}

\subsubsection{Distribuci\'on de masa }
La estructura se considera irregular cuando la masa de cualquier piso es mayor que 1,5 veces la masa 
de uno de los pisos adyacentes, con excepci\'on del piso de cubierta que sea m\'as liviano que el piso inferior.
$$m_D = 1.50m_E \text{ \'o } m _D > 1.50 m_C$$

\begin{figure}[h]
    \centering
    \includegraphics[width=0.15\textwidth]{imagenes/distribucion_de_masa.png}
\end{figure}

\subsubsection{Irregularidad geom\'etrica }
La estructura se considera irregular cuando la dimensi\'on en planta del sistema resistente en cualquier piso 
es mayor que 1,3 veces la misma dimensi\'on en un piso adyacente, exceptuando el caso de los altillos de un solo piso.
$$a > 1.3b$$

\begin{figure}[h]
    \centering
    \includegraphics[width=0.15\textwidth]{imagenes/irregularidad_geometrica.png}
\end{figure}
"""

template = Template(latex_template)

# Rellena la plantilla con el valor de la variable
latex_output = template.render()

# Abre el archivo en modo de escritura, pero con la opción de añadir
file_path = r"memoria\memoria_de_cálculo_cojitambo.tex"
with open(file_path, "a") as f:
    f.write(latex_output)

print("Archivo LaTeX generado exitosamente:", file_path)
print("Recuerda revisar que '/end{document}' se encuentre al final del archivo")
print("También que los caracteres latinos y tildes")