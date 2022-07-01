from PIL import Image

word_matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')
mask = mask.resize((1015, 559))
mask.putalpha(200)
word_matrix.paste(im=mask, box=(0, 0), mask=mask)
word_matrix.save('exercise_solved.png')
