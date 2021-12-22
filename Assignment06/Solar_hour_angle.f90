module SolarAngleHour

implicit none

real, parameter         :: pi=3.1415926536

contains

  subroutine cal_sla(lon,m,d,t,sah)
 
  implicit none  
 
  integer,intent(in)            :: m, d
  real(8),intent(in)            :: lon, t
  real(8),intent(out)           :: sah
  integer                       :: doy
  real(8)                       :: offset, eot, gam 
  doy=(m-1)*30+d
  gam=2*pi/365*(doy-1+(t-12)/24)
  eot=229.18*(0.000075+0.001868*cos(gam)-0.032077*sin(gam)-0.014615*cos(2*gam)-0.040849*sin(2*gam))
  offset=eot+MOD(lon,15.0)
  sah=15*(t-12)+offset/60

  end subroutine cal_sla

end module SolarAngleHour

