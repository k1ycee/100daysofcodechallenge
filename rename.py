import os 

# os.chdir('/Users/Fruitful/Videos/Videos/Tutorial/web dev/React')

# print(os.getcwd())

# for Videos in os.listdir():
#     file_name, file_ext = os.path.splitext(Videos)
#     fnom1, fnom2 = file_name.split('&')
#     print(fnom2)

def rename_file(file_path,file_name,new_name):
    os.chdir(file_path)
    n_nom = new_name + '.txt'
    for f in os.listdir():
        f_nom, f_ext = os.path.splitext(f)
        if file_name in f_nom:
            os.rename(f, n_nom)
            break
        elif file_name not in f:
            print('filename does not exist')
rename_file('/Users/Fruitful/Documents','ruthfees','kerryfees')