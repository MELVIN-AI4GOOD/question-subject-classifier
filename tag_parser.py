class TagParser:
    """
    Classe com todas as funções para realizar parsing dos arquivos com tags das questões
    """
    def __init__(self):
        pass

    @staticmethod
    def parse_txt(path: str) -> list[str]:
        """
        :param path: caminho do arquivo contendo as tags
        :return: lista com todas as tags em minúsculo
        """
        tag_list = []
        with open(path, "r") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                tag_list.append(line.strip().lower())
        return tag_list


# Teste

if __name__ == '__main__':
    parser = TagParser()
    biologia = parser.parse_txt("tags/biologia.txt")
    print(biologia)
