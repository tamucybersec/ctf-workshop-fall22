# Robots

## Description

The URL is all you need to get started to find the flag

## Solution
Use the developer tools and inspect the source code. Right mouse click on page -> Inspect or click Fn-F12.

flag: `gigem{N0ZonK-123-w!nn3rw!nn3r}`

Contents of robots.txt:
```text
User-agent: *
Disallow: /room1.html
Disallow: /room2.html
Disallow: /room3.html
```
room3.html contains the flag.
