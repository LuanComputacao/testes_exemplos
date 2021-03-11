import csv


class DevsServices:

    @staticmethod
    def read_csv():
        with open('devs.csv') as f:
            return [d for d in csv.DictReader(f)]

    @staticmethod
    def verifica_se_existe_pelo_nome(nome):
        devs = DevsServices.read_csv()
        return [d for d in devs if d.get('nome') == nome]
