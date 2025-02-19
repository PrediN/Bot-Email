from duckduckgo_search import DDGS
import json

def filtrar_resultados(resultados, palavras_chave):
    """Filtra os resultados com base nas palavras-chave."""
    resultados_filtrados = []
    for resultado in resultados:
        if any(palavra.lower() in resultado['title'].lower() for palavra in palavras_chave):
            resultados_filtrados.append(resultado)
    return resultados_filtrados

def search_duckduckgo(termo_busca, palavras_chave):
    """
    Busca no DuckDuckGo e retorna os resultados em formato JSON.
    """
    try:
        # Realizar a busca
        resultados = DDGS().text(termo_busca, region='wt-wt', safesearch='Moderate', timelimit='w', max_results=10)

        # Filtrar os resultados
        resultados_filtrados = filtrar_resultados(resultados, palavras_chave)

        # Converter para JSON
        with open('resultados_busca.json', 'w') as file:
            json.dump(resultados_filtrados, file, indent=4)


    except Exception as e:
        print(f"Erro na busca: {e}")
        return None

# Exemplo de uso
if __name__ == '__main__':
    termo_busca = "Inteligência artificial avanços"
    palavras_chave = ["inteligência artificial", "machine learning", "deep learning"]
    resultados_json = search_duckduckgo(termo_busca, palavras_chave)

    if resultados_json:
        # Salvar os resultados em um arquivo JSON
        with open('resultados_busca.json', 'w', encoding='utf-8') as arquivo_json:
            arquivo_json.write(resultados_json)  # Salva a string JSON diretamente

        print("Resultados da busca salvos em 'resultados_busca.json'")