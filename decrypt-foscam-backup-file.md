foscam C1 backup file (.bin file)

```
openssl enc -d -aes-128-cbc -in foscam-configuration-from102.bin -out del.bin -md md5 -k BpP+2R9*Q
```

AKA the symmetric decryption key is 
- "BpP+2R9*Q"
- aes-128-cbc
- md5 digest

Decrypts to a gzip archive with the contents...

```
 Directory of C:\Users\jason\Downloads\openssl\del\del~

05/20/2019  06:44 PM    <DIR>          .
05/20/2019  06:44 PM    <DIR>          ..
12/31/2009  05:04 PM               360 AllResetConfig.xml
05/20/2019  05:28 PM             4,160 AudioCodecConfig.xml
12/31/2009  05:04 PM               652 BaiduRtmpConfig.xml
12/31/2009  05:04 PM               337 CGIConfig.xml
12/31/2009  05:04 PM               416 CloudConfig.xml
05/20/2019  05:33 PM             2,497 configs.md5
12/31/2009  05:04 PM               347 DDNSConfig.xml
12/31/1969  05:01 PM               296 DDNSFactoryDataConfig.xml
05/04/2016  05:30 PM               876 DefProductConfig.xml
12/31/2009  05:04 PM               318 DevP2PInfoConfig.xml
06/08/2018  09:44 AM               441 DevVerConfig.xml
12/31/2009  05:04 PM               710 Ds18b20AlarmConfig.xml
12/31/2009  05:04 PM               458 Firewall.xml
12/31/2009  05:04 PM               336 FtpConfig.bin
12/31/1969  05:00 PM                 6 FtpPortConfig.xml
12/31/2009  05:04 PM               584 HumidityAlarmConfig.xml
12/31/1969  05:00 PM               953 HWManageConfig.xml
12/31/2009  05:04 PM               546 IOAlarmConfig.xml
05/10/2019  05:20 PM               280 IPCamInfoConfig.xml
05/10/2019  05:24 PM               951 LEDConfig.xml
12/31/2009  05:04 PM             2,210 MultiDevConfig.xml
04/05/2019  11:03 PM             1,136 NetworkConfig.bin
06/11/2015  02:36 AM             1,760 NVT_config.xml
05/20/2019  05:28 PM               278 OneKeyAlarmConfig.xml
01/13/2019  09:15 AM               262 OnvifAgentConfig.xml
12/31/2009  05:39 PM             1,250 OsdConfig.xml
12/31/2009  05:04 PM               367 P2PConfig.xml
06/08/2018  09:44 AM               366 PatchVerConfig.xml
12/31/2009  05:04 PM               263 PlayConfig.xml
12/31/2009  05:04 PM             1,863 ProcessListConfig.xml
12/31/2009  05:58 PM               878 ProductConfig.xml
12/31/2009  05:04 PM             9,323 PTZConfig.xml
04/05/2019  11:02 PM             1,136 PushConfig.xml
05/10/2019  05:37 PM             1,120 RecordConfig.bin
12/31/1969  05:00 PM               250 RemoteControlConfig.xml
05/20/2019  06:44 PM    <SYMLINK>      Rom.dat [C:\Users\jason\Downloads\openssl\del\del~\mnt\para\etc\Rom.dat]
12/31/2009  05:04 PM               352 ShareDirConfig.bin
12/31/2009  05:04 PM               480 SMTPConfig.bin
04/05/2019  11:02 PM               589 SoftApConfig.xml
05/20/2019  07:10 AM               701 SystemTimeConfig.xml
12/31/2009  05:04 PM               628 TemperatureAlarmConfig.xml
12/31/2009  05:04 PM               280 UDTMediaServerConfig.xml
12/31/2009  05:04 PM               246 UPnPConfig.xml
04/05/2019  11:02 PM             1,440 UserAccountConfig.bin
03/16/2018  08:58 AM               472 UserGuideConfig.xml
05/20/2019  05:27 PM             4,400 VideoCodecConfig.xml
04/05/2019  11:03 PM                78 webserver.conf
12/31/2009  05:04 PM               252 ZoomConfig.xml
```
