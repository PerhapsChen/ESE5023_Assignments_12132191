program Test2

use SolarAngleHour

implicit none

real(8)         :: t,lon,h
integer         :: m,d

t=15.5
lon=-118.24
m=11
d=24

call cal_sla(lon,m,d,t,h)

write(*,*) h

end program Test2
