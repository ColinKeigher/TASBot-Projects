import sys

charmap = {
	'A' : 0xb0,
	'B' : 0xb1,
	'C' : 0xb2,
	'D' : 0xb3,
	'E' : 0xb4,
	'F' : 0xb5,
	'G' : 0xb6,
	'H' : 0xb7,
	'I' : 0xb8,
	'J' : 0xb9,
	'K' : 0xba,
	'L' : 0xbb,
	'M' : 0xbc,
	'N' : 0xbd,
	'O' : 0xbe,
	'P' : 0xbf,
	'Q' : 0xc0,
	'R' : 0xc1,
	'S' : 0xc2,
	'T' : 0xc3,
	'U' : 0xc4,
	'V' : 0xc5,
	'W' : 0xc6,
	'X' : 0xc7,
	'Y' : 0xc8,
	'Z' : 0xc9,
	'a' : 0xd0,
	'b' : 0xd1,
	'c' : 0xd2,
	'd' : 0xd3,
	'e' : 0xd4,
	'f' : 0xd5,
	'g' : 0xd6,
	'h' : 0xd7,
	'i' : 0xd8,
	'j' : 0xd9,
	'k' : 0xda,
	'l' : 0xdb,
	'm' : 0xdc,
	'n' : 0xdd,
	'o' : 0xde,
	'p' : 0xdf,
	'q' : 0xca,
	'r' : 0xcb,
	's' : 0xcc,
	't' : 0xcd,
	'u' : 0xce,
	'v' : 0xcf,
	'w' : 0x81,
	'x' : 0x88,
	'y' : 0x8c,
	'z' : 0x8f,
	'.' : 0xe9,
	'!' : 0xea,
	'?' : 0xeb,
	' ' : 0xfe,
	'0' : 0xf0,
	'1' : 0xf1,
	'2' : 0xf2,
	'3' : 0xf3,
	'4' : 0xf4,
	'5' : 0xf5,
	'6' : 0xf6,
	'7' : 0xf7,
	'8' : 0xf8,
	'9' : 0xf9,
	',' : 0x9a,
	"'" : 0xab
}

out = "byte "

st = sys.argv[1]
for s in st:
	out += hex(charmap[s]).replace("0x","$") + ","

print(out[:-1])

