def write_file(file_name, file_content):
    with open(str(file_name) +'.txt', 'w') as file:
     file.write(str(file_content))

def append_file(file_name, append_content):
    with open(str(file_name) +'.txt', 'a') as file:
       file.write(str(append_content))

def read_file(file_name):
   with open(str(file_name) +'.txt', 'r') as file:
      file_content_read = file.read()
      return file_content_read
