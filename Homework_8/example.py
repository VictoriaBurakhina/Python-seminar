import json



def get_data_from_json(file):
    with open (file, 'r', encoding='Utf-8') as f:  #открыли файл с данными
        value = json.load(f)#загнали все,что надо в переменную
        result = value["input_cell"]
        return result  #вывели результат на экран







