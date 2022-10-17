# Timestamped Email

This email both passes DKIM verification:

```
$ ../verify.py timestamped.eml
timestamped.eml: DKIM signature verified
```

...and has been timestamped with [OpenTimestamps](https://opentimestamps.org),
proving that the email itself existed prior to 2016:

```
$ sudo pip3 install opentimestamps-client
$ ots verify timestamped.eml.ots
Assuming target filename is 'timestamped.eml'
Success! Bitcoin block 429347 attests existence as of 2016-09-11 EDT
```

If you don't have Bitcoin Core installed, you can also verify it manually
against a block explorer:

```
$ ots --no-bitcoin verify timestamped.eml.ots
Assuming target filename is 'timestamped.eml'
Not checking Bitcoin attestation; Bitcoin disabled
To verify manually, check that Bitcoin block 429347 has merkleroot e97422f79cddd4fbd176272b3aba09cbdae6874f5eb81db2a474b2e812076109
```
