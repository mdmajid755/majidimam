import tkinter as tk

class SimpleCalc:
    def __init__(self, root):
        self.root = root
        self.root.title("Basit Hesap Makinesi")
        
        # Giriş/çıkış için metin kutusu
        self.display = tk.Entry(root, width=20)
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Sayılar ve işlemler için düğmeler
        düğmeler = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '=', '+', 
        ]
        
        # Düğmeleri oluşturun ve ızgaraya yerleştirin
        satır, sütun = 1, 0
        for düğme_metni in düğmeler:
            tk.Button(root, text=düğme_metni, width=5, command=lambda t=düğme_metni: self.düğme_tıklama(t)).grid(row=satır, column=sütun)
            sütun += 1
            if sütun > 3:
                sütun = 0
                satır += 1
    
    def düğme_tıklama(self, düğme_metni):
        mevcut_metin = self.display.get()
        
        if düğme_metni == '=':
            try:
                sonuç = eval(mevcut_metin)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(sonuç))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Hata")
        else:
            self.display.insert(tk.END, düğme_metni)
            

if __name__ == "__main__":
    root = tk.Tk()
    hesap_makinesi = SimpleCalc(root)
    root.mainloop()
