def entrada_bien():
    form=SQLFORM(db.info4)
    if form.accepts(request.vars,session):pass
    
    return dict(form=form)
   
def borrardb():
    db.contactos.truncate()
    db.info4.truncate()
    
    return dict(cad='Cagada pastoret')
    
def relaciones():
           
    return dict(cad='Que si')
    
def entrada_borrar():
    form=SQLFORM(db.info4)
    return dict(form=form)
