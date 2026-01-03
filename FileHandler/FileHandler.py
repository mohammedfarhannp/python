class FileHandler:
    def Read(self, File_Name):
        with open(File_Name, 'r') as File:
            Data = File.read()
        return Data

    def Write(self, File_Name, Data):
        try:
            with open(File_Name, 'w') as File:
                File.write(str(Data))
            return True

        except:
            return False

    def B_Read(self, File_Name):
        with open(File_Name, 'rb') as File:
            Data = File.read()
        return Data

    def B_Write(self, File_Name, Data):
        try:
            with open(File_Name, 'wb') as File:
                File.write(Data)
            return True

        except:
            return False

    def Handler(self, File_Name, Mode):
        return open(File_Name, Mode)

