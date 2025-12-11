# createe a file add data in.txt file

with open ("suraja.tx","r") as p:
    data=p.read()
    new_data=data.replace("java ","pythone")
    print(new_data)
    p.write(new_data) 