import csv
import shutil

devs_file_spec = {
    'fieldnames': ['Nome', 'Programa em'],
    'filename': 'programadores.csv'
}


def escrita_de_csv(devs: list):
    with open(devs_file_spec['filename'], 'w') as devs_file:
        writer = csv.DictWriter(devs_file, fieldnames=devs_file_spec['fieldnames'])
        writer.writeheader()

        for dev in devs:
            writer.writerow(dev)


def leitura_de_csv():
    with open(devs_file_spec['filename'], 'r') as devs_file:
        reader = csv.DictReader(devs_file)
        for dev in reader:
            pass


def append_no_csv(devs: list):
    with open(devs_file_spec['filename'], 'a') as devs_file:
        writer = csv.DictWriter(devs_file, fieldnames=devs_file_spec['fieldnames'])
        for dev in devs:
            writer.writerow(dev)


def contar_devs_por_linguagem(linguagem: str) -> int:
    field_linguagem = devs_file_spec['fieldnames'][1]
    with open(devs_file_spec['filename'], 'r') as devs_file:
        reader = csv.DictReader(devs_file)

        return len([True for dev in reader if dev[field_linguagem] == linguagem])


def atualiza_linguagem(anterior: str, nova: str):
    linguagem_field = devs_file_spec['fieldnames'][1]
    temp_file = 'temp.csv'

    with open(devs_file_spec['filename'], 'r') as devs_file:
        reader = csv.DictReader(devs_file)

        with open(temp_file, 'w') as temp_csv:
            writer = csv.DictWriter(temp_csv, devs_file_spec['fieldnames'])
            writer.writeheader()

            for dev in reader:
                if dev[linguagem_field] == anterior:
                    dev.update({linguagem_field: nova})

                writer.writerow(dev)

    shutil.move(temp_file, devs_file_spec['filename'])


def main():
    devs = [
        ['John Snow', 'Java'],
        ['Ines Zistente', 'C'],
        ['Yuri', 'Python'],
        ['Juliano Shopping', 'Python']
    ]

    dev_dicts = [dict(zip(devs_file_spec['fieldnames'], dev)) for dev in devs]

    escrita_de_csv(dev_dicts)
    for _ in range(10000-1):
        append_no_csv(dev_dicts)
    leitura_de_csv()
    contagem = contar_devs_por_linguagem('Python')
    print(contagem)

    atualiza_linguagem('C', 'Python')
    atualiza_linguagem('Java', 'Python')
    
    contagem = contar_devs_por_linguagem('Python')
    print(contagem)


if __name__ == '__main__':
    main()
