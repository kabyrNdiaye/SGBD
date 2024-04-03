from tkinter import *
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from function import *

class DashboardOpencart:
    def __init__(self,root):
        self.root = root
        self.root.title("client Opencart")
        self.root.geometry("1366x768")
        self.root.config(bg="#eff5f6")
        ######En tete
        self.entete = Frame(self.root,bg="#09093d")
        self.entete.place(x = 300,y = 0,width=1070,height=60)
        self.deconnecte = Button(self.entete,text="Logout",bg="#ffffff",font=("sans serif",13,"bold"),bd=0,fg="#09093d",cursor="hand2")
        self.deconnecte.place(x=900,y=15)
        #Menu
        self.FrameMenu = Frame(self.root,bg="#ffffff")
        self.FrameMenu.place(x=0,y=0,width=300,height=750)
        self.logoImage = Image.open(r"opencart-logo.png")
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.FrameMenu,image = photo,bg="#ffffff" )
        self.logo.image1 = photo
        self.logo.place(x = 70,y=15)
        
        ##ajouter profil de l'administrateur
        self.profilImage = Image.open(r"admin.ico")
        photo = ImageTk.PhotoImage(self.profilImage)
        self.logo = Label(self.FrameMenu,image = photo,bg="#ffffff" )
        self.logo.image2 = photo
        self.logo.place(y=100)
        self.Nom =Label(self.FrameMenu,text="Admin",bg="#ffffff",font=("sans serif",13,"bold"))
        self.Nom.place(x=75,y=250)
        ##corps
        self.titre = Label(self.entete,text = "Opencart",font=("sans serif",23,"bold"),fg="#ffffff",bg="#09093d")
        self.titre.place(x=10,y=10)
        self.corp1 = Frame(self.root , bg="#ffffff")
        self.corp1.place(x=315,y=257, width = 930 , height = 300)
        self.corp2 = Frame(self.root, bg="#1b80c2")
        self.corp2.place(x=315, y=83, width=230, height=150)
        self.entete2 = Frame(self.corp2,bg="#09093d")
        self.entete2.place(width=230,height=35)
        self.entete2Label1 = Label(self.entete2,text="COMMANDES TOTALES",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        self.entete2Label1.place(x=5,y=4)
        self.entete2Label2 = Label(self.entete2,text="0%",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        self.entete2Label2.place(x=200,y=4)
        self.corp2Label = Label(self.corp2,text=TotalOrders(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp2Label.place(x=200,y=65)
        self.corp3 = Frame(self.root, bg="#1b80c2")
        self.corp3.place(x=562, y=83, width=230, height=150)
        self.entete3 = Frame(self.corp3,bg="#09093d")
        self.entete3.place(width=230,height=35)
        self.entete3Label1 = Label(self.entete3,text="VENTES TOTALES",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        self.entete3Label1.place(x=5,y=4)
        self.entete3Label2 = Label(self.entete3,text="0%",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        self.entete3Label2.place(x=200,y=4)
        self.corp3Label = Label(self.corp3,text=TotalSales(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp3Label.place(x=150,y=65)
        self.corp4 = Frame(self.root, bg="#1b80c2")
        self.corp4.place(x=809, y=83, width=230, height=150)
        self.entete4 = Frame(self.corp4,bg="#09093d")
        self.entete4.place(width=230,height=35)
        self.entete4Label1 = Label(self.entete4,text="CLIENTS TOTAUX",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        self.entete4Label1.place(x=5,y=4)
        self.entete4Label2 = Label(self.entete4,text="0%",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        self.entete4Label2.place(x=200,y=5)
        self.corp4Label = Label(self.corp4,text=TotalCustomers(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp4Label.place(x=200,y=65)
        self.corp5 = Frame(self.root, bg="#1b80c2")
        self.corp5.place(x=1056, y=83, width=188, height=150)
        self.entete5 = Frame(self.corp5,bg="#09093d")
        self.entete5.place(width=230,height=35)
        self.entete5Label1 = Label(self.entete5,text="PEOPLE ONLINE",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        self.entete5Label1.place(x=5,y=5)
        self.entete5Label2 = Label(self.entete5,text="0%",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        self.entete5Label2.place(x=160,y=4)
        self.corp5Label = Label(self.corp5,text=PeopleOnline(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp5Label.place(x=160,y=65)

        # self.corp6 = Frame(self.root, bg="#1b80c2")
        # self.corp6.place(x=1056, y=83, width=188, height=150)
        # self.entete6 = Frame(self.corp6,bg="#09093d")
        # self.entete6.place(width=230,height=35)
        # self.entete6Label1 = Label(self.entete6,text="TOTAL TRANSACTIONS",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        # self.entete6Label1.place(x=5,y=4)
        # self.entete6Label2 = Label(self.entete6,text="0%",font=("sans serif",11,"bold"),fg="#ffffff",bg="#09093d")
        # self.entete6Label2.place(x=160,y=4)
        # self.corp6Label = Label(self.corp6,text=TotalTransactions(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        # self.corp6Label.place(x=160,y=65)

        ##bouton de sortie
        self.logOut = Button(self.FrameMenu,bd=0,text="Quit",bg="#ffffff",font=("sans serif",13,"bold"),command=self.root.quit) 
        self.logOut.place(x=25,y=650,width=265)
        self.sortieImage = Image.open(r"arrow.png")
        photo = ImageTk.PhotoImage(self.sortieImage)
        self.logo = Label(self.FrameMenu,image = photo,bg="#ffffff")
        self.logo.image3 = photo
        self.logo.place(x=20,y=650)
        
        self.corp1 = Frame(self.root, bg="#ffffff")
        self.corp1.place(x=315, y=257, width=930, height=300)

        # Générer des données de chiffre d'affaires pour chaque mois
        # Imaginons que chaque mois a un 'chiffre d'affaires' distinct que nous voulons afficher
        chiffre_affaires = np.random.randint(100, 1000, size=12) * 1e6  # Chiffre en millions

        # Créer l'histogramme
        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.plot = self.figure.add_subplot(1, 1, 1)
        
        # Simulation d'un histogramme avec les données de chiffre d'affaires pour chaque mois
        mois = np.arange(1, 13)  # De 1 (Janvier) à 12 (Décembre)
        self.plot.hist(mois, bins=12, weights=chiffre_affaires, rwidth=1.0,edgecolor='black',linewidth=0.8)
        
        self.plot.set_title('chiffre d\'affaires par mois')
        self.plot.set_xticks(mois)
        self.plot.set_xticklabels(['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc'])
        self.plot.set_ylabel('Chiffre d\'affaires (en milliards)')
        self.plot.set_ylim(0, 1e9)  # Limite pour correspondre à 1 milliard

        # Ajout de l'histogramme à Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, self.corp1)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
if __name__ == "__main__":
    root = Tk()
    DashboardOpencart(root)
    root.mainloop()