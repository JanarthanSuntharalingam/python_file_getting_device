import os

class FileManager():
    img_file = []
    aud_file = []
    vid_file = []
    def __init__(self):
        global base_dir
        base_dir = os.getcwd()
        self.direc_list = []
        self.direc = os.listdir()
        for self.dm in self.direc:
            if self.dm[0] != '.':
                self.direc_list.append(self.dm)
        length = len(self.direc_list)      
        self.single_file_use(self.direc_list)

    def single_file_use(self, list):
        self.list = list
        for i in self.list:
            self.file_type(i)
        
    def file_type(self, file_name):
        self.file_name = file_name
        if os.path.isdir(self.file_name) == True:
            self.directory_details(self.file_name)
        elif os.path.isfile(self.file_name) == True:
            print(self.file_name)
            
    def directory_details(self, file):
        self.file = file
        opt =0
        length = os.listdir(self.file)
        for deem in length:
            src = (self.file + '/' + deem)
            self.file_fixing(deem, src)

    def file_fixing(self, file, src):
        self.file = file
        self.src =src
    
        if self.file.endswith(".mp3") or self.file.endswith(".wav") or self.file.endswith(".m4a"):
            self.aud_file.append(self.src)
        elif self.file.endswith(".jpg") or self.file.endswith(".jpeg") or self.file.endswith("png") or self.file.endswith(".svg"):
            self.img_file.append(self.file)
        elif self.file.endswith(".mp4"):
            self.vid_file.append(self.file)
        else:
            print("not matching : ", self.file)

if __name__ == '__main__':
    obj = FileManager()  
    print("audios : ",obj.aud_file)
    print("images : ",obj.img_file)
    print("videos : ",obj.vid_file)
