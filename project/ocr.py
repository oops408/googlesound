import easyocr
import matplotlib.pyplot as plt 

reader = easyocr.Reader(['en'])
result = reader.readtext('test.png')
text_only = reader.readtext('test.png', detail=0, paragraph=True)
print(result)
print(text_only)

im = plt.imread('test.png')

fig = plt.figure(figsize=(15,15))

plt.imshow(im)

for _ in result:
    x = [n[0] for n in _[0]]
    y = [n[1] for n in _[0]]
    plt.fill(x,y, facecolor='none', edgecolor='red')
    plt.text(x[0],y[0], _[1], color='red', fontsize=15)

plt.axis('off')
plt.savefig('output.png')
plt.show()

text_to_write = "\n".join(text_only)

with open("output.txt", "w") as text_file:
    text_file.write(text_to_write)