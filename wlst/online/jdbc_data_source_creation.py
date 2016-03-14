"""
This script configures a JDBC data source as a System Module and deploys it
to the server
"""
connect("weblogic","welcome1")
edit()

# Change these names as necessary
dsname="myJDBCDataSource"
server="examplesServer"
cd("Servers/"+server)
target=cmo
cd("../..")

startEdit()
# start creation
print 'Creating JDBCSystemResource with name '+dsname
jdbcSR = create(dsname,"JDBCSystemResource")
theJDBCResource = jdbcSR.getJDBCResource()
theJDBCResource.setName("myJDBCDataSource")

connectionPoolParams = theJDBCResource.getJDBCConnectionPoolParams()
connectionPoolParams.setConnectionReserveTimeoutSeconds(25)
connectionPoolParams.setMaxCapacity(100)
connectionPoolParams.setTestTableName("SYSTABLES")

dsParams = theJDBCResource.getJDBCDataSourceParams()
dsParams.addJNDIName("ds.myJDBCDataSource")

driverParams = theJDBCResource.getJDBCDriverParams()
driverParams.setUrl("jdbc:derby://localhost:1527/examples;create=true")
driverParams.setDriverName("org.apache.derby.jdbc.ClientXADataSource")
# driverParams.setUrl("jdbc:oracle:thin:@my-oracle-server:my-oracle-server-port:my-oracle-sid")
# driverParams.setDriverName("oracle.jdbc.driver.OracleDriver")

driverParams.setPassword("examples")
# driverParams.setLoginDelaySeconds(60)
driverProperties = driverParams.getProperties()

proper = driverProperties.createProperty("user")
#proper.setName("user")
proper.setValue("examples")

proper1 = driverProperties.createProperty("DatabaseName")
#proper1.setName("DatabaseName")
proper1.setValue("examples")

jdbcSR.addTarget(target)

save()
activate(block="true")

print 'Done configuring the data source'

