import sys, string, time
import com.xhaus.jyson.JysonCodec as json
from com.xebialabs.xlrelease.domain import Task
from com.xebialabs.deployit.plugin.api.reflect import Type
from java.text import SimpleDateFormat

def createPowershellTask(phaseId,title,precondition, propertyMap):

    parenttaskType = Type.valueOf("xlrelease.CustomScriptTask")
    parentTask = parenttaskType.descriptor.newInstance("nonamerequired")
    parentTask.setTitle(title)
    
    childTaskType = Type.valueOf("remoteScript.Powershell")
    childTask = childTaskType.descriptor.newInstance("nonamerequired")
    for item in propertyMap:
        childTask.setProperty(item,propertyMap[item])
    parentTask.setPythonScript(childTask)
    parentTask.setPrecondition(precondition)
    taskApi.addTask(phaseId,parentTask)


def createParallelTask(phaseId,title,precondition,propertyMap):
    paralleltaskType = Type.valueOf("xlrelease.ParallelGroup")
    parallelTask = paralleltaskType.descriptor.newInstance("nonamerequired")
    parallelTask.setTitle(title)
    parallelTask.setPrecondition(precondition)
    taskApi.addTask(phaseId,parallelTask)
    return parallelTask.id


mynewtask = createParallelTask(phase.id,task.title,None,{})
serversSplit = servers.split(",") 
for elem in serversSplit:
    createPowershellTask(mynewtask,elem,None,{'address':elem,'script':script,'remotePath':remotePath,'port':port,'username':username,'password':password,'connectionType':'WINRM_NATIVE','winrmEnableHttps':True})
