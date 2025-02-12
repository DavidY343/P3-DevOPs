import json

# Lista de casos de prueba basados en los requisitos
casos_de_prueba = [
    {"ID": "TP-01", "Requisito": "RF-01", "Descripción": "Verificar que el controlador recibe I_TRef e I_TReal cada 2s.", 
     "Entradas": ["I_TRef", "I_TReal"], "Salida Esperada": "Valores registrados cada 2s.", "Prioridad": "Alta"},
    
    {"ID": "TP-02", "Requisito": "RF-02", "Descripción": "Comprobar que el sistema activa la calefacción cuando I_TReal < I_TRef - 0.5°C.", 
     "Entradas": ["I_TRef=22", "I_TReal=21.4"], "Salida Esperada": "O_SC_ON = 1", "Prioridad": "Alta"},

    {"ID": "TP-03", "Requisito": "RF-03", "Descripción": "Comprobar que el sistema activa la refrigeración cuando I_TReal > I_TRef + 0.5°C.", 
     "Entradas": ["I_TRef=22", "I_TReal=22.6"], "Salida Esperada": "O_SR_ON = 1", "Prioridad": "Alta"},

    {"ID": "TP-04", "Requisito": "RF-04", "Descripción": "Verificar que el sistema chequea los errores de los subsistemas cada 2s.", 
     "Entradas": ["I_Error_SC", "I_Error_SR"], "Salida Esperada": "Registro de chequeo cada 2s.", "Prioridad": "Alta"},

    {"ID": "TP-05", "Requisito": "RF-05", "Descripción": "Comprobar que si un error persiste por más de 2s, el sistema intenta reiniciarse.", 
     "Entradas": ["Error persistente > 2s"], "Salida Esperada": "Intento de reinicio registrado.", "Prioridad": "Alta"},

    {"ID": "TP-06", "Requisito": "RF-06", "Descripción": "Verificar que el controlador cambia de estado entre Parado, Ejecución y Combate.", 
     "Entradas": ["Cambio de estado"], "Salida Esperada": "Transición correcta de estado.", "Prioridad": "Alta"},

    {"ID": "TP-07", "Requisito": "RF-07", "Descripción": "Verificar que en modo Parado se chequean errores cada 2s.", 
     "Entradas": ["Modo Parado activo"], "Salida Esperada": "Registro de chequeo en logs.", "Prioridad": "Media"},

    {"ID": "TP-08", "Requisito": "RF-08", "Descripción": "Comprobar que en modo Ejecución se mantiene I_TReal en ±0.5°C de I_TRef.", 
     "Entradas": ["I_TRef=22", "I_TReal variando"], "Salida Esperada": "I_TReal dentro del margen.", "Prioridad": "Alta"},

    {"ID": "TP-09", "Requisito": "RF-09", "Descripción": "Comprobar que en modo Combate se mantiene I_TReal en ±0.5°C de I_TRef durante el tiempo especificado.", 
     "Entradas": ["I_TRef=22", "Tiempo=10s"], "Salida Esperada": "I_TReal dentro del margen durante 10s.", "Prioridad": "Alta"},

    {"ID": "TP-10", "Requisito": "RF-10", "Descripción": "Verificar que ante un error interno se actualiza O_ERROR_SYS.", 
     "Entradas": ["Error interno detectado"], "Salida Esperada": "O_ERROR_SYS actualizado.", "Prioridad": "Alta"},

    {"ID": "TP-11", "Requisito": "RNF-01", "Descripción": "Medir la latencia del sistema para cambios en temperatura.", 
     "Entradas": ["Cambio de I_TReal"], "Salida Esperada": "Latencia ≤ 500ms.", "Prioridad": "Alta"},

    {"ID": "TP-12", "Requisito": "RNF-02", "Descripción": "Verificar que los eventos y estados se registran en logs.", 
     "Entradas": ["Evento de cambio de estado"], "Salida Esperada": "Registro en logs.", "Prioridad": "Media"},

    {"ID": "TP-13", "Requisito": "RNF-03", "Descripción": "Verificar que el sistema usa el protocolo de comunicación especificado.", 
     "Entradas": ["Conexión con subsistemas"], "Salida Esperada": "Protocolo estándar en uso.", "Prioridad": "Alta"}
]

# Guardar en un archivo JSON
json_filename = "casos_de_prueba.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(casos_de_prueba, json_file, indent=4, ensure_ascii=False)

# Devolver el archivo generado
json_filename
