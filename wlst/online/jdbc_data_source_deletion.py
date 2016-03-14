print 'starting the script ....'
username = 'weblogic'
password = 'welcome1'

connect(username,password,'t3://localhost:7001')

edit()
startEdit()

delete('myJDBCDataSource','JDBCSystemResource')

save()
activate(block="true")
