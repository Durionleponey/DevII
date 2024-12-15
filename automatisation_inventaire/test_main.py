import unittest
import os
import io
import sys
from main import CSVReader, merge_all_csv_in_directory, generate_summary_report


class TestCsvProgram(unittest.TestCase):
    """
    Tests améliorés pour vérifier les fonctionnalités principales,
    incluant des cas limites et des erreurs.
    """

    def setUp(self):
        # Redirection de la sortie standard pour analyser les messages d'erreur
        self.held_stdout = sys.stdout
        sys.stdout = io.StringIO()

        self.test_file = "test_file.csv"
        self.output_file = "merged_test.csv"

        # Création d'un fichier CSV simple
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write("id,name,score\n1,John,50\n2,Jane,75\n")

    def tearDown(self):
        # Nettoyage des fichiers générés
        sys.stdout = self.held_stdout
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        if os.path.exists("summary_report.txt"):
            os.remove("summary_report.txt")
        if os.path.exists("test_dir"):
            # Nettoyage du répertoire de test
            for f in os.listdir("test_dir"):
                os.remove(os.path.join("test_dir", f))
            os.rmdir("test_dir")

    def test_csv_reader(self):
        """
        Vérifie que le fichier CSV est lu correctement.
        """
        reader = CSVReader(self.test_file)
        reader.read_csv()
        data = reader.get_data()

        self.assertEqual(len(data), 3)  # En-tête + 2 lignes
        self.assertEqual(data[1], ["1", "John", "50"])

    def test_merge_csv(self):
        """
        Vérifie la fusion de fichiers CSV simples.
        """
        os.makedirs("test_dir", exist_ok=True)

        # Création d'un deuxième fichier CSV
        with open("test_dir/file1.csv", 'w', encoding='utf-8') as file:
            file.write("id,name,score\n3,Jack,60\n")

        merge_all_csv_in_directory("test_dir", self.output_file)

        self.assertTrue(os.path.exists(self.output_file))
        with open(self.output_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # En-tête + 1 ligne fusionnée
        self.assertEqual(len(lines), 2)
        self.assertIn("Jack", lines[1])

    def test_merge_non_existent_dir(self):
        """
        Test de la fusion sur un répertoire inexistant.
        Doit afficher un message d'erreur et ne pas créer de fichier.
        """
        merge_all_csv_in_directory("non_existent_dir", self.output_file)
        self.assertFalse(os.path.exists(self.output_file))
        output = sys.stdout.getvalue()
        self.assertIn("n'existe pas ou n'est pas un répertoire", output)

    def test_generate_report(self):
        """
        Vérifie que le rapport est généré avec les bonnes statistiques.
        """
        reader = CSVReader(self.test_file)
        reader.read_csv()
        data = reader.get_data()

        generate_summary_report(data)

        self.assertTrue(os.path.exists("summary_report.txt"))
        with open("summary_report.txt", 'r', encoding='utf-8') as file:
            content = file.read()

        self.assertIn("Somme", content)
        self.assertIn("Moyenne", content)

    def test_generate_report_no_numeric(self):
        """
        Test du rapport sur un CSV sans colonnes numériques.
        Le fichier ne doit pas générer d'erreur et le rapport sera vide ou minimal.
        """
        no_num_file = "no_num.csv"
        # On met des valeurs non numériques (ex: 'John', 'Jane' plutôt que '1', '2')
        with open(no_num_file, 'w', encoding='utf-8') as file:
            file.write("id,name\nJohn,Smith\nJane,Doe\n")

        reader = CSVReader(no_num_file)
        reader.read_csv()
        data = reader.get_data()

        generate_summary_report(data)
        self.assertTrue(os.path.exists("summary_report.txt"))

        with open("summary_report.txt", 'r', encoding='utf-8') as f:
            content = f.read()
        # Ici, on s'attend à aucune statistique, donc pas de mention de "Moyenne"
        self.assertNotIn("Moyenne", content)

        os.remove(no_num_file)

    def test_reader_missing_file(self):
        """
        Test de la lecture d'un fichier manquant.
        """
        missing_file = "missing.csv"
        reader = CSVReader(missing_file)
        reader.read_csv()
        output = sys.stdout.getvalue()
        self.assertIn("n'a pas été trouvé", output)


if __name__ == "__main__":
    unittest.main()
