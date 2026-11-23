# Monitoreo Hídrico – Reservorio Tinajones

Aplicación de escritorio (Python + PyQt5 + MySQL) bajo arquitectura MVC.
Entidad: **EstacionHidrica** (compuerta, porcentaje_llenado, caudal_m). El `mensaje_alerta` se evalúa en Python y no se guarda en la BD.

| % llenado | Mensaje |
|---|---|
| < 30 | ALERTA: SEQUIA / RESTRICCION |
| 30 – 85 | NIVEL OPERATIVO NORMAL |
| > 85 | ALERTA: RIESGO DE DESBORDE |

## Estructura
```
database/   conexion.py + tinajones_db.sql
models/     estacion_model.py
controllers/estacion_controller.py
views/      main_window.py, registro_dialog.py
main.py
```

## Ejecución
1. Ejecutar `database/tinajones_db.sql` en MySQL Workbench.
2. Ajustar la contraseña en `database/conexion.py`.
3. ```
   python -m venv venv
   venv\Scripts\activate        # Windows  (Linux/Mac: source venv/bin/activate)
   pip install -r requirements.txt
   python main.py
   ```

## Integrantes
- Apellidos y Nombres
