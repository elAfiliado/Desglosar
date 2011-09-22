# coding: utf8
# intente algo como
def entrada():
    form=SQLFORM(db.info)
    if form.accepts(request.vars,session): pass
    
    txt=db.info[12].texto
    c=0
    for i in range(len(txt)): c=c+1
    response.write('el total de c es '+str(c)+'. ')
   
    import re
    pattern=re.compile(".*a[0-5].*")
    for i in range(len(txt)):
    ## encontrar el primer email
        s=txt[:i]
        if pattern.search(s):
            response.write('Se ha encontrado a1 o a2 o a3 \r o a4 o a5 o a0\n')
        elif not pattern.search(s) and i==(len(txt)-1):
            response.write('Nanai contrai')
        
    response.write('La len(txt) es '+str(len(txt))+' y la i es '+str(i))
    response.write('*********************')

    cont=0
    for i in xrange(0,4):
        cont=cont+1
        response.write('Para el valor i '+str(i)+' el contador se pone a '+str(cont))
    response.write(' y el resultado final es de i '+str(i)+' el contador se pone a '+str(cont)+'. ')
    i=0
    while i<len(txt):
        response.write(txt[i]+'-')
        i=i+1
    response.write('. La len(txt) es de '+str(len(txt))+' y la i se ha quedado en '+str(i))
    db.info.insert(texto="Vete a Cascarla")
    
    return dict(form=form)
