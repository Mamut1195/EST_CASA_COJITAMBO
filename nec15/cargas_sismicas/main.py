from espectro import EspectroNEC
#Datos para obtencion del espectro en la ubicacion del proyecto
n=2.48
Fa=1.5
Fd=1.75
Fs=1.6
Z=0.25
r=1.5
ZONA_SISMICA = 0.25
PERFIL_DEL_SUELO = 'E'

# Crear una instancia de la clase EspectroNEC
espectro_nec = EspectroNEC(n=n, Fa=Fa, Fd=Fd, Fs=Fs, Z=Z, r=r)

# Calcular el espectro sísmico elástico de aceleraciones y graficarlo
espectro_nec.graficar_espectro()

# Guardar los puntos del espectro en un archivo de texto
espectro_nec.extraccion_de_puntos(ruta_de_archivo=r'nec15/cargas_sismicas', nombre_archivo='puntos_espectro_nec.txt')

from jinja2 import Template

SOBRECARGA_CUBIERTA = 0.70 #KN/m2

latex_template = r"""
\subsection{Espectro s\'ismico}
El espectro s\'ismoco se construye a partir de los datos de la geolog\'ia local determinados por el estudios de suelos.
De esta manera los pa\'arametros que permiten la construcci\'on del espectro de acuerdo a la NEC son:

\begin{enumerate}
    \item[\textbullet] \textbf{Fa} - Coeficiente de amplificaci\'on de suelo en la zona de periodo corto.
    \item[\textbullet] \textbf{Fd} - Desplazmiento para dise\~no en roca.
    \item[\textbullet] \textbf{Z} - Factor de zona s\'simica.
    \item[\textbullet] \textbf{n} - Raz\'on entre la aceleraci\'on espectral Sa (T = 0.1 s) y el PGA para el periodo de retorno seleccionado.
    \item[\textbullet] \textbf{r} - Factor usado en el espectro de dise\~no el\'astico, cuyos valores dependen de la ubicaci\'on geogr\'afica del proyecto.
\end{enumerate}

Los valores de los par\'ametros se muestran en la siguiente tabla:

\begin{table}[h]
    \centering
    \resizebox{\textwidth}{!}{
    \begin{tabular}{|c|c|c|c|c|c|c|c|}
        \hline
        \textbf{ZONA SISMICA} & \textbf{Perfil suelo} & \textbf{Fa} & \textbf{Fd} & \textbf{Fs} & \textbf{Z} & \textbf{r} & \textbf{n}\\
        \hline
        {{ ZONA_SISMICA }} & {{ PERFIL_DEL_SUELO }} & {{ Fa }} & {{ Fd }} & {{ Fs }} & {{ Z }} & {{ r }} & {{ n }}\\
        \hline
    \end{tabular}
    }
\end{table}

Con los valores presentados en la tabla se grafica el espectro.

\begin{figure}[h]
    \centering
    \includegraphics[width=0.5\textwidth]{imagenes/espectro.png}
\end{figure}
"""

template = Template(latex_template)

# Rellena la plantilla con el valor de la variable
latex_output = template.render(ZONA_SISMICA = ZONA_SISMICA,
                               PERFIL_DEL_SUELO = PERFIL_DEL_SUELO,
                               Fa = Fa,
                               Fd = Fd,
                               Fs =Fs,
                               Z = Z,
                               r = r,
                               n = n
                                    )

# Abre el archivo en modo de escritura, pero con la opción de añadir
file_path = r"memoria\memoria_de_cálculo_cojitambo.tex"
with open(file_path, "a") as f:
    f.write(latex_output)

print("Archivo LaTeX generado exitosamente:", file_path)
print("Recuerda revisar que '/end{document}' se encuentre al final del archivo")
print("También que los caracteres latinos y tildes")