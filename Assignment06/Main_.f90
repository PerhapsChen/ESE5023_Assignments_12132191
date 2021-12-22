program MainReadM

implicit none

integer                                 :: u1, u2, mc, mr, nc, nr, i, j
real(8), dimension(:,:),allocatable     :: M, N
real(8), dimension(4,4)                 :: MN

u1=50
u2=51
mc=3
mr=4
nc=4
nr=3

open(unit=u1,file='M.dat',status='old')
open(unit=u2,file='N.dat',status='old')

allocate(M(mr,mc))
allocate(N(nr,nc))

do i=1,mr
  read(u1,*) M(i,:)
enddo

do i=1,nr
  read(u2,*) N(i,:)
enddo

close(u1)
close(u2)

do i=1,mr
  write(*,*) "Line ",i,":",M(i,:)
enddo

do i=1,nr
  write(*,*) "Line ",i,":",N(i,:)
enddo

call Matrix_multip(M,N,MN)

do i=1,4
  write(*,*) "Line ",i,":",MN(i,:)
enddo

open(unit=u1,file='new1.dat',status='replace')
do i=1,4
  write(u1,'(f9.2)') MN(i,:)
enddo

close(u1)

deallocate(M)
deallocate(N)

End Program MainReadM

