from files_infoEkaterina import *
from files_formatterEkaterina import *
import datetime


def main():
    FileOne = F.File(processor='I3 3,40',
                                name='Два ядра два гига',
                                ram='8',
                                quantity='10',
                                memoryСapacity='120',
                                ramGpu='2',
                                price='13000')
    print(formatFileInfo(FileOne))


    FileTwo = F.FileInfoNamedTuple(processor='I5 5,40',
                                name='Четыре ядра Четыре гига',
                                ram='16',
                                quantity='12',
                                memoryСapacity='120',
                                ramGpu='2',
                                price='25000')
    print(formatFileInfoTuple(FileTwo))


    file_tables = F.FileInfoTypedDict(processor='I7 5,40',
                                name='Самый мощный самый лучший',
                                ram='32',
                                quantity='2',
                                memoryСapacity='500',
                                ramGpu='12',
                                price='1000000')
    print(formatFileInfoDict(file_tables))



if __name__ == "__main__":
    main()
