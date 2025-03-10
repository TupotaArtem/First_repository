def get_cats_info(path):
    try:
        with open(path) as file:
            cats=[]

            for line in file:
                id,name,age = line.strip().split(',')
                cats.append( {"id": id, "name": name, "age": age})

            if not cats:
                return 0   
            
        return cats
        
    except FileNotFoundError:
        print("Файл не знайдено")  
        return None

    except Exception as e:
        print(f"Невідома помилка {e}")
        return None
    
if __name__=='__main__': 
    cats_info=get_cats_info('/home/tupota/Python_cors_HW/First_repository/HW_4/cats_info.txt')
    print(cats_info)
    