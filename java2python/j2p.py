#!/usr/bin/python3

import sys
import re

def pasaj2p(cadena):
    comandos=[  ["\.toUpperCase\(\)",".upper()"],               # cadenas
                ["\.trim\(\)", ".strip()"],
                ["\.equals\((.*)\)",r"==\1"],
                ["\.substring\((.*),(.*)\)",r"[\1:\2]"],
                ["\.charAt\((.[^\)]*)\)",r"[\1]"],
                ["([^\s]+)\.contains\(([^\)]+)\)",r"\2 in \1"],
                ["String.valueOf\(","str("],
                [r"(\w+)\.length\(\)",r"len(\1)"],              # conversiones literales
                ["(=\s*)true",r"\1True"],
                ["(\s+)true;", r"\1True"],
                ["(=\s*)false",r"\1False"],
                ["(\s+)false;",r"\1False"],
                ["s\.nextLine","input"],
                ["System\.console\(\)\.readLine\(\)","input()"],
                ["Double\.parseDouble","float"],
                ["Integer\.parseInt","int"],
                ["Integer\.toString","str"],
                ["Integer\.MAX_VALUE","sys.maxsize"],
                ["Integer\.MIN_VALUE","(-sys.maxsize-1)"],
                ["s\.nextInt\(\)","int(input())"],
                ["s\.nextDouble\(\)","float(input())"],
                ["Math\.abs","abs"],
                ["Math\.random\(","random.random("],
                ["Math\.","math."],
                ["Thread.sleep\((.+\))(.*)",r"time.sleep(0.001*\1\2 #Ojo: de ms a seg"],
                ["for\s*\((.*)\)\s+{",r"for \1:","crea_for"],   # for
                ["do {","while True:"],                         # do..while
                ["} while\s*(\(.*\))",r"    if not \1: break"],
                ["System\.out\.println","print"],                 # impresión
                ["System\.out\.print\((.*)\)",r'print(\1,end="")'],
                ['System\.out\.printf(.*"),\s*(.*)',r'print\1%(\2,end="")'],
                ["if\s+\((.*)\)\s+{",r"if \1:"],               # if
                ["} else {","else:"],
                ["} else if","elif"],
                ["&&","and"],                                  # operadores
                ["\|\|","or"],
                ["(\w+)\+\+",r"\1 += 1"],
                ["(\w+)\-\-", r"\1 -= 1"],
                ["(\s*while\s*)\((.*)\)\s+{",r"\1\2:"],
                ["=(\s*)new ",r"=\1"],                         # POO
                ["this\.","self."]
        ]
    linea=cadena
    # quitamos 4 espacios iniciales
    linea = re.compile("^ {4}").sub("",linea)
    # comentarios de PSeInt
    linea = re.compile("^  //").sub("#",linea)
    # comentarios normales
    linea = re.compile("//").sub("#",linea)
    # Comentarios /* ... */
    linea = re.compile("/\*\s*").sub('"""\n',linea)
    linea = re.compile("\s*\*/").sub('"""\n',linea)
    # ; final
    linea = re.compile(";(\s+#.*)?$").sub(r"\1",linea)
    # dos espacios de sangría por cuatro
    blancos = len(linea)-len(linea.lstrip(" "))
    linea = " "*2*blancos + linea.lstrip(" ")
    # comandos
    for comando in comandos:
        linea = re.compile(comando[0]).sub(comando[1],linea)
        # si hay tercer elemento es que hay que evaluar una función
        if len(comando)>2:
            f=eval(comando[2])
            linea = f(linea)
    # impresión: pasar a cadenas f
    #linea = re.compile(r'(^\s*print\(.*)(".*)"\+(\w+)([\)|\+"])').sub(r'\1f\2{\3}"\4 #Ojo!!! ¿cadena f?',linea)
    patron1 = re.compile('"\s*\+\s*(\w+)\s*\+\s*"') # expresión enmedio
    patron2 = re.compile('"\s*\+\s*(\w+)([,end=""]?\))') # expresión al final   
    patron3 = re.compile('print\((\w+)\+"')  # expresión al principio: ejemplo-> print(num+"...
    if patron1.search(linea) or patron2.search(linea) or patron2.search(linea):
        cadena_original = linea.strip()
        linea = patron1.sub(r"{\1}",linea)      #ponemos llaves
        linea = patron2.sub(r'{\1}"\2',linea)
        linea = patron3.sub(r'print(f"{\1}',linea)
        linea = re.compile('print\(([^"]*)"').sub(r'print(\1f"',linea)
        linea = linea[:-1] + " #Original: "+cadena_original+"\n"    # controlamos salto de línea
    return linea

