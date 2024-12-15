import csv
import os
import argparse

class CSVReader:
    def __init__(self, file_path):
        """
        Initialise le chemin du fichier CSV et une variable pour stocker les données.
        """
        self.file_path = file_path
        self.data = []

    def read_csv(self):
        """
        Lit le fichier CSV et stocke les données dans une liste de listes.
        """
        try:
            with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.data = [row for row in reader]
        except FileNotFoundError:
            print(f"Erreur : Le fichier {self.file_path} n'a pas été trouvé.")
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier : {e}")

    def get_data(self):
        """
        Retourne les données sous forme de liste de listes.
        """
        return self.data

    def print_data(self):
        """
        Affiche les données ligne par ligne.
        """
        for row in self.data:
            print(row)


def merge_all_csv_in_directory(directory, output_file):
    """
    Lit tous les fichiers CSV dans un répertoire donné et fusionne leur contenu dans un seul fichier.
    """
    merged_data = []
    header_included = False

    if not os.path.isdir(directory):
        print(f"Erreur : Le répertoire {directory} n'existe pas ou n'est pas un répertoire.")
        return

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            print(f"Lecture du fichier : {filename}")
            reader = CSVReader(file_path)
            reader.read_csv()
            data = reader.get_data()

            if data:
                if not header_included:
                    merged_data.append(data[0])  # Ajouter l'en-tête une seule fois
                    header_included = True
                merged_data.extend(data[1:])  # Ajouter le reste des données

    # Écrire les données fusionnées dans le fichier de sortie
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(merged_data)
        print(f"Les fichiers CSV ont été fusionnés dans {output_file}")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier fusionné : {e}")


def generate_summary_report(data):
    """
    Génère un rapport récapitulatif des données CSV avec des statistiques utiles.
    """
    if not data:
        print("Aucune donnée disponible pour générer le rapport.")
        return

    headers = data[0]
    stats = {}

    # Calcul des statistiques pour chaque colonne numérique
    for i, header in enumerate(headers):
        column_values = [row[i] for row in data[1:] if i < len(row) and row[i].replace('.', '', 1).isdigit()]
        column_values = list(map(float, column_values))

        if column_values:
            stats[header] = {
                "somme": sum(column_values),
                "moyenne": sum(column_values) / len(column_values),
                "minimum": min(column_values),
                "maximum": max(column_values),
                "count": len(column_values),
                "écart-type": (sum((x - (sum(column_values) / len(column_values))) ** 2 for x in column_values) / len(column_values)) ** 0.5
            }

    # Afficher le rapport
    print("\n=== Rapport Récapitulatif ===")
    for header, stat in stats.items():
        print(f"Colonne : {header}")
        print(f"  Somme : {stat['somme']}")
        print(f"  Moyenne : {stat['moyenne']}")
        print(f"  Minimum : {stat['minimum']}")
        print(f"  Maximum : {stat['maximum']}")
        print(f"  Nombre d'entrées : {stat['count']}")
        print(f"  Écart-type : {stat['écart-type']}")
        print("----------------------")

    # Exporter le rapport dans un fichier texte
    try:
        with open("summary_report.txt", 'w', encoding='utf-8') as file:
            file.write("=== Rapport Récapitulatif ===\n")
            for header, stat in stats.items():
                file.write(f"Colonne : {header}\n")
                file.write(f"  Somme : {stat['somme']}\n")
                file.write(f"  Moyenne : {stat['moyenne']}\n")
                file.write(f"  Minimum : {stat['minimum']}\n")
                file.write(f"  Maximum : {stat['maximum']}\n")
                file.write(f"  Nombre d'entrées : {stat['count']}\n")
                file.write(f"  Écart-type : {stat['écart-type']}\n")
                file.write("----------------------\n")
        print("Rapport récapitulatif exporté dans : summary_report.txt")
    except Exception as e:
        print(f"Erreur lors de l'écriture du rapport récapitulatif : {e}")


def search_in_csv(file_path):
    """
    Permet de rechercher des informations rapidement dans un fichier CSV par produit, catégorie, prix, etc.
    """
    reader = CSVReader(file_path)
    reader.read_csv()
    data = reader.get_data()

    if not data:
        print("Le fichier est vide ou n'a pas pu être lu.")
        return

    headers = data[0]
    while True:
        try:
            print("\n=== Menu de Recherche ===")
            print("0. Quitter")
            print("1. Rechercher par colonne")
            print("2. Générer un rapport récapitulatif")

            choice = int(input("Votre choix : "))

            if choice == 0:
                print("Fermeture du menu.")
                break

            if choice == 1:
                print("\nColonnes disponibles :")
                for i, header in enumerate(headers):
                    print(f"{i + 1}. {header}")

                col_choice = int(input("Choisissez une colonne : "))

                if 1 <= col_choice <= len(headers):
                    search_column = headers[col_choice - 1]
                    search_value = input(f"Entrez la valeur à rechercher dans '{search_column}' : ")

                    print(f"\nRésultats pour '{search_value}' dans la colonne '{search_column}':")
                    col_index = col_choice - 1
                    for row in data[1:]:
                        if col_index < len(row) and search_value.lower() in row[col_index].lower():
                            print(row)
                    print("\nRecherche terminée.")
                else:
                    print("Choix de colonne invalide. Veuillez réessayer.")
            elif choice == 2:
                generate_summary_report(data)
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except Exception as e:
            print(f"Erreur : {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Outil de fusion et d'analyse de fichiers CSV.")
    parser.add_argument("--dir", default="./csv_files", help="Chemin du répertoire contenant les CSV à fusionner (par défaut: ./csv_files).")
    parser.add_argument("--output", default="merged.csv", help="Nom du fichier CSV fusionné (par défaut: merged.csv).")

    args = parser.parse_args()

    merge_all_csv_in_directory(args.dir, args.output)
    search_in_csv(args.output)
