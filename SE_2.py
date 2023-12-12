import json

def cargar_base_de_datos(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def buscar(respuesta, solucion):
    if respuesta == "s":
        if pregunta["razones"]["fuente_de_alimentacion"]:
            diagnostico_final["soluciones"][0]["finales"]["fuente_de_alimentacion"] += 1
            
        if pregunta["razones"]["ram"]:
            diagnostico_final["soluciones"][0]["finales"]["ram"] += 1
            
        if pregunta["razones"]["disco_duro"]:
            diagnostico_final["soluciones"][0]["finales"]["disco_duro"] += 1
            
        if pregunta["razones"]["ventiladores_sistema_de_enfriamiento"]:
            diagnostico_final["soluciones"][0]["finales"]["ventiladores_sistema_de_enfriamiento"] += 1
            
        if pregunta["razones"]["sistema_operativo"]:
            diagnostico_final["soluciones"][0]["finales"]["sistema_operativo"] += 1
            
        if pregunta["razones"]["rendimiento"]:
            diagnostico_final["soluciones"][0]["finales"]["rendimiento"] += 1
            
        if pregunta["razones"]["malware_virus"]:
            diagnostico_final["soluciones"][0]["finales"]["malware_virus"] += 1
            
        if pregunta["razones"]["temperatura"]:
            diagnostico_final["soluciones"][0]["finales"]["temperatura"] += 1
            
        if pregunta["razones"]["controladores"]:
            diagnostico_final["soluciones"][0]["finales"]["controladores"] += 1
            
        if pregunta["razones"]["hardware_general"]:
            diagnostico_final["soluciones"][0]["finales"]["hardware_general"] += 1
            
        if pregunta["razones"]["limpieza_de_componentes"]:
            diagnostico_final["soluciones"][0]["finales"]["limpieza_de_componentes"] += 1
            
        if pregunta["razones"]["investigar"]:
            diagnostico_final["soluciones"][0]["finales"]["investigar"] += 1
            
    else:
        return

preguntas: dict = cargar_base_de_datos('SE_preguntas_2.json')
diagnostico_final: dict = cargar_base_de_datos('SE_datos_2.json')
diagnosticos: dict = cargar_base_de_datos('SE_diagnosticos.json')

num_preguntas = len(preguntas["preguntas"])

print("Diagnostico tecnico")
for i in range(0, num_preguntas):
    pregunta = preguntas["preguntas"][i]
    respuesta = input(f"{pregunta['pregunta']} (s/n): ")
    buscar(respuesta, pregunta)

    if i == num_preguntas-1:
        max_valor = max(diagnostico_final["soluciones"][0]["finales"].values())
        claves_maximas = [clave for clave, valor in diagnostico_final["soluciones"][0]["finales"].items() if valor == max_valor]
        empatados = len(claves_maximas)
        print("\n\n-------DIAGNOSTICO-------\n")
        
        if max_valor == 0:
            print("No parece que su computadora/laptop tenga algun problema, aun asi, si considera algo anormal busque asistencia tecnica capacitada")
        else:
            for y in range(0,empatados):
                print(diagnosticos["diagnosticos"][claves_maximas[y]])