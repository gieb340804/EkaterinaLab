import files_info as F
import datetime

def formatFileInfo(data) -> str:
            return (f"путь файла: {data.directory}\n "
                    f"Имя файла: {data.name} \n "
                    f"расширение: {data.extension} \n "
                    f"дата и время создания: {data.dataTime} \n "
                    f"атрибут: {data.attributes} \n "
                    f"признак удаления: {data.deletionSign} \n "
                    f"секторов: {data.numberSectors} \n {10 * '-'}\n {10 * '-'}\n")


def formatFileInfoTuple(data) -> str:
            return (f"путь файла: {data.directory}\n "
                    f"Имя файла: {data.name} \n "
                    f"расширение: {data.extension} \n "
                    f"дата и время создания: {data.dataTime} \n "
                    f"атрибут: {data.attributes} \n "
                    f"признак удаления: {data.deletionSign} \n "
                    f"секторов: {data.numberSectors} \n {10 * '-'}\n {10 * '-'}\n")

def formatFileInfoDict(data) -> str:
            return (f"путь файла: {data['directory']}\n "
                    f"Имя файла: {data['name']} \n "
                    f"расширение: {data['extension']} \n "
                    f"дата и время создания: {data['dataTime']} \n "
                    f"атрибут: {data['attributes']} \n "
                    f"признак удаления: {data['deletionSign']} \n "
                    f"секторов: {data['numberSectors']} \n {10 * '-'}\n {10 * '-'}\n")




if __name__ == "__main__":
    
    FileOne = F.File('Barnaul', 'Barnaul','Barnaul','Barnaul','Barnaul','Barnaul','Barnaul')
    print(formatFileInfo(FileOne))

    FileTwo = F.File(directory='C:/Users/Domashnev/AppData/Local/Programs/Python/Python311',
                                name='GTA6',
                                extension='.exe',
                                dataTime='10.10.2023',
                                attributes='системный',
                                deletionSign='нет',
                                numberSectors='3')
    print(formatFileInfo(FileTwo))

    file_table = F.FileInfoNamedTuple('Barnaul123', 'Barnaul','Barnaul','Barnaul','Barnaul','Barnaul','Barnaul')
    print(formatFileInfoTuple(file_table))

    file_tables = F.FileInfoTypedDict(directory='C:/Users/Domashnev/AppData/Local/Programs/Python/Python311',
                                    name='GTA6',
                                    extension='.exe',
                                    dataTime='10.10.2023',
                                    attributes='системный',
                                    deletionSign='нет',
                                    numberSectors='5')
    print(formatFileInfoDict(file_tables))


    