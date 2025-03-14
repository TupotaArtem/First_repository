def total_salary(path):
    try:
        with open(path) as file:
            ls=[]

            for line in file:
                name,cost = line.strip().split(',')
                ls.append(int (cost))

            if not ls:
                return 0, 0   

            total= sum(ls)
            average= total/len(ls)
            
        return total,average
        
    except FileNotFoundError:
        print("Файл не знайдено")  
        return None,None  

    except Exception as e:
        print(f"Невідома помилка {e}")
        return None,None 
    
if __name__=='__main__': 
    tot,average=total_salary('text.txt')
    print(f"Загальна сума заробітної плати: {tot}, Середня заробітна плата: {average}")