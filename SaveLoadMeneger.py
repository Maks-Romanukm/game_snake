import pickle
import os
#wb = write bite = запизувати байти
#rw = read bite = читати байти

class SaveLoadSystem:
    # ініцилізуємо
    def __init__(self, file_extension, save_folder):
        self.file_extension = file_extension  # file_extension = розширення файлу
        self.save_folder = save_folder  # save_folder = зберегти папку

    # для збереження та завантаження даних                                   записуємо сюда байти
    def save_data(self, data, name):
        data_file = open(self.save_folder + "/" + name + self.file_extension, "wb")# відкрити папку/назва/розшиорення файлу(txt, pdf)
        pickle.dump(data, data_file)#сериалізація = pickle.dump = коли беремо x і зберігаємо

    def load_data(self, name):#завантажати
        data_file = open(self.save_folder + "/" + name + self.file_extension, "rb")
        data = pickle.load(data_file)#завантажуємо файл
        return data # вернути завантажений  файл

    def check_for_file(self, name):# перевірка файлу
        return os.path.exists(self.save_folder + "/" + name + self.file_extension)

    '''Якщо файлів збережених  немає або ПЛАН Б'''
    def load_game_data(self, files_to_load, default_data):# якщо даних немає значення по стандарту
        variables = []
        for index, file in enumerate(files_to_load):
            if self.check_for_file(file):
                variables.append(self.load_data(file))
            else:
                variables.append(default_data[index])

        if len(variables) > 1:
            return tuple(variables)
        else:
            return variables[0]
    '''список усіх даних = data to save, назва файлу = file name'''
    def save_game_data(self, data_to_save, file_names):#метод масового збереження
        for index, file in enumerate(data_to_save):
            self.save_data(file, file_names[index])
