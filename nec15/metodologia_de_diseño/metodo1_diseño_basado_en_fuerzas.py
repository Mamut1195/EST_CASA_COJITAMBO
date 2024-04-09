from jinja2 import Template


latex_template = r"""
\chapter{Metodolog\'a de dise\~{n}o estructural - Dise\~{n}o basado en fuerzas}
La NEC establece que las estrucuturas deben dise\~{n}arse para resistir fuerzas s\'ismicas provenientes de las 
combinaciones de las fuerzas horizontales. Adem\'as que las fuerzas s\'ismicas de dise\~{n}o act\'uan de manera
no concurrente en la direcci\'on de cada eje principal de la estrucutura para luego ser combinadas de acuerdo a 
las siguientes combinaciones:
\begin{enumerate}
    \item \textbf{Combinaci\'on 1} $E_{h1} = max[(E_x + 0.3E_y), (E_y + 0.3E_x)]$
    \item \textbf{Combinaci\'on 2} $E_{h2} =\pm \sqrt{E_x^2 + E_y^2}$
\end{enumerate}

Donde:

\begin{enumerate}
    \item[\textbullet] $E_{h}$ Componente horizontal de la fuerza s\-ismica
    \item[\textbullet] $E_x$ Componente horizontal de la fuerza s\-ismica seg\'un el eje x
    \item[\textbullet] $E_y$ Componente horizontal de la fuerza s\-ismica seg\'un el eje y
\end{enumerate}

El dise\~{n}ador considerar\'a el siguiente valor de la componente s\-ismica horizontal: 
\begin{enumerate}
    \item \textbf{Combinaci\'on m\'as desfavorable} $E_h = max[E_{h1}, E_{h2}]$
\end{enumerate}
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