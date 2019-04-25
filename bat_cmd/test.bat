set num=1
:liuhu
if %num% equ 10 exit
set /a num+=1
ping -n 3 127.0.0.1
echo "liuhu nihao ma " >> test.txt

goto liuhu