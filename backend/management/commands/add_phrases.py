import os
from django.core.management.base import BaseCommand
from core.models import Phrases  # Ajuste conforme o app onde está o modelo Frase

class Command(BaseCommand):
    help = "Adiciona frases à base de dados a partir de um ficheiro de texto"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Caminho para o ficheiro contendo as frases")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        # Caminho absoluto ao ficheiro, partindo do diretório principal
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        absolute_path = os.path.join(base_dir, file_path)

        if not os.path.exists(absolute_path):
            self.stderr.write(self.style.ERROR(f"Ficheiro não encontrado: {absolute_path}"))
            return

        with open(absolute_path, 'r', encoding='utf-8') as file:
            frases = file.readlines()

        adicionadas = 0
        ignoradas = 0

        for frase in frases:
            frase = frase.strip()
            if not frase:
                continue

            try:
                Phrases.objects.create(conteudo=frase)
                adicionadas += 1
            except Exception:
                ignoradas += 1

        self.stdout.write(self.style.SUCCESS(
            f"{adicionadas} frases adicionadas com sucesso! {ignoradas} frases ignoradas."
        ))
