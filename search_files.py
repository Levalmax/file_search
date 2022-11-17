import os
import datetime

serialNumber ='8405'  #Вводим заводской номер тр-ра для поиска
catalog = 'Z:\Протоколы\Протоколы Выезд' #Указываем папку поиска

def timeOff(function_to_decorate): #функция декоратор для подсчета времени выполнения поиска.
    def obertka(a,b):
        start = datetime.datetime.now()
        print('Начало сортировки: ', start.second,'.',start.microsecond, 'сек')
        function_to_decorate(a,b)
        stop = datetime.datetime.now()
        print('Конец сортировки: ', stop.second, '.', stop.microsecond, 'сек')
        c = stop.second - start.second
        e = stop.microsecond - start.microsecond
        print('Время выполнения:', c, '.', e, 'сек')
    return obertka


@timeOff
def find_all(search,path):  
  dictionary = {}
  newDictionary = {}
  allSerialNumberFind = []
  i = 0
  for root, dirs, files in os.walk(path):
    dictionary[root] = files #получили словарь, где keys -это директория, а values  - список файлов.
  
  """ Проходимся циклом по именам файлов,
  и выделяем заводской номер тр-ра из имени файла.
  Далее создаем словарь, где key - путь к фалу, values - заводской номер тр-ра.
  Т.к. путь фала может быть один и тотже,то для того что бы не
  повторялся путь в словаре приписываем спереди значение i.
  Создается новый словарь newDictionary. """

  for key in dictionary:   #прохождение цмклом по словарю dictionary
    for names in dictionary[key]: # прохождение по именам фалов
      all = names.split('_') #т.к. все фалы имеют наименование серийный номер_подстанция_и т.д., разбиваем через split("_")
      rootId = str(i) + '_' + key #создаем уникальное значение key для словаря
      newDictionary[rootId] = all[0] #создаем новый словарь
      i += 1

  """ Нахождение нужного номера среди имен файлов """
  for searchNumber in newDictionary:
    if newDictionary[searchNumber] == serialNumber:
      v = searchNumber.split('_') #отделяем i от имени пути расположения файла
      allSerialNumberFind.append(newDictionary[searchNumber]) #создаем список с заводскими номерами
      print ('Найден заводской номер: ',serialNumber, '-->', v[1])
        
  return print(allSerialNumberFind) #дополнительно выводим список с найденными заводскими номерами



if __name__ == '__main__':
  find_all(serialNumber, catalog)

        

