"""
This script starts an edit session, creates two different JMS Servers, 
targets the jms servers to the server WLST is connected to and creates
jms topics, jms queues and jms templates in a JMS System module. The 
jms queues and topics are targeted using sub-deployments. 
"""

import sys
from java.lang import System


print "Starting the script ..."
connect('weblogic','welcome1','t3://localhost:7001')
edit()
startEdit()

servermb=getMBean("Servers/examplesServer")
if servermb is None:
    print 'Value is Null'

else:
    jmsserver1mb = create('MyJMSServer1','JMSServer')
    jmsserver1mb.addTarget(servermb)
    jmsserver2mb = create('MyJMSServer2','JMSServer')
    jmsserver2mb.addTarget(servermb)

    jmsMySystemResource = create("myJmsSystemResource","JMSSystemResource")
    jmsMySystemResource.addTarget(servermb)
    
    subDep1mb = jmsMySystemResource.createSubDeployment('DeployToJMSServer1')
    subDep1mb.addTarget(jmsserver1mb)
    subDep2mb = jmsMySystemResource.createSubDeployment('DeployToJMSServer2')
    subDep2mb.addTarget(jmsserver2mb)
    
    theJMSResource = jmsMySystemResource.getJMSResource()
    
    connfact1 = theJMSResource.createConnectionFactory('MyCF1')
    connfact1.setJNDIName('jms.MyCF1')
    connfact1.setSubDeploymentName('DeployToJMSServer1')
    connfact2 = theJMSResource.createConnectionFactory('MyCF2')
    connfact2.setJNDIName('jms.MyCF2')
    connfact2.setSubDeploymentName('DeployToJMSServer2')
    
    print "Creating MyQueue1..."
    jmsqueue1 = theJMSResource.createQueue('MyQueue1')
    jmsqueue1.setJNDIName('jms.MyJMSQueue1')
    jmsqueue1.setSubDeploymentName('DeployToJMSServer1')
    
    print "Creating MyQueue2..."
    jmsqueue2 = theJMSResource.createQueue('MyQueue2')
    jmsqueue2.setJNDIName('jms.MyJMSQueue2')
    jmsqueue2.setSubDeploymentName('DeployToJMSServer2')
    
    print "Creating MyTopic1..."
    jmstopic1 = theJMSResource.createTopic("MyTopic1")
    jmstopic1.setJNDIName('jms.MyJMSTopic1')
    jmstopic1.setSubDeploymentName('DeployToJMSServer1')
    
    print "Creating MyTopic2..."
    jmstopic2 = theJMSResource.createTopic("MyTopic2")
    jmstopic2.setJNDIName('jms.MyJMSTopic2')
    jmstopic2.setSubDeploymentName('DeployToJMSServer2')
    
    print "Creating MyJMSTemplate..."
    jmstemplate = theJMSResource.createTemplate('MyJMSTemplate')
    jmstemplate.setMaximumMessageSize(20)    
    
try:
    save()
    activate(block="true")
    print "script returns SUCCESS"   
except:
    print "Error while trying to save and/or activate!!!"
    dumpStack()