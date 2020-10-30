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

## FAQ

### "Can't signatures can be faked, replayed, forged, or cheated?"

Not cryptographic signatures, at least, not in any practical/reasonable manner.

They use a mathematical trick of **public-key crypto** where a pair of matching keys
are generated. Something signed with one, a **private-key**, can only be verified with the
other, the **public-key**.

Public-key signatures it what underlies Bitcoin. If you could find a way to forge these
signatures, you could instantly make billions of dollars.

The trick is you have to keep the private-key private. Bitcoin do sometimes get stolen
when people break into a computer and steal the wallet's private-key. If somebody broke
into GMail, they'd be able to forge signatures as well.

So many people ask this question. They know basic 'checksums', and know that if you change
the contents you can just change the checksum to match. The step they don't undestand
is that public-keys are involved, that without knowing the matching private-key, there's
no way to adjust the signature to match the contents.

### "Okay, you've verified the metadata, but couldn't the contents of the body of the email be changed?"

The signature covers both the metadata and the body. The slightest change to either
invalidates the signature.

### "Okay, you've verified the email contents, couldn't the metadata be spoofed, such as the real email being sent last month?"

The signature covers both the metadata and the body. Yes, some email metadata isn't covered by
the signature, esoteric things like `X-Received:` headers. But the signature does cover the
ones we care about: `Date:`, `From:`, `To:`, and `Subject:`.

### "How about very small changes? Couldn't they escape detection?"

It's like being a "little bit pregnant". If you changed the smallest thing, then the entire
signatures fails -- and verification fails. It doesn't matter how small.

Well, except spaces. DKIM uses a "relaxed" verification scheme which allows, in certain
circumstances, spaces to be added.

But even that isn't an issue here. This message used the "quoted printable" encoding,
which means there's almost no place to add a space.

### "But GMail's DNS servers no longer provide the public-key"

This is indeed a problem -- for most email domains that aren't GMail.

But in this case, because GMail is so popular, there are thousands of sources
of the old key, including archives of old sites, log files from servers, and so
on.

Thus, in theory the system only works when the domain in question is currently
providing the public-key to validate signatures, in practice we can know GMail's
old key even if they don't provide it directly.

The proper key is one of the files in this project, but of course, I could
be lying. You can verify this by googling the key, searching archives
like Archive.org, or by specialty logging sites that have retained
copies of the old key.

### "My DKIM verifier can only fetch the key from a DNS server"

Yes, that's a problem. Other DKIM verification tools and libraries can grab
the key from a file, so you could try that ([like this one](https://gist.github.com/stevecheckoway/51e63d4c269bd2be4a50a3b39645a77c)).

What I did instead was set up BIND9 as my DNS resolver, then configured
a "Response Policy Zone" (RPZ) with this one record changed. This means
that it'll provide live resolution for any other names, but overwrite
the correct response (of "not found") with the old key that I retrieve
from Internet websites.

Overriding certain records in a resolver this way is pretty common practice.
If you manage your own DNS server already, you can easily update it to 
provide the correct public-key.

### "What about this page that says DKIM can be fooled?"

Many people cite the following web page to claim DKIM doesn't work:

<https://noxxi.de/research/breaking-dkim-on-purpose-and-by-chance.html>

None of it applies to this email. It does not apply because:
- there are no duplicate metadata fields in the actual email
- there isn't a length (`l=`) field in the actual email
- the `content-transfer-encoding` field is included within the signature

It's pretty obvious that it doesn't apply if you read it and pay attention to it.

### So the Email is real, but the account could be fake. It's only somebody **claiming** to be Pozharskyi."

Yup, that's possible. It seems his official address was `vadym.pozharskyi@burisma.com`,
not the `v.pozharskyi.ukraine@gmail.com` address seen in this email.

DKIM only proves that was the real `From:` address. It doesn't prove who actually
owned the account. Indeed, even if it was his account, a staffer could've sent
it on his behalf.

So we can't authentic it was this person.

What we can verify, however, is that if somebody created a GMail account to 
impersonate Pozharskyi back in 2014, it was some trickery they were up to then,
but not now. It would have to be some really long-ranged plan whereby they
send fake emails to his  account on the hopes that somebody in the future
his emails could leak or get hacked. Frankly, if that was their plan, they should've
sent more incriminating emails (this one isn't that incriminating).

But, there are other sources that sorta validate that he used this address.
For example, there's [this document](https://www.hsgac.senate.gov/imo/media/doc/2020-08-31-Painter%20Interview%20with%20Exhibits.pdf)
from a Senate investigation showing him using that GMail address last year.