def crea_for(linea):
    partes = linea.split(";")   # dividimos for en tres partes
    # inicialización
    patron1=re.compile("for\s+(int\s+)?(\w+)\s*=(.+)")
    if patron1.search(partes[0]):    # tiene formato de <variable_control>=<valor inicial>
        control = patron1.sub(r"\2",partes[0]).strip()
        v_ini = patron1.sub(r"\3",partes[0]).strip()
    else:
        return linea
    # condición
    patron2=re.compile("(\w+)\s*([<>][=]*)\s*(.+)")
    if patron2.search(partes[1]):   # tiene formato de <variable_control><op><expresión>
        c,op,fin=patron2.search(partes[1]).groups()
        if control==c and op!="==": # coincide la variable de control con la inicial y operador válido
            if len(op)>1:   # hay que sumar o restar 1
                inc = "+1" if op[0]=="<" else "-1"
                if fin.strip().isdecimal():
                    fin = str(eval(fin+inc))
                else:
                    fin += inc
        else:
            return linea
    else:
        return linea
    # incremento
    patron3=re.compile("(\w+)\s*([+-][+-=])\s*(.*):")
    if patron3.search(partes[2]):   # tiene formato de <variable_control><op><expresión>
        c,op,inc=patron3.search(partes[2]).groups()
        if control==c and op in ["++","--","+=","-="]:
            if op=="++":
                inc="1"
            elif op=="--":
                inc="-1"
            elif op=="-=":
                inc="-"+inc
        else:
            return linea
    else:
        return linea
    # si llegamos aquí es que se puede convertir a for de Python
    l = "for "+control+" in range("
    if inc=="1":
        if v_ini!="0":
            l += v_ini+","
        l += fin+"):"
    else:
        l += v_ini+","+fin+","+inc+"):"
    l = linea.split("for")[0]+l    # espacios a la izquierda de for
    return l + " # for original:"+linea.split("for")[1][:-1]+"\n"

def es_innecesaria(cadena):
    a_borrar=[  "import",
                "\s*Scanner s",
                "\s*public static void main",
                "\s*public class",
                "^\s*}\s*$"]
    exp_reg="|".join(a_borrar)
    return re.match(exp_reg,cadena)

# ---------
# Principal
#----------
hay_main = False # nos servirá para ver si es programa o clase
if len(sys.argv)<2:
    print("Falta fichero java")
    sys.exit(1)

# cargamos ficheros
fjava=open(sys.argv[1], 'r')
programa=fjava.readlines()
fjava.close()

# borramos líneas
i=0
while i<len(programa):
    if es_innecesaria(programa[i]):
        if not hay_main: # antes de borrar
            hay_main = "public static void main" in programa[i]
        programa.pop(i)
        if i<len(programa) and not programa[i].strip(): # línea vacía, borramos también
            programa.pop(i)
    else:
        i+=1

# sustituimos
for i in range(len(programa)):
    programa[i]=pasaj2p(programa[i])

# buscamos bloques print...input
i=0
while i<len(programa)-1:
    if re.match("^\s*print\(",programa[i]) and re.search("input\(\)",programa[i+1]):
        cadena = re.match("^\s*print\((.*)[\)$|\)\s+#]",programa[i]).group(1)
        programa.pop(i) # quitamos print
        programa[i] = re.compile("input\(\)").sub("input("+cadena,programa[i])
        if re.search(',end=""',programa[i]):
            programa[i] = re.compile(',end=""').sub("",programa[i]) # viene de System.out.print
        else:
            programa[i] = programa[i][:-1]+" # Ojo!!!! ¿salto de línea previo?\n" # viene de System.out.println
    i+=1

# buscamos módulos a importar
modulos=["math","random","sys","time"]
inserta=set()
for linea in programa:
    for m in modulos:
        if m+"." in linea:
            inserta.add("import "+m+"\n")

# añadimos módulos y si es una clase añadimos "class..."
if len(inserta)>0 or (not hay_main):
    i=0
    # buscamos después de comentarios
    if programa[0][:3]=="'''":  # buscamos cierre comentario
        i=1
        while i<len(programa) and not "'''" in programa[i]:
            i+=1
        i+=1
    while i<len(programa) and programa[i][0]=="#":
            i+=1
    # insertamos
    clase = "" if hay_main else "class "+sys.argv[1].replace(".java",":") # la clase se llama como el fichero
    programa = programa[:i]+list(inserta)+["\n"+clase]+programa[i:]

# buscamos funciones
i = 0
inserta_espacios = False
es_comentario = False
patron = re.compile("\s+public\s+static\s+(.+\(.*\))\s*{")
comentario = re.compile("^\s*\"{3}|'{3}")
for i in range(len(programa)):
    if patron.search(programa[i]):  # función
        programa[i] = patron.sub(r"def \1:",programa[i])
        inserta_espacios = True
    elif comentario.search(programa[i]):
        es_comentario = not es_comentario
    elif inserta_espacios and len(programa[i].strip()):
        programa[i] = "    "+programa[i]

# escribimos
fpython=open(sys.argv[1].replace(".java",".py"), 'w')
fpython.writelines(programa)
fpython.close()
