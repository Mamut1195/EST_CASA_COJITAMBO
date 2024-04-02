from jinja2 import Template

SOBRECARGA_CUBIERTA = 0.70 #KN/m2

latex_template = r"""
\subsection{Cargas Variables}
Para el proyecto unicamente existen sobrecargas variables de cubierta. La NEC señala que
la carga de cubierta es de {{SOBRECARGA_CUBIERTA}}

"""

template = Template(latex_template)#

# Rellena la plantilla con el valor de la variable
latex_output = template.render(SOBRECARGA_CUBIERTA = SOBRECARGA_CUBIERTA)

# Abre el archivo en modo de escritura, pero con la opción de añadir
file_path = r"memoria\memoria_de_cálculo_cojitambo.tex"
with open(file_path, "a") as f:
    f.write(latex_output)

print("Archivo LaTeX generado exitosamente:", file_path)
print("Recuerda revisar que '/end{document}' se encuentre al final del archivo")
print("También que los caracteres latinos y tildes")