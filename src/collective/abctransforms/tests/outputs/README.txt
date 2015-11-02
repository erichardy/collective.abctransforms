abc2midi ../inputs/DonaldBlue.abc -o DonaldBlue1.mid
timidity --quiet=9 -A 400 -EFchorus=2,50 -EFreverb=2 -Oa -o DonaldBlue1.aiff DonaldBlue1.mid
lame --cbr -b 32 -f --quiet DonaldBlue1.aiff DonaldBlue1.mp3

abcm2ps ../inputs/DonaldBlue.abc -O DonaldBlue.ps
ps2pdf DonaldBlue.ps DonaldBlue.pdf
# abcm2ps ../inputs/DonaldBlue.abc -E -O DonaldBlue.eps

# with ps2epsi
# convert -filter Catrom -resize 600 DonaldBlue.epsi DonaldBlue.png
#
# with convert from abcm2ps -E .... for eps output
# convert -filter Catrom -resize 600 DonaldBlue001.eps DonaldBlue2.png
# seems less quality than the other.
