from cargas import CargasNEC15
from jinja2 import Template

# Calculo de cargas permanentes en el proyecto
# Las unidades que se manejarán son kN_m

# Carga fibrocemento
FIBROCEMENTO = 0.16  # KN/m2

# Carga acero en frio
ACERO_EN_FRIO = 0.08  # kN/m2

# Carga acero en caliente
ACERO_EN_CALIENTE = 0.06  # kN/m (Para manejar una sola unidad en cargas se usará kN/m2)
ACERO_EN_CALIENTE = 1.2 #kN/m2

# Instalaciones hidraulicas y eléctricas
INSTALACIONES_HI_ELEC = 1  # kN/m2

# Cielo Raso
CIELO_RASO = 0.5  # kN/m2

CARGA_MUERTA = FIBROCEMENTO + ACERO_EN_FRIO + ACERO_EN_CALIENTE + INSTALACIONES_HI_ELEC + CIELO_RASO


# Crear una instancia de la clase CargasNEC15
cargas = CargasNEC15()

# Llamar al método cargas_permanente
#cargas_permanentes = cargas.cargas_permanente()

latex_template = """
\subsection{Cargas Permanentes}
Las cargas permanentes consideradas para el proyecto son:
\begin{enumerate}
    \item Fibrocemento = {{FIBROCEMENTO}} KN/m
    \item Acero en frío = {{ACERO_EN_FRIO}} KN/m
    \item Acero en caliente = {{ACERO_EN_CALIENTE}} KN/m
    \item Instalaciones = {{INSTALACIONES_HI_ELEC}} KN/m
    \item Cielo Raso = {{CIELO_RASO}} KN/m

\end{enumerate}
"""

template = Template(latex_template)#

# Rellena la plantilla con el valor de la variable
latex_output = template.render(FIBROCEMENTO = FIBROCEMENTO, 
                               ACERO_EN_FRIO = ACERO_EN_FRIO,
                               ACERO_EN_CALIENTE = ACERO_EN_CALIENTE,
                               INSTALACIONES_HI_ELEC = INSTALACIONES_HI_ELEC,
                               CIELO_RASO = CIELO_RASO
                               )

# Abre el archivo en modo de escritura, pero con la opción de añadir
file_path = r"memoria\memoria_de_cálculo_cojitambo.tex"
with open(file_path, "a") as f:
    f.write(latex_output)

print("Archivo LaTeX generado exitosamente:", file_path)


