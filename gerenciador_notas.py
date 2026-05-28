# ==============================================================================
# Script: gerenciador_notas.py
# Propósito: Motor lógico e geração de relatórios acadêmicos
# ==============================================================================

def calcular_media(notas):
    """
    Calcula a média aritmética simples a partir de uma lista de avaliações.
    Trata o caso extremo de lista vazia para evitar ZeroDivisionError.
    """
    if not notas:
        return 0.0
    return float(sum(notas) / len(notas))


def verificar_aprovacao(media, media_minima=7.0):
    """
    Valida o status de aprovação com base na nota de corte institucional.
    """
    if media >= media_minima:
        return 'Aprovado'
    else:
        return 'Reprovado'


def gerar_relatorio(alunos):
    """
    Itera sobre a lista de dicionários dos alunos, calcula as médias,
    verifica os status de aprovação e exibe uma tabela formatada no terminal.
    """
    print("\n" + "="*55)
    print(f"{'RELATÓRIO DE DESEMPENHO ACADÊMICO':^55}")
    print("="*55)
    print(f"{'Estudante':<25} | {'Média':<10} | {'Situação':<12}")
    print("-"*55)
    
    for estudante in alunos:
        nome_aluno = estudante["nome"]
        lista_notas = estudante["notas"]
        
        media_final = calcular_media(lista_notas)
        status_final = verificar_aprovacao(media_final)
        
        print(f"{nome_aluno:<25} | {media_final:<10.2f} | {status_final:<12}")
        
    print("="*55 + "\n")


# Este bloco garante que o relatório só rode se executarmos ESTE arquivo direto
if __name__ == '__main__':
    cadastro_estudantes = [
        {"nome": "Ana Silva", "notas": [8.5, 7.0, 9.0]},
        {"nome": "Carlos Oliveira", "notas": [5.5, 6.0, 4.5]},
        {"nome": "Mariana Santos", "notas": [9.5, 10.0, 9.0]}
    ]
    
    gerar_relatorio(cadastro_estudantes)