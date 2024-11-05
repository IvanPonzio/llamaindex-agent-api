from fastapi import FastAPI, HTTPException
from llama_index.llms.gemini import Gemini
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os
import uvicorn

app = FastAPI()

# Configuración de LlamaIndex y Gemini
llm = Gemini(model="models/gemini-pro", api_key="AIzaSyCpcPwrzy-LnIdtRSbweol2y_ibZvA_Su0")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Asignación de los modelos a las configuraciones de LlamaIndex
Settings.llm_model = llm
Settings.embed_model = embed_model

# Carga e indexación de documentos en el directorio data/
data_directory = "./app/data"
documents = SimpleDirectoryReader(data_directory).load_data()  # Cargar documentos .txt desde el directorio
index = VectorStoreIndex.from_documents(documents)  # Crear índice a partir de los documentos
query_engine = index.as_query_engine(streaming=True, llm=llm)  # Crear motor de consulta utilizando el LLM

# Crear herramienta de motor de consulta para el agente
query_engine_tools = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(
        name="PDF",
        description="Responde preguntas específicas sobre los personajes de la obra."
    ),
)
agent = ReActAgent.from_tools([query_engine_tools], llm=llm, verbose=True)

@app.get("/query")
async def query(q: str):
    try:
        # Usar stream_chat para obtener la respuesta
        stream_response = agent.stream_chat(message=q)
        stream_response.print_response_stream()  # Imprimir la respuesta

        return {"status": "success", "message": "Respuesta impresa en la consola."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el procesamiento de la consulta: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
