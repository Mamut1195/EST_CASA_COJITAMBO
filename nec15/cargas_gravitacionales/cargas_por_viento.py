from jinja2 import Template

#Carga de viento
#Velocidad instantanea máxima del viento
V = 21 #m/s

#Coeficiente de correlación según tabla 5
COEFICIENTE_DE_CORRELACION = 0.91

#Velocidad corregida del viento
velocidad_corregida = V * COEFICIENTE_DE_CORRELACION

##Solo se calculará para la cubierta

#Densidad del aire
DENSIDAD_DEL_AIRE = 1.25 #kg/m3

#Coeficiente de entorno/altura
c_e_barlovento = 0.3

c_e_sotavento = -0.6

#Coeficiente de forma
c_f = 0.8

#Barlovento
barlovento = 0.5 * DENSIDAD_DEL_AIRE * (velocidad_corregida ** 2) * c_e_barlovento * c_f #N/m2

BARLOVENTO = barlovento * 0.001 #kN/m2

#Sotavento
sotavento = 0.5 * DENSIDAD_DEL_AIRE * (velocidad_corregida ** 2) * c_e_sotavento * c_f #N/m2

SOTAVENTO = sotavento * 0.001 #kN/m2

latex_template = r"""
\section{Cargas Por viento}
Para obtener las cargas por viento primero hay que calcular la velocidad del viento. Para esto la 
NEC nos da la siguiente f\'ormula: 
$$V_b = V \cdot \alpha$$

Donde:

$V_b$: Velocidad corregida del viento en $m/s$

$V$: Velocidad instant\'anea m\'axima del viento en m/s, registrada a 10 m de altura sobre el terreno.

\begin{table}[h]
    \centering
    \begin{tabular}{|c|c|c|}
    \hline
    Coef. de correlaci\'on&Velocidad instant\'anea&Velocidad corregida\\
    &(m/s)&(m/s)\\
    \hline
    {{ COEFICIENTE_DE_CORRELACION }}&{{ V }}&{{ velocidad_corregida }}\\
    \hline
    \end{tabular}
\end{table}

\subsection{Presi\'on del viento}
La NEC establece la siguiente f\'ormula para el c\'alculo de la presi\'on del viento:
$$P = \frac{1}{2} \rho V_b^2 c_e c_f$$

Donde:

$P$: Presi\'on de c\'alculo expresada en Pa $N/m^2$

$\rho$: Densidad del aire expresada en $Kg/m^3$ (En general, se puede adoptar 1.25 $Kg/m^3$)

$c_e$ : Coeficiente de entorno/altura

$c_f$ : Coeficiente de forma


Con la f\'ormula se obtienen los valores del Barlovento y Sotavento, cuyos valores son presentados
en las siguientes tablas.

\begin{table}[h]
    \centering
    \resizebox{\textwidth}{!}{
    \begin{tabular}{|c|c|c|c|c|}
        \hline
        Densidad del aire ($kg/m^3$) & Velocidad del viento ($m/s$) & Coef. Entorno/altura & Coef. De forma & Barlovento ($kN/m^2$)\\
        \hline
        {{ DENSIDAD_DEL_AIRE }}&{{ velocidad_corregida }}&{{ c_e_barlovento }}&{{ c_f }}&{{ BARLOVENTO }}\\
        \hline
    \end{tabular}
    }
\end{table}

\begin{table}[h]
    \centering
    \resizebox{\textwidth}{!}{
    \begin{tabular}{|c|c|c|c|c|}
        \hline
        Densidad del aire ($kg/m^3$) & Velocidad del viento ($m/s$) & Coef. Entorno/altura & Coef. De forma & Barlovento ($kN/m^2$)\\
        \hline
        {{ DENSIDAD_DEL_AIRE }}&{{ velocidad_corregida }}&{{ c_e_sotavento }}&{{ c_f }}&{{ SOTAVENTO }}\\
        \hline
    \end{tabular}
    }
\end{table}

"""

template = Template(latex_template)

# Rellena la plantilla con el valor de la variable
latex_output = template.render(velocidad_corregida = velocidad_corregida,
                               DENSIDAD_DEL_AIRE = DENSIDAD_DEL_AIRE,
                               c_e_barlovento = c_e_barlovento,
                               c_e_sotavento = c_e_sotavento,
                               c_f = c_f,
                               SOTAVENTO = SOTAVENTO,
                               BARLOVENTO = BARLOVENTO,
                               COEFICIENTE_DE_CORRELACION = COEFICIENTE_DE_CORRELACION,
                               velociadad_instantanea = V
                               )

# Abre el archivo en modo de escritura, pero con la opción de añadir
file_path = r"memoria\memoria_de_cálculo_cojitambo.tex"
with open(file_path, "a") as f:
    f.write(latex_output)

print("Archivo LaTeX generado exitosamente:", file_path)
print("Recuerda revisar que '/end{document}' se encuentre al final del archivo")
print("También que los caracteres latinos y tildes")