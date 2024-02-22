def contador(num):
    if num <= 1000:
        print(num)
        contador(num + 1)

contador(1) 
