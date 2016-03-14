# This example script connects WLST to the Admin Examples Server
# * starts an edit session
# * removes a JMS system resource module.
import sys
from java.lang import System
    
print 'starting the script ....'
connect('weblogic','welcome1','t3://localhost:7001')
edit()
startEdit()
jmsMySystemResource = delete("myJmsSystemResource","JMSSystemResource") 
jmsMyServer1 = delete("MyJMSServer1","JMSServer") 
jmsMyServer2 = delete("MyJMSServer2","JMSServer")
save()
activate(block="true")
print 'System Resource removed ...'
disconnect()