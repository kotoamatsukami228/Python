def input_name():
    return input('введите имя: ')

def input_surname():
    return input('введите фамилию: ')

def input_patronymic():
    return input('введите отчество: ')

def input_phone():
    return input('введите номер: ')

def input_address():
    return input('введите адрес: ')

def create_contact():
    surname=input_surname()
    name=input_name()
    patronymic=input_patronymic()
    phone=input_phone()
    address=input_address()
    
    return f'{name} {surname} {patronymic} {phone}\n {address}\n\n'

def add_contact(contact):    
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)
        
    
def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list=file.read().rstrip().split('\n\n')
        for nn,contact in enumerate(contacts_list,1):
            print(nn,contact)
    
    
def search_contact():
    var_search=input('Выберете вариант поиска: '
                     '1. По фамилии\n'
                     '2. по имени\n'
                     '3. по отчеству\n'
                     '4. По номеру телефона\n'
                     '5. По адресу\n'
                     'Ввод: ')
    
    while var_search not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные')
            var_search=input('Введите вариант поиска: ')
    
    
    index_var=int(var_search)-1
    
    search=input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list=file.read().rstrip().split('\n\n')
    for contact_str in contacts_list:
        contact_lst=contact_str.replace('\n','  ').split()
        if search in contact_lst[index_var]:
            print(contact_str)
        # if search in contact_str:
        #     print([contact_str])
    
    
def interface():
    with open('phonebook.txt','a', encoding='UTF-8'):
        pass
    command='-1'
    while command!='4':
        print('Возможные варианты взаимодействия: \n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Выход из программы')
        command=input('введите номер действия: ')
        
        while command not in ('1', '2', '3', '4'):
            print('Некорректные данные')
            command=input('Введите номер действия: ')
            
        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                print('всего хорошего!')
                
interface()
                
                
