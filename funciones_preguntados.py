def separar_lista(lista : list, key : str ) -> list:
    """la funcion separa la lista principal en una sublista

    Args:
        lista (list): recibe la lista principal
        key (str): separa todas las preguntas que sean el value de esta key que recibe

    Returns:
        list: devuelve la lista separada
    """
    lista_separada = []

    for elemento in lista : 
        lista_separada.append(elemento[key])
    return(lista_separada)


