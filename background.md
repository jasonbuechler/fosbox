# Foscam Cloud

Foscam IP cameras offer a "Cloud Plan" for saving camera recordings to "the cloud". 

![cloud recording plan interface](cloud-recording-plan.png)	


But some recent additions to their SDK for CGI gateway interface reveals some tantalizing info that seems like it allows us to see and potentially tinker under the hood of the cloud-recording functionality: namely that apparently Dropbox is "the cloud". (Note that the data output from the 'get' function has significantly more parts than can be 'set', at least according to the published documentation.)

![cloud verbs from cgi sdk](cgi-cloud-configs.png)	

![other cloud verbs from cgi sdk](cgi-cloud-other.png)


Here's the interesting output from a run of `getCloudConfig` 

![actual output from getconfig](example-getconfig.png)	


It seems very much like the standard dropbox API is being used (with oauth2 code), which makes my mouth water. I have my own dropbox. Maybe I don't want to pay Foscam's fees?  Logically, [according to dropbox](https://blogs.dropbox.com/developers/2013/07/using-oauth-2-0-with-the-core-api/) the client_id parameter is Foscam's API app key. I tried the most obvious next step, and attempted a `...cmd=setCloudConfig&authAddr=CUSTOM_ADDR...` but found it wasn't changed after another `getCloudConfig`.


# Overwriting embedded resources

An undocumented set-API-key function would have been so so nice. But apparently we need to look elsewhere under much heavier rocks to find a solution. 

The camera has no ssh/telnet running, but it does have a semi-secret FTP server. Unfortunately, they were smart enough to 

Maybe if nothing else, I could do something like rewrite all outgoing dropbox urls with that client_id to my own at the router, and do some tricky https verification juggling with Burp. But for now, I'm assuming that client_id is hardcoded in the firmware files somewhere... and maybe it's as simple as changing the value and "upgrading" the firmware?  

