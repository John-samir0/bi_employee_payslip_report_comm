# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'HR Employee Payslip Reports(PDF/Excel) Community Edition',
    'version': '17.0.0.0',
    'category': 'Human Resources',
    'summary': 'Employee Multiple Payslip Report print employee payslip report hr payslip report employee pay slip report mass employee payslip report print payslip report print employee payroll report print pay slip report print payslip excel report payslip xls report',
    'description': """ User can print multiple employee payslip report with salary computation group by with salary rule category and salary rules in both pdf and xls file format at a one click. """,
    'author': 'BROWSEINFO',
    'website': 'https://www.browseinfo.com/demo-request?app=bi_employee_payslip_report_comm&version=17&edition=Community',
    "price": 15,
    "currency": 'EUR',
    'depends': ['hr_payroll_community'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/payslip_report_wizard.xml',
        'report/employee_payslip_report.xml',
        'report/payslip_report_template.xml',
    ],
    "auto_install": False,
    "installable": True,
    "license": 'OPL-1',
    "live_test_url": 'https://www.browseinfo.com/demo-request?app=bi_employee_payslip_report_comm&version=17&edition=Community',
    "images": ["static/description/Banner.gif"],

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
