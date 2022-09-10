# Secret Number

## Description
Can you find the secret number?

## Solution
Notice the sequence in numbers. They are incrementing by 2,3,4,5,7,8,9 so we can assume the next value is incremented by 10. You need to modify the POST request data being sent to the application to include 55. The easiest way is to inspect the source code so see the html form section and the options tags. `<option value="1">1</option>` can be change to `<option value="55">1</option>` then click submit. Doing this sends "numbers=55&submit=Submit" in the body of the HTTP request.

OR 

Upon viewing the website we're instructed to "Find the secret number" and given a select form. It can be enumerated, but that doesn't pan out -- none of the listed numbers are the secret numbers. Fortunately for us the select box is all client side and if we have a way to make these POST requests we can just make them with whatever number we want. A quick bash one-liner later to enumerate numbers, out pops the flag. 

```bash
for i in $(seq 1 1 100); do curl -X POST http://localhost/index.php -d numbers=$i 2>/dev/null | rg gigem ; done;
```
`gigem{TraingleNumSeqNotSoSecret}`


## Developer Notes
Run `make` to start up the container on port 80. For cleanup, run `make stop`.
