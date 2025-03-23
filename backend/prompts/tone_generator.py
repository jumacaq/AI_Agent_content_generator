GENERATE_REFINED_INFO = """Tu tarea es **refinar y mejorar** un guion de **reel de Instagram o TikTok**, aplicando **pensamiento en cadena (Chain of Thought)** para ajustar el **tono, lenguaje y público objetivo** según los siguientes parámetros:  

🔹 **Entrada Original:**  
{previous_script}  

🔹 **Nuevo Público Objetivo:** {new_target_audience}  
🔹 **Nuevo Tono:** {new_tone}  
🔹 **Idioma:** {language}  

### **Proceso de Refinamiento**  
**Análisis del guion original**: Identifica qué partes funcionan bien y cuáles deben ajustarse.  
**Adaptación del tono y lenguaje**: Modifica expresiones y estructura para alinearlas con el nuevo público.  
**Optimización del mensaje**: Asegura claridad y coherencia con los parámetros dados.  
**Refuerzo del Call to Action (CTA)**: Ajusta la llamada a la acción para maximizar el impacto en la audiencia.  
** No incluir emojis en tu respuesta**
### **Salida esperada**  
Un guion optimizado y mejorado, alineado con el tono, idioma y público objetivo especificados. La respuesta debe seguir este formato:\n{format_instructions}\n"""
