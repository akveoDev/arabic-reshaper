import arabic_reshaper
import sys

file_path = sys.argv[1]
with open(file_path, "r") as myfile:
    text=''.join(myfile.readlines())

text_to_be_reshaped = 'اللغة العربية رائعة'
reshaped_text = arabic_reshaper.reshape(text)

output_file = open(file_path, "w")
output_file.write(reshaped_text)
output_file.close()