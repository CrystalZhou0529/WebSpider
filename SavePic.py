import requests
import os

if __name__=="__main__":
    root = "C:\\Users\\chris\\Desktop\\Treasure\\zyl photo\\"
    url = input("URL:")
    #url = "http://pic1.win4000.com/wallpaper/2018-09-29/5baed5702d0ec.jpg"
    path = root + url.split("/")[-1]
    if len(path)>50:
        path = root + "pic.jpg"
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if os.path.exists(path):
            i = 1
            while os.path.exists(path):
                path = root + "pic(" + str(i) + ").jpg"
                i+=1
        if not os.path.exists(path):
            r=requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("Save")

        else:
            print("Repeated name!")
    except:
        print("False!")        

