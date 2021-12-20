tmp=$(mktemp -d)
while test 1
do
for win in $(wmctrl -l | cut -d " " -f 1)
do
import -window "$win" "$tmp/$win.png"
colorname=$(tesseract "$tmp/$win.png" - --psm 11 --dpi 72 -l eng 2>/dev/null | python2 suggestcolor.py)
case $colorname
in
"black" )
color="363B48"
;;
"gray" )
color="868A93"
;;
"red" )
color="E41B1B"
;;
"orange" )
color="E4601B"
;;
"yellow" )
color="E4DD1B"
;;
"green" )
color="1BE41E"
;;
"blue" )
color="1B4DE4"
;;
"purple" )
color="681BE4"
;;
* )
color="ff0000"
esac
sed s/"#000000"/"#${color}"/g < AJ-Padlock-Silhouette.svg | rsvg-convert | convert -resize "64x64" png:- -size "64x64" xc:none -composite png:- | xseticon -id $win /dev/stdin
done
done
