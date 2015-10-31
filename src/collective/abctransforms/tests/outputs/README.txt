abc2midi ../inputs/DonaldBlue.abc -o DonaldBlue1.mid
timidity --quiet=9 -A 400 -EFchorus=2,50 -EFreverb=2 -Oa -o DonaldBlue1.aiff DonaldBlue1.mid
lame --cbr -b 32 -f --quiet DonaldBlue1.aiff DonaldBlue1.mp3
