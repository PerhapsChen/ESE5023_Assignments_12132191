program SEA

use Declination_angle
use SolarAngleHour

implicit none

real, parameter         :: pii=3.1415926536
real(8)                 :: lat,lon,t,sah,da
integer                 :: m,d
real(8)                 :: aes

lat=22.542883
lon=114.062996
t=10.0+32/60
m=12
d=31

call cal_angle(m,d,da)
call cal_sla(lon,m,d,t,sah)

aes=asin(sin(lat/180*pii)*sin(da/180*pii)+cos(lat/180*pii)*cos(da/180*pii)*cos(sah/180*pii))
aes=aes/pii*180.0

write(*,*) aes

end program SEA
