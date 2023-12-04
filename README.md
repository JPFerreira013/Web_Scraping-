# Web_Scraping-
# Web Scraping de Proventos - BBSE3

Este projeto realiza web scraping na página de proventos da empresa BBSE3 no site [Fundamentus](https://www.fundamentus.com.br/proventos.php?papel=BBSE3&tipo=2), coletando dados estruturados sobre dividendos. O web scraping é feito em Python, utilizando as bibliotecas `requests`, `pandas`, `beautifulsoup4`, e `matplotlib`.

## Instalação

Antes de executar o código, certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalá-las executando o seguinte comando no terminal:

```bash
pip install requests pandas beautifulsoup4

Executando o Código
O script web_scraping_bbse3.py realiza as seguintes etapas:

Faz uma requisição para a URL da página de proventos da BBSE3.
Utiliza o BeautifulSoup para analisar o conteúdo HTML e extrair a tabela de proventos.
Refatora os dados, convertendo formatos de data e valores.
Gera gráficos de proventos por ação e proventos anuais.
Exporta os dados para um arquivo CSV.
