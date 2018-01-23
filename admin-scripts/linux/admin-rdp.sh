#!/bin/bash
# created by elrey

lab=$(ifconfig | grep broadcast | cut -d ' ' -f 10 | cut -d '.' -f 1)
if [[ $lab -eq 172 ]] ; then
	xfreerdp /f /v:172.16.1.30 /d:UNCC-49SD /u:rodriguez.adm /clipboard /p:$(zenity --password)
else
	xfreerdp /f /v:ccdc-pa.uncc.edu /d:UNCC-49SD /u:rodriguez.adm /clipboard /p:$(zenity --password)
fi
