from zanox.client import Client
import json
import config

c = Client(connectid=config.CONNECTID,
           secretkey=config.SECRETKEY)

programs = json.loads(c.getProgramApplications())
for program in programs['programApplicationItems']['programApplicationItem']:
    incentives = json.loads(c.searchIncentives(program=program['program']['@id']))
    print "%d incentives found for %s" % (incentives['total'], program['program']['$'])

