from files_info import *
from files_formatter import *
import datetime


def main():
    FileOne = F.File(directory='C:/Users/Domashnev/AppData/Local/Programs/Python/Python311',
                                name='GTA6',
                                extension='.txt',
                                dataTime='2023,10,17',
                                attributes='системный',
                                deletionSign='нет',
                                numberSectors='3')
    print(formatFileInfo(FileOne))


    FileTwo = F.FileInfoNamedTuple(directory='C:/Users/Domashnev/AppData/Local/Programs/Python/Python311',
                                name='GTA5',
                                extension='.txt',
                                dataTime='2020,10,15',
                                attributes='системный',
                                deletionSign='нет',
                                numberSectors='3')
    print(formatFileInfoTuple(FileTwo))


    file_tables = F.FileInfoTypedDict(directory='C:/Users/Domashnev/AppData/Local/Programs/Python/Python311',
                                    name='GTASA',
                                    extension='.txt',
                                    dataTime='2017,10,17',
                                    attributes='системный',
                                    deletionSign='нет',
                                    numberSectors='7')
    print(formatFileInfoDict(file_tables))

    
    # moscow_dataclass = CityInfo(population=12635466, name='Moscow', \
    #                             longitude=37.62, latitude=55.75)
    # print(format_city_info(moscow_dataclass))

if __name__ == "__main__":
    main()
