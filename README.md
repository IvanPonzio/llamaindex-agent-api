<<<<<<< HEAD
# llamaindex-agent-api
=======
# LlamaIndex Agent API

Este proyecto es una API construida con FastAPI que utiliza LlamaIndex y el modelo Gemini para responder preguntas específicas sobre documentos. La API permite realizar consultas sobre los documentos indexados y devolver respuestas utilizando procesamiento de lenguaje natural.

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/IvanPonzio/llamaindex-agent-api.git
   cd llamaindex-agent-api
2. **Crear un entorno virtual (opcional pero recomendado): **
  ```bash
  python -m venv venv
  source venv/bin/activate  # En Linux o Mac
  venv\Scripts\activate  # En Windows
  ```

3. ** Instalar las dependencias: **
    ```bash
    pip install -r requirements.txt

Uso
1. Asegúrate de que los documentos que deseas consultar estén en el directorio ./app/data/.

2. Inicia la API:
   ```bash
   python3 -m app.main
   ```
3. Realiza una consulta utilizando el siguiente endpoint:
    ```bash
    GET /query?q={tu consulta}



>>>>>>> master
