from jinja2 import Template

from carga_permanente import CARGA_MUERTA
from cargas_de_granizo import CARGA_DE_GRANIZO
from cargas_por_viento import BARLOVENTO, SOTAVENTO
from sobrecarga_cubierta import SOBRECARGA_CUBIERTA



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
    \item[\textbullet] \textbf{D} - Carga permanente
    \item[\textbullet] \textbf{E} - Carga de sismo
    \item[\textbullet] \textbf{L} - Sobrecarga (carga viva)
    \item[\textbullet] \textbf{Lr} - Sobrecarga cubierta (carga viva)
    \item[\textbullet] \textbf{S} - Carga de granizo
    \item[\textbullet] \textbf{W} - Carga de viento
\end{enumerate}

Las cargas para el proyecto se presentan en la siguiente tabla:

\begin{table}[h]
    \centering
    \begin{tabular}{|c|c|c|c|c|}
        \hline
        \textbf{Carga Muerta} & \textbf{Sobrecarga Cubierta} & \textbf{Barlovento} & \textbf{Sotavento} & \textbf{Granizo} \\
        \hline
        {{ CARGA_MUERTA_1 }} & {{ SOBRECARGA_CUBIERTA_1 }} & {{ BARLOVENTO_1 }} & {{ SOTAVENTO_1 }} & {{ CARGA_DE_GRANIZO_1 }}\\
        \hline
    \end{tabular}
\end{table}

Las cargas s\'ismcas se calcular\'an con ayuda del programa ETABS.
El proyecto por sus carater\'isticas arquitect\'onicas no cuenta con cargas vivas.
"""

template = Template(latex_template)

# Rellena la plantilla con el valor de la variable
latex_output = template.render(CARGA_MUERTA_1 = CARGA_MUERTA,
                               SOBRECARGA_CUBIERTA_1 = SOBRECARGA_CUBIERTA,
                               BARLOVENTO_1 = BARLOVENTO,
                               SOTAVENTO_1 = SOTAVENTO,
                               CARGA_DE_GRANIZO_1 = CARGA_DE_GRANIZO )

# Abre el archivo en modo de escritura, pero con la opción de añadir
file_path = r"memoria\memoria_de_cálculo_cojitambo.tex"
with open(file_path, "a") as f:
    f.write(latex_output)

print("Archivo LaTeX generado exitosamente:", file_path)
print("Recuerda revisar que '/end{document}' se encuentre al final del archivo")
print("También que los caracteres latinos y tildes")