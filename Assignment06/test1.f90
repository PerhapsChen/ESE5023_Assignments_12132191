program TestProgram

use Declination_angle

implicit none

real(8)                 ::angle
integer                 ::m, d

m=12
d=22

call cal_angle(m,d,angle)

write(*,*) angle

end program TestProgram
