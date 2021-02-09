'''
I have written a class.
It has a text writer method.
The method gets two input arguments: content=" "  and name=" "
Name has a default value of text.txt
Content has no default value
'''

from classes import text_writer_file
name=input("name: ")
content=input("content: ")
instance=text_writer_file.text_writer(content,name)
instance.attack()
print(instance.param)