from dataclasses import dataclass
from typing import NamedTuple, TypedDict
from datetime import date

@dataclass(slots=True, frozen=True )
class File:
    directory : str
    name : str
    extension : str
    dataTime : date
    attributes : str
    deletionSign : str
    numberSectors : int


class FileInfoNamedTuple(NamedTuple):
    directory : str
    name : str
    extension : str
    dataTime : date
    attributes : str
    deletionSign : str
    numberSectors : int


class FileInfoTypedDict(TypedDict):
    directory : str
    name : str
    extension : str
    dataTime : date
    attributes : str
    deletionSign : str
    numberSectors : int

if __name__ == "__main__":
    
    file_dataclass = File('C:/Users/Domashnev/AppData/Local/Programs/Python/Python311', 
                          'Barnaul',
                          'Barnaul',
                          'Barnaul',
                          'Barnaul',
                          'Barnaul',
                          1024,)
    print(file_dataclass)

    

    def fileList() -> File:
        return File (directory ='C:/Users/Domashnev/AppData/Local/Programs/Python/Python311',
                    name = 'Должники',
                    extension = 'не помню',
                    dataTime = '2020,10,17',
                    attributes = 'не помню',
                    deletionSign ='не удален',
                    numberSectors ='1024')
    
    # print(f'имя файла - {fileList().name}')
    print(fileList())

    def format_city_info(File):
        return (f"Название города: {File.name}\n {10 * '-'}\n"
                f"Долгота: {File.extension}\n")
    
    barnaul = File('Barnaul', 'Barnaul','Barnaul','Barnaul','Barnaul','Barnaul','Barnaul')
    print(format_city_info(barnaul))


    file_dataInfoTypedDict = FileInfoTypedDict(directory='C:/Users/Domashnev/AppData/Local/Programs/Python/Python311',
                                    name='GTA6',
                                    extension='.exe',
                                    dataTime='10.10.2023',
                                    attributes='системный',
                                    deletionSign='нет',
                                    numberSectors='3')
    print(file_dataInfoTypedDict) 

# class MyClass:
#     data: int
    
#     def __del__(self):
#         print("Удаление объекта MyClass")


#NamedTible 



      