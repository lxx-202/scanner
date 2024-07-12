import exrex
import requests

class Mulu:
    def __int__(self):
        pass
    def get_contents(self):
        with open("PHP.txt", "r") as f:
            contents = f.read().splitlines()
            return contents


    def get_url(self,url,contents):
        new_url_list=[]
        for value in contents:
            new_url = "http://"+url + "/" +value
            res=requests.get(new_url)
            if res.status_code == 200 or res.status_code == 403 or res.status_code == 302:
                new_url_list.append(new_url)
        return new_url_list


    def put_contents(self,new_url_list):
        with open("url.txt","a") as f:
            for value in new_url_list:
                f.write(value+"\n")

    def run(self):

       contents = self.get_contents()
       url = (input("请输入url:"))
       print(self.get_url(url, contents))
       self.put_contents(self.get_url(url, contents))



if __name__ == '__main__':
   Mulu().run()




