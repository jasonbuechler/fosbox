# Foscam Cloud

Foscam IP cameras offer a "Cloud Plan" for saving camera recordings to "the cloud". 
![cloud recording plan interface](cloud-recording-plan.png)	

But some recent additions to their SDK for CGI gateway interface reveals some tantalizing info that seems like it allows us to see and potentially tinker under the hood of the cloud-recording functionality: namely that apparently Dropbox is "the cloud". 
![cloud verbs from cgi sdk](cgi-cloud-configs.png)	

It seems very much like the standard dropbox API is being used, which is interesting. I have my own dropbox. Maybe I don't want to pay Foscam's fees!

Note that the data output from the 'get' function has significantly more parts than can be 'set', at least according to the published documentation.


![actual output from getconfig](example-getconfig.png)	

![firmware package decrypted and expanded](firmware-upgrade-decrypted.png)	

![squashfs files are nonstandard](sqfs-files-nonstandard.png)
