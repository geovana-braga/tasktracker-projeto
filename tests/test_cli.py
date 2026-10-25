import contextlib
import io
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src import main as tasktracker


class TaskTrackerCliTests(unittest.TestCase):
    def setUp(self):
        self.pasta_temporaria = tempfile.TemporaryDirectory()
        self.arquivo_dados = Path(self.pasta_temporaria.name) / "tarefas.json"
        self.ambiente = patch.dict(os.environ, {"TASKTRACKER_DATA_FILE": str(self.arquivo_dados)})
        self.ambiente.start()
        tasktracker.tarefas.clear()

    def tearDown(self):
        tasktracker.tarefas.clear()
        self.ambiente.stop()
        self.pasta_temporaria.cleanup()

    def executar(self, respostas):
        saida = io.StringIO()
        with patch("builtins.input", side_effect=respostas), contextlib.redirect_stdout(saida):
            tasktracker.main()
        return saida.getvalue()

    def test_cadastro_validacoes_e_listagem_na_mesma_execucao(self):
        saida = self.executar(
            [
                "1",
                "",  # título obrigatório
                "Estudar Docker",
                "Revisar o projeto",
                "Urgente",  # prioridade inválida
                "Media",
                "31/10/2026",
                "2",
                "3",
            ]
        )

        self.assertIn("O título é obrigatório", saida)
        self.assertIn("Prioridade inválida", saida)
        self.assertIn("Tarefa cadastrada com sucesso!", saida)
        self.assertIn("Título: Estudar Docker", saida)
        self.assertIn("Prioridade: Média", saida)
        self.assertIn("Status: Pendente", saida)
        self.assertEqual(len(tasktracker.tarefas), 1)
        self.assertTrue(self.arquivo_dados.exists())

    def test_tarefa_continua_apos_sair_e_abrir_novamente(self):
        self.executar(["1", "Tarefa persistente", "Revisar", "Alta", "31/10/2026", "3"])
        tasktracker.tarefas.clear()

        saida = self.executar(["2", "3"])
        self.assertIn("Título: Tarefa persistente", saida)
        self.assertIn("Status: Pendente", saida)

    def test_listagem_sem_tarefas(self):
        saida = self.executar(["2", "3"])
        self.assertIn("Nenhuma tarefa cadastrada no momento.", saida)
        self.assertEqual(tasktracker.tarefas, [])

    def test_opcao_invalida_retorna_ao_menu(self):
        saida = self.executar(["9", "3"])
        self.assertIn("Opção inválida. Digite 1, 2 ou 3.", saida)
        self.assertIn("Aplicação encerrada.", saida)


if __name__ == "__main__":
    unittest.main()
