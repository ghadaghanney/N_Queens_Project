from tkinter import *

echiquier=[] 
position_reine=[] 
solution=[]


def init_echiquier(n):
    for i in range(0,n):
        position_reine.append(0)
        L=[]
    for k in range(0,n):
        L.append(0)
    echiquier.append(L)
    
    
    
#Affichage de toutes les solutions possibles
def afficher_solution():
    for ligne in echiquier:
        for case in ligne:
            print(case,"",end="")
        
    
# Placer les reines sur l'echiquier
def placer_reine(n):
    for i in range(0,n): 
        for k in range(0,n):
            echiquier[i][k]=0
    for i in range(0,n):
        echiquier[position_reine[i]][i]= 1
    afficher_solution()

    
    
#Fonction de teste si la case est valide:
def Valider(L ,co):
    for i in range(0,co):
        if position_reine[i]==L or abs(position_reine[i]-L)==abs(i-co):
            return 0
    return 1





def placer_toute_reines(col,n):
    global k,x,t,solution #pour compter les solutions
    if(col==n):        
        solution=solution+position_reine
        print(position_reine)
        x=int(k.get())+1
        k.set(x)
    else :
#pour une colonne donne, on teste si l'une des ligne est valide pour placer la reine,

     for i in range(0,n): 
        if(Valider(i,col)): 
            position_reine[col]=i 
            placer_toute_reines(col+1,n) 
    
  
    
def calculer(n):
    global k,clic,position_reine,solution
    solution=[]
    clic.set(0)
    position_reine=[]
    k.set(0)
    init_echiquier(n)
    placer_toute_reines(0,n)
   
    

def voir(n):
    global clic,k
    cli=int(clic.get())-1
    d=400//n
    for i in range(n):
        col=list(range(n))
        for j in range(n):
            col[i]=list(range(n))
            lo=i*d
            ha=j*d
            col[i][j]=c.create_rectangle(lo,ha,lo+d,ha+d,outline='white',fill='blue')
                           
    for i in range (n*cli,n*cli+n):
            c.create_oval(solution[i]*d+1,(i-n*cli)*d+1,solution[i]*d+d-1,(i-n*cli)*d+d-1,fill='white')
    if cli+1<int(k.get()):
        cli=cli+1
        clic.set(cli+1)
                           
                           
                           
                           
#debut programme :
x=0
solution=[]
#cherche_solution(0)
f=Tk()
clic=StringVar()
clic.set(1) 
k=StringVar()
k.set(0)
c = Canvas(f,bg='white',height=500,width=500)
c.pack(side=TOP)
spin=Spinbox(f, values=(4,5,6,7,8,9,10,11), width=4)
spin.config( font="sans 12", justify="center")
spin.pack()
b=Button(f,text="Calculer",command=lambda:calculer(int(spin.get())))
b.pack()
ll=Label(f,text="Nombre de solutions")
ll.pack()
l=Label(f,textvariable=k)
l.pack()
Label(f).pack()
bb=Button(f,text="Voulez-vous voir la solution ? ",command=lambda:voir(int(spin.get())))
bb.pack()
lll=Label(f,textvariable=clic)
lll.pack()
f.mainloop()
print('Nombre de solutions:',k.get())