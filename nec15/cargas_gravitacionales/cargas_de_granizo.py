from jinja2 import Template

#Calculo de la carga de granizo

PESO_ESP_GRANIZO = 1000 #kg/m3

ALTURA_DE_ACUMULACION = 0.02 #m

#Carga de granizo

CARGA_DE_GRANIZO = PESO_ESP_GRANIZO * ALTURA_DE_ACUMULACION #kg/m2

CARGA_DE_GRANIZO = CARGA_DE_GRANIZO/10 #KN/m2

latex_template = r"""
\subsection{Cargas de granizo}
Seg\'un la NEC se debe considerar una acumulaci\'on de granizo en un corto periodo de tiempo.
Para cubiertas con pendientes menores de 15\% se debe considerar una carga m\'inima de 0.50 $kN/m^2$; 
para cubiertas con pendientes menores del 5\% se debe considerar 1.0 kN/m2. Se determinan de la siguiente forma:

$$S = \rho H_s$$

Donde:

$\rho $: Peso espec\'ifico del granizo (en defecto: 1000 $Kg/m^3$)

$H_s$: Altura de acumulaci\'on ($m$)

La f\'ormula mencionada nos da una carga de granizo igual a {{ CARGA_DE_GRANIZO }}

"""

template = Template(latex_template)

# Rellena la plantilla con el valor de la variable
latex_output = template.render(CARGA_DE_GRANIZO = CARGA_DE_GRANIZO)

# Abre el archivo en modo de escritura, pero con la opción de añadir
file_path = r"memoria\memoria_de_cálculo_cojitambo.tex"
with open(file_path, "a") as f:
    f.write(latex_output)

print("Archivo LaTeX generado exitosamente:", file_path)
print("Recuerda revisar que '/end{document}' se encuentre al final del archivo")
print("También que los caracteres latinos y tildes")