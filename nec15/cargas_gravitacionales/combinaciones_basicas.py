from jinja2 import Template

from cargas_gravitacionales.carga_permanente import CARGA_MUERTA
from cargas_gravitacionales.cargas_de_granizo import CARGA_DE_GRANIZO
from cargas_gravitacionales.cargas_por_viento import BARLOVENTO, SOTAVENTO
from cargas_gravitacionales.sobrecarga_cubierta import SOBRECARGA_CUBIERTA
from cargas_gravitacionales.cargas import CargasNEC15

CARGA_MUERTA = CARGA_MUERTA
CARGA_DE_GRANIZO = CARGA_DE_GRANIZO
BARLOVENTO = BARLOVENTO
SOTAVENTO = SOTAVENTO
SOBRECARGA_CUBIERTA = SOBRECARGA_CUBIERTA
diccionario_de_cargas = CargasNEC15()
diccionario_de_cargas.add_to_dict_carga_permanente(CARGA_MUERTA)
diccionario_de_cargas.add_to_dict_sobrecarga_cubierta(SOBRECARGA_CUBIERTA)
diccionario_de_cargas.add_to_dict_carga_de_barlovento(BARLOVENTO)
diccionario_de_cargas.add_to_dict_carga_de_sotavento(SOTAVENTO)


latex_template = r"""
\subsection{Combinaciones para el dise\~no de \'ultima resistencia}
La NEC se\~nala que las estructuras, componentes y cimentaciones deber'an dise\~narse
para que la resistencia de dise\~no iguale o supere las siguientes combinaciones:

\begin{enumerate}
    \item \textbf{Combinaci\'on 1} - 1.4D
    \item \textbf{Combinaci\'on 2} - 1.2D + 1.6L+ 0.5max(Lr ; S ; R)
    \item \textbf{Combinaci\'on 3} - 1.2D + 1.6max(Lr ; S ; R)+ max(L ; 0.5W)
    \item \textbf{Combinaci\'on 4} - 1.2D + 1.0W + L + 0.5 max(Lr ; S ; R)
    \item \textbf{Combinaci\'on 5} - 1.2D + 1.0E + L + 0.2S
    \item \textbf{Combinaci\'on 6} - 0.9D + 1.0W
    \item \textbf{Combinaci\'on 7} - 0.9D + 1.0E
\end{enumerate}

En donde cada s\'imbolo significa:

\begin{enumerate}
    \item \textbf{D} - Carga permanente
    \item \textbf{E} - Carga de sismo
    \item \textbf{L} - Sobrecarga (carga viva)
    \item \textbf{Lr} - Sobrecarga cubierta (carga viva)
    \item \textbf{S} - Carga de granizo
    \item \textbf{W} - Carga de viento
\end{enumerate}

Las cargas para el proyecto se presentan en la siguiente tabla:

\begin{table}[h]
    \centering
    \resizebox{\textwidth}{!}{
    \begin{tabular}{|c|c|c|c|c|}
        \hline
        \textbf{Carga Muerta} & \textbf{Sobrecarga Cubierta} & \textbf{Barlovento} & \textbf{Sotavento} & \textbf{Granizo} \\
        \hline
        {{ CARGA_MUERTA }} & {{ SOBRECARGA_CUBIERTA }} & {{ BARLOVENTO }} & {{ SOTAVENTO }} & {{ CARGA_DE_GRANIZO }}\\
        \hline
    \end{tabular}
    }
\end{table}

Las cargas sísmcas se calcular\'an con ayuda del programa ETABS.
El proyecto por sus carater\'isticas arquitect\'onicas no cuenta con cargas vivas.
"""

template = Template(latex_template)

# Rellena la plantilla con el valor de la variable
latex_output = template.render(  )

# Abre el archivo en modo de escritura, pero con la opción de añadir
file_path = r"memoria\memoria_de_cálculo_cojitambo.tex"
with open(file_path, "a") as f:
    f.write(latex_output)

print("Archivo LaTeX generado exitosamente:", file_path)
print("Recuerda revisar que '/end{document}' se encuentre al final del archivo")
print("También que los caracteres latinos y tildes")