#!/bin/sh

remove_audio()
{
    rmmod hi3518_adec
    rmmod hi3518_aenc
    rmmod hi3518_ao
    rmmod hi3518_ai
    rmmod hi3518_sio
    rmmod acodec
    rmmod hidmac
    echo "remove audio"
}

remove_sns()
{
    rmmod hi_i2c &> /dev/null
    rmmod ssp &> /dev/null
    rmmod ssp_sony &> /dev/null
}


remove_ko()
{
    remove_audio
    remove_sns
    rmmod sha_204
    rmmod wdt
    rmmod hirtc
    rmmod fos_ptz
    rmmod ssp_ad9020
    rmmod adc
	
    rmmod sil9024 &> /dev/null
    rmmod hi_i2c.ko &> /dev/null
    rmmod pwm
    rmmod gpioi2c_ex
    rmmod higpio

    #rmmod hi3518_ive
    rmmod hi3518_vda

    rmmod hi3518_region
    rmmod hi3518_rc
    rmmod hi3518_jpege
    rmmod hi3518_h264e
    rmmod hi3518_chnl
    rmmod hi3518_group
    rmmod hi3518_venc
  
    #rmmod hifb
    #rmmod hi3518_vou
    rmmod hi3518_vpss
    #rmmod hi3518_isp
    rmmod hi3518_viu

    rmmod hi3518_dsu
    rmmod hi3518_tde
    rmmod hiuser 
    rmmod hi3518_sys
    rmmod hi3518_base
    rmmod mmz
}

remove_ko
