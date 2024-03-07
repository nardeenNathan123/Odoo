{
    'name': 'Hospitals System',
    'version': '1.0',
    'summary': 'hospital',
    'description': 'hospital',
    'author': 'nardeen',
    'category': 'hospital',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/department_view.xml',
        'views/doctor_view.xml',
    ],
    'application': True,
}
