# -*- coding: utf-8 -*-

db.define_table('valores',
    Field('gremio',db.gremios, default=request.vars.id),
    Field('nombre'),
    Field('fecha'),
    Field('pago',requires=IS_IN_SET(['Permanente', 'Periodico'])),
    Field('timporte',label='Tipo de importe', requires=IS_IN_SET(['Porcentual','Monto fijo'])),
    Field('valor')
    )

db.define_table('convenios',
    Field('empleador',db.empleadores, default=request.vars.id),
    Field('convenio', db.gremios)
    )

#db.valores.pago.widget=SQLFORM.widgets.radio.widget
