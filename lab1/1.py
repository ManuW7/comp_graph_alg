import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Пути к изображениям
IMAGE1_PATH = "1.jpg"
IMAGE2_PATH = "2.jpg"

# Загружаем изображения
img1 = Image.open(IMAGE1_PATH).convert("RGB")
img2 = Image.open(IMAGE2_PATH).convert("RGB")

root = tk.Tk()
root.title("RGB-анализ")
root.geometry("800x600")

# Картинка
label_img = tk.Label(root)
label_img.place(x=200, y=20)

# Значения R/G/B
label_values = tk.Label(root, text="R: -  G: -  B: -")
label_values.place(x=200, y=300)

# Фигура matplotlib
fig, ax = plt.subplots(figsize=(4,2.5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(x=200, y=330)

def compute_rgb(pil_img):
    """Суммируем все пиксели и делим на количество"""
    w, h = pil_img.size
    pixels = pil_img.load()
    total = w * h
    sum_r = sum_g = sum_b = 0
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            sum_r += r
            sum_g += g
            sum_b += b
    return sum_r/total, sum_g/total, sum_b/total

def show(pil_img):
    # Показ картинки и сохранение ссылки в label
    photo = ImageTk.PhotoImage(pil_img)
    label_img.image = photo
    label_img.config(image=photo)

    # Вычисляем средние
    r, g, b = compute_rgb(pil_img)
    label_values.config(text=f"R: {r:.2f}  G: {g:.2f}  B: {b:.2f}")

    # Рисуем три столбика
    ax.clear()
    ax.bar(["R","G","B"], [r,g,b], color=["red","green","blue"])
    ax.set_ylim(0,255)
    canvas.draw()

# Кнопки
btn1 = tk.Button(root, text="Картинка 1", command=lambda: show(img1))
btn1.place(x=20, y=20, width=150, height=40)

btn2 = tk.Button(root, text="Картинка 2", command=lambda: show(img2))
btn2.place(x=20, y=70, width=150, height=40)

root.mainloop()
