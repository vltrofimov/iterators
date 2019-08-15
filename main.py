import json
import requests
import hashlib
with open("countries.json",encoding="utf-8") as countries:
    data_countries=json.load(countries)
list_of_countries=[]
for data in data_countries:
    list_of_countries.append(data['name']['official'])

class Myrange:
    def __init__(self, writepath,list_of_c,n):
        self.writepath = writepath
        self.list_of_c=list_of_c
        self.file = open(writepath, 'w', encoding='utf-8')
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n == 0:
            self.file.close()
            raise StopIteration
        to_write = "https://wikipedia.org/wiki/"+str(self.list_of_c[len(self.list_of_c)-self.n])
        response = requests.get('https://wikipedia.org/wiki/' + str(self.list_of_c[len(self.list_of_c)-self.n]))
        self.file.write(to_write)
        self.file.write('\n')
        self.n-=1
        return to_write
def myrange (path):
    with open (path,encoding='utf-8') as file:
        for line in file:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    for item in Myrange('test.txt',list_of_countries,len(list_of_countries)):
        print(item)
    print(myrange('test.txt'))


