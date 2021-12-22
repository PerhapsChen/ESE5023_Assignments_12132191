program SEA

use Declination_angle
use SolarAngleHour

implicit none

real, parameter         :: pii=3.1415926536
real(8)                 :: lat,lon,t,sah,da
integer                 :: m,d
real(8)                 :: aes

lat=32.22
lon=1.0
t=10.0
m=3
d=3

call cal_angle(m,d,da)
call cal_sla(lon,m,d,t,sah)

aes=asin(sin(lat/180*pii)*sin(da/180*pii)+cos(lat/180*pii)*cos(da/180*pii)*cos(sah/180*pii))
aes=aes/pii*180.0

write(*,*) aes

end program SEA
