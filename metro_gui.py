import tkinter as tk
from tkinter import ttk, messagebox
from HayriyeNurYildizoglu_MetroSimulation import MetroAgi
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Metro ağı kurulumunu yapar ve istasyonları bağlantılarıyla birlikte ekler

def metro_agini_olustur():
    metro = MetroAgi()

    # İstasyonlar
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)
    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)
    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)
    return metro

# Ana GUI sınıfı
class MetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sürücüsüz Metro Simülasyonu")
        self.root.geometry("600x600")
        self.metro = metro_agini_olustur()

        self.istasyonlar = list(self.metro.istasyonlar.keys())

        # Başlangıç ve hedef seçim alanları
        ttk.Label(root, text="Başlangıç İstasyonu:").pack(pady=5)
        self.baslangic_combo = ttk.Combobox(root, values=self.istasyonlar)
        self.baslangic_combo.pack()

        ttk.Label(root, text="Hedef İstasyon:").pack(pady=5)
        self.hedef_combo = ttk.Combobox(root, values=self.istasyonlar)
        self.hedef_combo.pack()

        # Düğmeler
        ttk.Button(root, text="En Az Aktarma (BFS)", command=self.goster_bfs).pack(pady=10)
        ttk.Button(root, text="En Hızlı Rota (A*)", command=self.goster_astar).pack(pady=10)
        ttk.Button(root, text="Metro Ağı Grafiğini Göster", command=self.grafigi_goster).pack(pady=10)

        self.sonuc_label = ttk.Label(root, text="")
        self.sonuc_label.pack(pady=10)

        self.canvas_widget = None  # Çizilen grafik için tkinter canvas referansı

    # BFS algoritması ile en az aktarmalı rota
    def goster_bfs(self):
        bas = self.baslangic_combo.get()
        hedef = self.hedef_combo.get()
        if bas and hedef:
            rota = self.metro.en_az_aktarma_bul(bas, hedef)
            if rota:
                yol = " -> ".join(i.ad for i in rota)
                self.sonuc_label.config(text=f"En az aktarma: {yol}")
                self.grafigi_goster(rota)
            else:
                messagebox.showinfo("Bilgi", "Rota bulunamadı.")
        else:
            messagebox.showwarning("Uyarı", "İstasyonları seçin.")

    # A* algoritması ile en hızlı rota
    def goster_astar(self):
        bas = self.baslangic_combo.get()
        hedef = self.hedef_combo.get()
        if bas and hedef:
            sonuc = self.metro.en_hizli_rota_bul(bas, hedef)
            if sonuc:
                rota, sure = sonuc
                yol = " -> ".join(i.ad for i in rota)
                self.sonuc_label.config(text=f"En hızlı rota ({sure} dk): {yol}")
                self.grafigi_goster(rota)
            else:
                messagebox.showinfo("Bilgi", "Rota bulunamadı.")
        else:
            messagebox.showwarning("Uyarı", "İstasyonları seçin.")

    # Metro ağı grafiğini çizen fonksiyon
    def grafigi_goster(self, rota=None):
        g = nx.Graph()
        pos = {}
        labels = {}

        # Düğümleri oluştur
        for istasyon in self.metro.istasyonlar.values():
            g.add_node(istasyon.idx)
            labels[istasyon.idx] = istasyon.ad

        # Kenarları oluştur
        kenarlar = set()
        for istasyon in self.metro.istasyonlar.values():
            for komsu, _ in istasyon.komsular:
                if (komsu.idx, istasyon.idx) not in kenarlar:
                    g.add_edge(istasyon.idx, komsu.idx)
                    kenarlar.add((istasyon.idx, komsu.idx))

        # Otomatik pozisyonlama
        pos = nx.spring_layout(g, seed=42)

        # Rota üzerindeki kenarları yeşil yap
        kenar_renkleri = []
        for u, v in g.edges():
            if rota and self._kenar_rotada(u, v, rota):
                kenar_renkleri.append("green")
            else:
                kenar_renkleri.append("gray")

        # Çizim işlemi
        fig, ax = plt.subplots(figsize=(6,5))
        nx.draw(
            g, pos, ax=ax, with_labels=True, labels=labels,
            node_color='skyblue', edge_color=kenar_renkleri,
            node_size=700, font_size=8
        )

        # Önceki grafik varsa kaldır
        if self.canvas_widget:
            self.canvas_widget.get_tk_widget().destroy()

        # Yeni grafiği göster
        self.canvas_widget = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas_widget.get_tk_widget().pack(pady=10)
        self.canvas_widget.draw()

    # Rota üzerinde bir kenar var mı kontrolü
    def _kenar_rotada(self, u, v, rota):
        for i in range(len(rota) - 1):
            a, b = rota[i].idx, rota[i+1].idx
            if (u == a and v == b) or (u == b and v == a):
                return True
        return False

# Uygulamayı başlat
if __name__ == "__main__":
    root = tk.Tk()
    app = MetroApp(root)
    root.mainloop()