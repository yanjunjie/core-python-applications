# This example script corresponds to the cluster_creation.py script:
# * connects WLST to the Admin Examples Server
# * starts an edit session
# * For each cluster created in cluster_creation.py, it deletes the
# * managed servers and the migratabletargets.
# * Lastly, it deletes the clusters.

print 'starting the script ....'
username = 'weblogic'
password = 'welcome1'
clusters = 'cluster1','cluster2'
ms1 = {'managed1':7701,'managed2':7702,'managed3':7703, 'managed4':7704, 'managed5':7705}
ms2 = {'managed6':7706,'managed7':7707,'managed8':7708, 'managed9':7709, 'managed10':7710}

connect(username,password,'t3://localhost:7001')

edit()
startEdit()
s = " (migratable)"

for m, lp in ms1.items():
  print 'deleting managed server '+m
  serverMBean = getMBean("Servers/"+m)
  serverMBean.setCluster(None)
  managedServer = delete(m,'Server')

for m1, lp1 in ms2.items():
  print 'deleting managed server '+m1
  serverMBean = getMBean("Servers/"+m1)
  serverMBean.setCluster(None)
  managedServer = delete(m1,'Server')

for c in clusters:
  print 'deleting cluster '+c
  clu = delete(c,'Cluster')  
  

save()
activate(block="true")
print 'Saved Changes ...'

print 'End of script ...'

disconnect()
