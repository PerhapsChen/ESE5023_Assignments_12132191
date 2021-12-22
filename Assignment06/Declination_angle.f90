module Declination_angle

implicit none
!here I consider that there are 30 days in each month.

real, parameter         :: pi=3.1415926536

contains

  subroutine cal_angle(m,d,da)
  
  implicit none

  integer,intent(in)            :: m, d
  real(8),intent(out)           :: da
  integer                       ::doy

  doy=(m-1)*30+d
  da=asin(sin(-23.44/180*pi)*cos(((360/365.24)*(doy+10)+360/pi*0.0167*sin(360/365.24*(doy-2)))/180*pi))  
  da=da/pi*180

  end subroutine cal_angle
end module Declination_angle
