[![Keep Alive Streamlit](https://github.com/cursinhoeachusp/rastreador_aprovados/actions/workflows/main.yml/badge.svg)](https://github.com/cursinhoeachusp/rastreador_aprovados/actions/workflows/main.yml)

<div align="center">

# Rastreador de Aprovados | CPE

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

<p align="center">
  Automatização do cruzamento de dados entre alunos do Cursinho Popular EACH e listas oficiais de vestibulares (FUVEST, SISU, UNESP).
</p>

</div>

## Problema identificado
A conferência de aprovados costumava ser feita de forma manual, exigindo que a equipe analisasse listas em PDF com milhares de nomes. Além de lento e sujeito a erros humanos, cruzar listas desestruturadas (como PDFs de vestibulares) com planilhas de alunos era um desafio técnico complexo.

## Solução proposta
O rastreador evoluiu de um simples script para uma aplicação web completa. Para resolver o problema dos PDFs (que não possuem tabelas perfeitas), o nosso algoritmo extrai todo o conteúdo do arquivo e o transforma em um bloco de texto contínuo. 

Ele busca o nome do aluno nesse texto e, ao encontrá-lo, cria uma **janela de contexto** (analisando os caracteres ao redor do nome) para procurar fragmentos do **CPF** do aluno. Isso atesta a aprovação com segurança e elimina o risco de falsos positivos com homônimos.

### Principais funcionalidades
- **Interface web:** Interação amigável construída com Streamlit. Basta arrastar os arquivos na tela.
- **Leitura de dados Desestruturados:** Suporte direto a arquivos `.pdf` e `.txt`, além das planilhas `.csv` e `.xlsx`.
- **Validação dupla (Nome + CPF):** Cruzamento inteligente que usa a proximidade do documento no texto para validar nomes exatos ou até mesmo nomes cortados pela formatação do vestibular.
- **Rapidez:** Processa blocos gigantescos de texto e milhares de nomes em segundos.

## Tecnologias utilizadas
* **Python 3:** Linguagem base do back-end.
* **Streamlit:** Framework para a criação da interface web interativa.
* **Pdfplumber & PyPDF:** Bibliotecas responsáveis pela extração e leitura pesada dos arquivos PDF.
* **Pandas:** Manipulação, estruturação das tabelas de dados e geração de relatórios.
* **RapidFuzz:** Algoritmos de correspondência de textos (fuzzy matching) para buscas em planilhas.
* **Unidecode & RegEx:** Normalização de texto e limpeza de caracteres especiais.

## Como executar

Para rodar a aplicação localmente, siga os passos:

1. **Clone o repositório:**
```bash
git clone [https://github.com/cursinhoeachusp/rastreador_aprovados.git](https://github.com/cursinhoeachusp/rastreador_aprovados.git)
cd rastreador_aprovados
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Inicie a aplicação:**
```bash
streamlit run app.py
```

4. **No navegador:**
O sistema abrirá automaticamente. Faça o upload da planilha de alunos, depois do PDF oficial, selecione o método de validação (nome + CPF) e clique em "Buscar".

## Exemplo de resultado
O sistema gera um painel interativo com os resultados classificados, pronto para a conferência da diretoria:
| Aluno CPE | Nome detectado | Similaridade | Status | Observação |
| :---: | :---: | :---: | :---: | :---: |
| Carlos Souza | CARLOS SOUZA | 100% | ✅ Aprovado | Nome completo e CPF (.456.) conferem. |
| Ana V. Silva | ANA V. SILVA | Parcial + CPF | ✅ Aprovado (Nome cortado) | Nome longo identificado + CPF confirmado. |
| João Pedro | JOÃO PEDRO | 100% | ⚠️ Verificar | Nome encontrado, mas CPF não bateu no contexto. |

<br>

<div align='center'><b>Desenvolvido com 🧡💙 por Inovatec</b></div>
