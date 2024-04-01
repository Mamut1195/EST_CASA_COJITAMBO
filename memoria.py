from jinja2 import Template

# Define la plantilla LaTeX
latex_template = r"""
\documentclass{article}
\usepackage[utf8]{inputenc} % Paquete para manejar la codificación UTF-8
\usepackage[spanish]{babel} % Paquete para manejar el idioma español
\begin{document}
Hola {{ nombre }} ¿Cómo estás?
\end{document}
"""

# Crea un objeto Template de Jinja2 con la plantilla LaTeX
template = Template(latex_template)

# Define el valor de la variable nombre
nombre = "Juan"

# Rellena la plantilla con el valor de la variable
latex_output = template.render(nombre=nombre)

# Guarda el contenido en un archivo
file_path = "archivo_latex.tex"
with open(file_path, "w") as f:
    f.write(latex_output)

print("Archivo LaTeX generado exitosamente:", file_path)
