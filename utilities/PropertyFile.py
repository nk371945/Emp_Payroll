from jproperties import Properties

credentials = Properties()

with open('credentials.properties', 'rb') as read_prop:
    credentials.load(read_prop)


def getValues(key):
    global value
    if key == 'excelFilePath':
        value = credentials.get('excelFilePath').data
    elif key == 'login_test_data':
        value = credentials.get('login_test_data').data
    elif key == 'department':
        value = credentials.get('department').data
    elif key == 'employee':
        value = credentials.get('employee').data
    elif key == 'payroll':
        value = credentials.get('payroll').data
    elif key == 'view_payslip':
        value = credentials.get('view_payslip').data
    elif key == 'test_report_file':
        value = credentials.get('test_report_file').data
    elif key == 'url':
        value = credentials.get('url').data
    elif key == 'valid_login_email':
        value = credentials.get('valid_login_email').data
    elif key == 'valid_login_password':
        value = credentials.get('valid_login_password').data
    elif key == 'name':
        value = credentials.get('name').data
    elif key == 'report_url':
        value = credentials.get('report_url').data
    elif key == 'sender_mail':
        value = credentials.get('sender_mail').data
    elif key == 'receiver_mail':
        value = credentials.get('receiver_mail').data
    elif key == 'subject':
        value = credentials.get('subject').data
    elif key == 'port':
        value = credentials.get('port').data
    elif key == 'server':
        value = credentials.get('server').data
    elif key == 'username':
        value = credentials.get('username').data
    elif key == 'password':
        value = credentials.get('password').data
    elif key == 'text':
        value = credentials.get('text').data
    elif key == 'pre_file':
        value = credentials.get('pre_file').data
    elif key == 'post_file':
        value = credentials.get('post_file').data
    return value