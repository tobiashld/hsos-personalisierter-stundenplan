from distutils.command.clean import clean
from ics import Calendar,Event
from datetime import datetime
import requests

##########################################################################################################################################################
###############        ausfüllen            ##############################################################################################################
##########################################################################################################################################################

# ohne die letzte Zahl, falls vorhanden. 20DWF2 wird zu 20DWF
studiengruppe = '20DWF'
semester = '5'

# EBU = E-Business
# IMA = Informationsmanagement
# IBM = IT-Beratung und Marketing
# ITI = IT-Infrastrukturmanagement
# PDI = Produktionsinformatik
schwerpunkt = 'IMA'

# Veranstaltungsname im Stundenplan
gewaehlteModule = [
    'Programmierprojekt',
    'Infomationsmanangement / ERP-Systeme A',
    'Projektmanagement',
    'Networking: Networking Basics',
    'Projektierung von IuK-Systemen',
    'Verteilte Systeme'
    ]

##########################################################################################################################################################
###############   nichts mehr ausfüllen     ##############################################################################################################
##########################################################################################################################################################



url = 'https://sked.lin.hs-osnabrueck.de/sked/grp/'+studiengruppe+'-'+schwerpunkt+'-'+semester+'.ics'
dirtyCalendar = Calendar()
cleanCalendar = Calendar()


def doYourThing():
    req = requests.get(url)
    dirtyCalendar = Calendar(req.text)
    cleanCalendar = dirtyCalendar.clone()
    cleanCalendar.events.clear()

    for event in dirtyCalendar.events:
        if str(event.name.split("'")[0]) in gewaehlteModule:
            cleanCalendar.events.add(event)
        
    print(cleanCalendar)

    with open('my.ics', 'w') as f:
        f.writelines(cleanCalendar.serialize_iter())
    

    


doYourThing()