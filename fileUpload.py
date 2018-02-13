import glob, time
from slacker import Slacker
slack = Slacker('token-from-slack') ## get token from slack and add here to upload file;
from datetime import date
today = date.today().strftime('%Y-%m-%d')
todayfilenamepattern = "filename_"+today ## filename with date name
slackfilename=todayfilenamepattern+'.csv'
var1 = glob.glob('/mydir/'+todayfilenamepattern+'*')
if var1:
        print var1[0]
        slack.files.upload(var1[0],None,'.csv',slackfilename,slackfilename, None,'#channelName') ##put correct channel name
else:
        print "File Doesn't exists"
        slack.chat.post_message('#channelName', 'File Not available today!', 'piyush')
