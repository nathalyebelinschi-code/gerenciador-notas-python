# ==============================================================================
# Script: test_notas.py
# Propósito: Suíte de testes unitários automatizados
# ==============================================================================

import unittest

# IMPORTAÇÃO CRUCIAL: Traz as funções do seu primeiro arquivo para serem testadas aqui
from gerenciador_notas import calcular_media, verificar_aprovacao

class TestGerenciamentoNotas(unittest.TestCase):
    """Classe de testes para validar o comportamento do gerenciador de notas."""

    def test_condicoes_normais_sucesso(self):
        """Valida o funcionamento padrão com notas normais (Aprovação/Reprovação)."""
        # Testando cenário de aprovação
        media_alta = calcular_media([8.0, 7.5, 9.0])
        self.assertEqual(verificar_aprovacao(media_alta), 'Aprovado')

        # Testando cenário de reprovação
        media_baixa = calcular_media([5.0, 4.5, 6.0])
        self.assertEqual(verificar_aprovacao(media_baixa), 'Reprovado')

    def test_caso_extremo_lista_vazia(self):
        """Valida se o sistema não quebra (Edge Case) ao receber lista sem notas."""
        media_vazia = calcular_media([])
        self.assertEqual(media_vazia, 0.0)
        self.assertEqual(verificar_aprovacao(media_vazia), 'Reprovado')

    def test_acionamento_limitador_corte_zero(self):
        """Valida a estabilidade se a nota de corte configurada for zero."""
        media_qualquer = calcular_media([2.0, 1.5, 3.0])
        status = verificar_aprovacao(media_qualquer, media_minima=0.0)
        self.assertEqual(status, 'Aprovado')

if __name__ == '__main__':
    unittest.main()