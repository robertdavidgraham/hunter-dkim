# hunter-dkim

This project validates that the "smoking gun" email from that NYPost story
actually was a valid email sent 6 years ago. We know this because GMail
cryptographically signed it with "DKIM".

This repository contains the original email, plus Google's DKIM key at the 
time the email was sent. This key is no longer provided by GMail's DNS
servers, so you have to hack up a server yourself, such as using BIND9
as a resolver with a Response Policy Zone (RPZ).

Remember that while the email is validated, the context isn't. It's possible this
reflects a secret meeting to conspire with Vice President Biden. Or, it's possible the
guy attended one of the many Washington D.C. social functions whereby people
shake hands with politicians and exchange pleasantries. As Richelieu is claimed to have
said **"Give me six words by the most honest of men and I'll find something to hang him by"**.
Give me an email dump from the most honest of persons, and I'll pull one out of context
to hang them in the court of social media.

## FAQ: Can't signatures can be faked, replayed, forged, or cheated?

Not cryptographic signatures, at least, not in any practical/reasonable manner.

They use a mathematical trick of **public-key crypto** where a pair of matching keys
are generated. Something signed with one, a **private-key**, can only be verified with the
other, the **public-key**.

Public-key signatures it what underlies Bitcoin. If you could find a way to forge these
signatures, you could instantly make billions of dollars.

The trick is you have to keep the private-key private. Bitcoin do sometimes get stolen
when people break into a computer and steal the wallet's private-key. If somebody broke
into GMail, they'd be able to forge signatures as well.

## FAQ: Okay, you've verified the metadata, but couldn't the contents of the body of the email be changed?

The signature covers both the metadata and the body.

## FAQ: Okay, you've verified the email contents, couldn't the metadata be spoofed, such as the real email being sent last month?

The signature covers both the metadata and the body.

## FAQ: How about very small changes? Couldn't they escape detection?

It's like being a "little bit pregnant". If you changed the smallest thing, then the entire
signatures fails -- and verification fails. It doesn't matter how small.

Well, except spaces. DKIM uses a "relaxed" verification scheme which allows, in certain
circumstances, spaces to be added here. In theory this could be an issue, but in practice,
it's not an issue here. It uses "quoted printable" encoding, meaning, there's no place
to insert a space.

## FAQ: But GMail's DNS servers no longer provide the public-key

This is indeed a problem -- for most email domains that aren't GMail.

But in this case, because GMail is so popular, there are thousands of sources
of the old key, including archives of old sites, log files from servers, and so
on.

Thus, in theory the system only works when the domain in question is currently
providing the public-key to validate signatures, in practice we can know GMail's
old key even if they don't provide it directly.

## FAQ: My DKIM verifier can only fetch the key from a DNS server

Yes, that's a problem. Other DKIM verification tools and libraries can grab
the key from a file, so you could try that.

What I did instead was set up BIND9 as my DNS resolver, then configured
a "Response Policy Zone" (RPZ) with this one record changed. This means
that it'll provide live resolution for any other names, but overwrite
the correct response (of "not found") with the old key that I retrieve
from Internet websites.

Overriding certain records in a resolver this way is pretty common practice.
If you manage your own DNS server already, you can easily update it to 
provide the correct public-key.

## FAQ: What about this page that says DKIM can be fooled?

Many people cite the following web page to claim DKIM doesn't work:

<https://noxxi.de/research/breaking-dkim-on-purpose-and-by-chance.html>

None of it applies to this email. It does not apply because:
- there are no duplicate metadata fields in the actual email
- there isn't a length (`l=`) field in the actual email

It's pretty obvious that it doesn't apply if you read it and pay attention to it.








