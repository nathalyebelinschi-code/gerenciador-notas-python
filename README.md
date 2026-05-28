# 📊 Sistema de Gerenciamento de Notas Acadêmicas (Com Testes Unitários)

Este projeto consiste em uma solução de software desenvolvida em Python para automatizar o registro, processamento e acompanhamento de desempenho acadêmico. A aplicação foi projetada sob os padrões de arquitetura de software limpa, adotando o **Princípio da Responsabilidade Única (SRP)** e as diretrizes de estilo da **PEP 8**.

O grande diferencial deste projeto é a implementação de uma suíte de **Testes Unitários automatizados**, garantindo a resiliência do motor de cálculo contra falhas e comportamentos inesperados.

---

## 🛠️ Tecnologias e Engenharia Aplicada

* **Linguagem:** Python 3.14
* **Modelagem de Dados:** Lista de dicionários compostos (`list` e `dict`) para simular o armazenamento estruturado em memória.
* **Garantia de Qualidade (QA):** Uso do módulo nativo `unittest` para validação de fluxos normais e blindagem de casos extremos.
* **Tratamento de Edge Cases:** Proteção algorítmica contra o erro crítico de divisão por zero (`ZeroDivisionError`) ao processar arrays de notas vazios.

---

## ⚙️ Demonstração de Execução & Testes

### 🔹 1. Relatório Acadêmico Gerado
<img width="1641" height="1026" alt="print1nota" src="https://github.com/user-attachments/assets/7f523dc5-d06e-4b3d-bf03-f45b8a55b379" />


### 🔹 2. Suíte de Testes Aprovada (OK)
<img width="1631" height="1027" alt="print2notas" src="https://github.com/user-attachments/assets/05276704-03c0-4409-af7a-e7417f393fe5" />


---

## 🚀 Como Executar

1. Clone o repositório ou baixe os arquivos `.py`.
2. Para rodar o sistema principal e visualizar o relatório:
   ```bash
   python gerenciador_notas.py
