db=SQLDB('sqlite://mydb.db')

db.define_table('remitentes',
    SQLField('nombre','string',length=50))
    
db.define_table('contactos',
    SQLField('nombre','string',length=50),
    SQLField('email','string',length=50),
    SQLField('remitentesant',db.remitentes))

db.define_table('info',
    SQLField('texto','string',length=10000,notnull=True),
    SQLField('selector','integer'))
    
db.define_table('info2',
    SQLField('texto','string',length=30000,notnull=True),
    SQLField('longitud'))
    
db.define_table('info4',
    SQLField('texto','string',length=30000,notnull=True),
    SQLField('longitud'))
    
db.define_table('persona',
    SQLField('nombre'),
    SQLField('nacimiento','date'))
    
db.define_table('perro',
    SQLField('nombre'),
    SQLField('nacimiento','date'),
    SQLField('amo_id',db.persona))

db.perro.amo_id.requires=IS_IN_DB(db,'persona.id','persona.nombre')
