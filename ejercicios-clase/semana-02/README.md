# Semana 02 - Entorno de trabajo

El entorno virtual se creó como `venv` en la raíz del repositorio con Python 3.12.
En PowerShell se activó con `Set-ExecutionPolicy -Scope Process Bypass` y `.\venv\Scripts\Activate.ps1`.
Antes de instalar dependencias, se comprobó que Python y pip pertenecían al entorno y que `pip list` solo mostraba pip.
Matplotlib se instaló dentro del entorno con `python -m pip install matplotlib`.
El archivo `requirements.txt` se generó en la raíz mediante `pip freeze`.
Otra persona puede crear su entorno con `python -m venv venv` y activarlo desde la raíz.
Después puede instalar las mismas versiones con `python -m pip install -r requirements.txt`.
