import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import *
import sqlite3

# --------- FRAMES - PRINCIPAL -------------
janela = Tk()
janela.title("Aplicativo de Cadastramento")
janela.geometry("900x600+1000+200")
janela.iconbitmap("")
janela.config(bg='grey')

# --------- VARIAVEIS -------------

nome = StringVar()
telefone = StringVar()
idade = StringVar()
email = StringVar()
endereco = StringVar()
av1 = StringVar()
av2 = StringVar()
av3 = StringVar()
avd = StringVar()
id = None
updateWindow = None
newWindow = None

# --------- METODOS -------------


def database():
    conn = sqlite3.connect("")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'alunos' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT, telefone TEXT, idade TEXT, email TEXT, endereco TEXT, av1 TEXT, av2 TEXT, av3 TEXT, avd TEXT) """
    cursor.execute(query)
    cursor.execute("SELECT * FROM 'alunos' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def submitData():
    if nome.get() == "" or telefone.get() == "" or idade.get() == "" or email.get() == "" or endereco.get() == "" or av1.get() == "" or av2.get() == "" or avd.get() == "":
        resultado = msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("")
        cursor = conn.cursor()
        query = """ INSERT INTO 'alunos' (nome, telefone, idade, email, endereco, av1, av2, av3, avd) VALUES(?, ?, ?, ?, ?, ? , ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), str(telefone.get()), str(idade.get()), str(email.get()), str(endereco.get()), str(av1.get()), str(av2.get()), str(av3.get()), str(avd.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'alunos' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        telefone.set("")
        idade.set("")
        email.set("")
        endereco.set("")
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")

def updateData():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("cadastro.db")
    cursor = conn.cursor()
    cursor.execute(""" UPDATE 'alunos' SET nome = ?, telefone = ?, idade = ?, email = ?, endereco = ?, SET av1 = ?, SET av2 = ?, SET av3 = ?, SET avd = ?, WHERE id = ?""", (str(nome.get()), str(telefone.get()), str(idade.get()), str(email.get()), str(endereco.get()), str(av1.get()), str(av2.get()), str(av3.get()), str(avd.get()), int(id)))
    conn.commit()
    cursor.execute("SELECT * FROM 'alunos' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    updateWindow.destroy()


def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo['values']
    id = selectedItem[0]
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    nome.set(selectedItem[1])
    telefone.set(selectedItem[2])
    idade.set(selectedItem[3])
    email.set(selectedItem[4])
    endereco.set(selectedItem[5])
    av1.set(selectedItem[6])
    av2.set(selectedItem[7])
    av3.set(selectedItem[8])
    avd.set(selectedItem[9])
    # --------- FRAMES - ATUALIZAR -------------
    updateWindow = Toplevel()
    updateWindow.title("**** ATUALIZANDO CONTATO *****")
    formTitulo = Frame(updateWindow)
    formTitulo.pack(side=TOP)
    formContato = Frame(updateWindow)
    formContato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = updateWindow.winfo_screenwidth()
    sc_height = updateWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)

    # --------- LABELS - ATUALIZAR -------------
    lbl_title = Label(formTitulo, text="Atualizando Item", font=('arial', 18), bg='blue', width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContato, text='Nome', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(formContato, text='telefone', font=('arial', 12))
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(formContato, text='Idade', font=('arial', 12))
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(formContato, text='Email', font=('arial', 12))
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(formContato, text='Endereco', font=('arial', 12))
    lbl_endereco.grid(row=4, sticky=W)
    lbl_av1 = Label(formContato, text='AV1', font=('arial', 12))
    lbl_av1.grid(row=5, sticky=W)
    lbl_av2 = Label(formContato, text='AV2', font=('arial', 12))
    lbl_av2.grid(row=6, sticky=W)
    lbl_av3 = Label(formContato, text='AV3', font=('arial', 12))
    lbl_av3.grid(row=7, sticky=W)
    lbl_avd = Label(formContato, text='AVD', font=('arial', 12))
    lbl_avd.grid(row=8, sticky=W)

    # --------- ENTRY - ATUALIZAR -------------
    nomeEntry = Entry(formContato, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    telefoneEntry = Entry(formContato, textvariable=telefone, font=('arial', 12))
    telefoneEntry.grid(row=1, column=1)
    idadeEntry = Entry(formContato, textvariable=idade, font=('arial', 12))
    idadeEntry.grid(row=2, column=1)
    emailEntry = Entry(formContato, textvariable=email, font=('arial', 12))
    emailEntry.grid(row=3, column=1)
    enderecoEntry = Entry(formContato, textvariable=endereco, font=('arial', 12))
    enderecoEntry.grid(row=4, column=1)
    av1Entry = Entry(formContato, textvariable=av1, font=('arial', 12))
    av1Entry.grid(row=5, column=1)
    av2Entry = Entry(formContato, textvariable=av2, font=('arial', 12))
    av2Entry.grid(row=6, column=1)
    av3Entry = Entry(formContato, textvariable=av3, font=('arial', 12))
    av3Entry.grid(row=7, column=1)
    avdEntry = Entry(formContato, textvariable=avd, font=('arial', 12))
    avdEntry.grid(row=8, column=1)
    # --------- BOTÃO - ATUALIZAR -------------
    bttn_updatecom = Button(formContato, text="Atualizar", width=50, command=updateData)
    bttn_updatecom.grid(row=9, columnspan=2, pady=10)


# --------- METODO - DELETAR -------------
def deleteData():
    if not tree.selection():
        resultado = msb.showwarning(
            '', 'Por favor, selecione o item na lista.', icon='warning')
    else:
        resultado = msb.askquestion(
            '', 'Tem certeza que deseja deletar?')
        if resultado == 'yes':
            selectItem = tree.focus()
            conteudo = (tree.item(selectItem))
            selectedItem = conteudo['values']
            tree.delete(selectItem)
            conn = sqlite3.connect("")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'alunos' WHERE id = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()


def insertData():
    global newWindow
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    # --------- FRAMES - CADASTRAR -------------
    newWindow = Toplevel()
    newWindow.title("Cadastramento")
    formTitulo = Frame(newWindow)
    formTitulo.pack(side=TOP)
    formContato = Frame(newWindow)
    formContato.pack(side=TOP, pady=10)
    width = 500
    height = 400
    sc_width = newWindow.winfo_screenwidth()
    sc_height = newWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)

    # --------- LABELS - CADASTRAR -------------
    lbl_title = Label(formTitulo, text="cadastramento", font=('arial', 18), bg='blue', width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContato, text='Nome', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(formContato, text='telefone', font=('arial', 12))
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(formContato, text='Idade', font=('arial', 12))
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(formContato, text='Email', font=('arial', 12))
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(formContato, text='Endereco', font=('arial', 12))
    lbl_endereco.grid(row=4, sticky=W)
    lbl_av1 = Label(formContato, text='AV1', font=('arial', 12))
    lbl_av1.grid(row=5, sticky=W)
    lbl_av2 = Label(formContato, text='AV2', font=('arial', 12))
    lbl_av2.grid(row=6, sticky=W)
    lbl_av3 = Label(formContato, text='AV3', font=('arial', 12))
    lbl_av3.grid(row=7, sticky=W)
    lbl_avd = Label(formContato, text='AVD', font=('arial', 12))
    lbl_avd.grid(row=8, sticky=W)

    # --------- ENTRY - CADASTRAR -------------
    nomeEntry = Entry(formContato, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    telefoneEntry = Entry(formContato, textvariable=telefone, font=('arial', 12))
    telefoneEntry.grid(row=1, column=1)
    idadeEntry = Entry(formContato, textvariable=idade, font=('arial', 12))
    idadeEntry.grid(row=2, column=1)
    emailEntry = Entry(formContato, textvariable=email, font=('arial', 12))
    emailEntry.grid(row=3, column=1)
    enderecoEntry = Entry(formContato, textvariable=endereco, font=('arial', 12))
    enderecoEntry.grid(row=4, column=1)
    av1Entry = Entry(formContato, textvariable=av1, font=('arial', 12))
    av1Entry.grid(row=5, column=1)
    av2Entry = Entry(formContato, textvariable=av2, font=('arial', 12))
    av2Entry.grid(row=6, column=1)
    av3Entry = Entry(formContato, textvariable=av3, font=('arial', 12))
    av3Entry.grid(row=7, column=1)
    avdEntry = Entry(formContato, textvariable=avd, font=('arial', 12))
    avdEntry.grid(row=8, column=1)
    # --------- BOTÃO - CADASTRAR -------------
    bttn_submitcom = Button(formContato, text="Cadastrar", width=50, command=submitData)
    bttn_submitcom.grid(row=9, columnspan=2, pady=10)


# ---------------- FRAME PRINCIPAL -------------
top = Frame(janela, width=500, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(janela, width=500, bg='grey')
mid.pack(side=TOP)
midleft = Frame(mid, width=100)
midleft.pack(side=LEFT, pady=10)
midleftPadding = Frame(mid, width=350, bg="grey")
midleftPadding.pack(side=LEFT)
midright = Frame(mid, width=100)
midright.pack(side=RIGHT, pady=10)
bottom = Frame(janela, width=500)
bottom.pack(side=BOTTOM)
tableMargin = Frame(janela, width=500)
tableMargin.pack(side=TOP)

# --------------- LABELS PRINCIPAL --------------
lbl_title = Label(top, text="Sistema de Cadastramento", font=('arial', 18), width=500)
lbl_title.pack(fill=X)

lbl_alterar = Label(bottom, text="Para atualizar o item clique duas vezes.", font=('arial', 12), width=200)
lbl_alterar.pack(fill=X)

# --------------- BUTTONS PRINCIPAL --------------
bttn_add = Button(midleft, text="Cadastrar", bg="green", command=insertData)
bttn_add.pack()
bttn_delete = Button(midright, text="Deletar", bg="Red", command=deleteData)
bttn_delete.pack(side=RIGHT)

# --------------- TREEVIEW PRINCIPAL --------------

ScrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
ScrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=("ID", "Nome", "telefone", "Idade", "Email", "Endereço", "av1", "av2", "av3", "avd"), height=400, selectmode="extended", yscrollcommand=ScrollbarY.set, xscrollcommand = ScrollbarX.set)
ScrollbarY.config(command=tree.yview)
ScrollbarY.pack(side=RIGHT, fill=Y)
ScrollbarX.config(command=tree.xview)
ScrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("telefone", text="telefone", anchor=W)
tree.heading("Idade", text="Idade", anchor=W)
tree.heading("Email", text="Email", anchor=W)
tree.heading("Endereço", text="Endereço", anchor=W)
tree.heading("av1", text="AV1", anchor=W)
tree.heading("av2", text="AV2", anchor=W)
tree.heading("av3", text="AV3", anchor=W)
tree.heading("avd", text="AVD", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=80)
tree.column('#7', stretch=NO, minwidth=0, width=80)
tree.column('#8', stretch=NO, minwidth=0, width=80)
tree.column('#9', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('<Double-Button-1>', onSelect)


if __name__ == '__main__':
    database()
    janela.mainloop()
