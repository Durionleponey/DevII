import unittest
import os
from main import CSVReader, merge_all_csv_in_directory, generate_summary_report

class TestCsvProgram(unittest.TestCase):
    """
    Tests simplifiés pour vérifier les fonctionnalités principales.
    """

    def setUp(self):
        """
        Prépare l'environnement de test avec un fichier CSV simple.
        """
        self.test_file = "test_file.csv"
        self.output_file = "merged_test.csv"

        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write("id,name,score\n1,John,50\n2,Jane,75\n")



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

        with open("test_dir/file1.csv", 'w', encoding='utf-8') as file:
            file.write("id,name,score\n3,Jack,60\n")

        merge_all_csv_in_directory("test_dir", self.output_file)

        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 3)  # En-tête + 2 lignes (1 de test_file, 1 fusionnée)

        os.remove("test_dir/file1.csv")
        os.rmdir("test_dir")

    def test_generate_report(self):
        """
        Vérifie que le rapport est généré avec les bonnes statistiques.
        """
        reader = CSVReader(self.test_file)
        reader.read_csv()
        data = reader.get_data()

        generate_summary_report(data)

        with open("summary_report.txt", 'r', encoding='utf-8') as file:
            content = file.read()

        self.assertIn("Somme", content)
        self.assertIn("Moyenne", content)
        os.remove("summary_report.txt")

if __name__ == "__main__":
    unittest.main()
