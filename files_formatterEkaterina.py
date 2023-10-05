import files_infoEkaterina as F
import datetime

def formatFileInfo(data) -> str:
            return (f"модели компьютера: {data.name} \n "
                    f"частотой процессора: {data.processor}Ггц \n "
                    f"объемом ОЗУ: {data.ram}Gb \n "
                    f"объемом жесткого диска: {data.memoryСapacity} Gb \n "
                    f"объемом памяти видеокарты: {data.ramGpu} Gb\n "
                    f"цена компьютера: {data.price} Руб\n "
                    f"имеющихся в наличии: {data.quantity} Шт \n {10 * '-'}\n {10 * '-'}\n")


def formatFileInfoTuple(data) -> str:
            return (f"модели компьютера: {data.name} \n "
                    f"частотой процессора: {data.processor}Ггц \n "
                    f"объемом ОЗУ: {data.ram}Gb \n "
                    f"объемом жесткого диска: {data.memoryСapacity} Gb \n "
                    f"объемом памяти видеокарты: {data.ramGpu} Gb\n "
                    f"цена компьютера: {data.price} Руб\n "
                    f"имеющихся в наличии: {data.quantity} Шт \n {10 * '-'}\n {10 * '-'}\n")

def formatFileInfoDict(data) -> str:
            return (f"модели компьютера: {data['name']}\n "
                    f"частотой процессора: {data['processor']} Ггц\n "
                    f"объемом ОЗУ: {data['ram']} Gb\n "
                    f"объемом жесткого диска: {data['memoryСapacity']} Gb\n "
                    f"объемом памяти видеокарты: {data['ramGpu']} Gb\n "
                    f"цена компьютера: {data['price']} руб\n "
                    f"имеющихся в наличии: {data['quantity']} Шт\n {10 * '-'}\n {10 * '-'}\n")

