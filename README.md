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

### "How can I replicate this?"

There's a python script that'll do the validation for you within this repo.

If you run your own resolver, they all have ability to override certain records,
so you can insert this one record (for `20120113._domainkey.gmail.com TXT`) 
so that any tool will work, such as the DKIM Verifier add-on for Thunderbird.
Google "Response Policy Zones for BIND9". That's what I first did.

Once you've replicated that the emails verify, try to change them and see if
they still verify. Change then and change the signature. Hack away. Find
some way that verification can happen with forged/altered emails.

### "The entire email dump verified or just this one?"

I've only validated this one email. It's the only one sent to me.

Many can't be validated. They are sent from domains that don't use DKIM
to sign outgoing emails. Others used DKIM when sent, but we can no longer
find the public-keys that would authenticate them (it's been years).

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

### So the Email is real, but the account could be fake, by someone **claiming** to be Pozharskyi."

Yup, that's possible. We've only proven *a* Vadym Pozharskyi sent the email,
not that *the* Vadym Pozharskyi sent it. It's somebody who, in 2014, claimed
to have been a "V. Pozharskyi from Ukraine".

DKIM proves only that
the account indeed was `v.pozharskyi.ukraine@gmail.com`.
You can create an account `rob.graham.usa@gmail.com`, 
and GMail will happily verify those outgoing messages without verifying
the person sending them is actually named Robert Graham. In any event,
even if it could verify a person's real name, it couldn't verify it's the same
Robert Graham as myself.

Thus, we know the emails (based on DKIM) come from somebody claiming to
be a Vadym Pozharskyi, but there's no way to prove it's our Vadym.

But, there are other sources that validate that he used this address.
For example, there's [this document](https://www.hsgac.senate.gov/imo/media/doc/2020-08-31-Painter%20Interview%20with%20Exhibits.pdf)
from a Senate investigation showing him using that GMail address last year.

DKIM does verify the date (`Date:`). If it's somebody claiming to have been Pozharskyi
claiming to have met Hunter's dad, then it's a conspiracy from 2014 not a 
conspiracy from 2020. It would mean somebody who knew intimate details about
Hunter Biden sending him fake messages on the off chance that in a future election
they would be able to hack into Hunter's email account to expose them.

Like the theory of them hacking into GMail to obtain the private-key, if the 
conspiracy was this sophisticated, they could do better emails. This one is lame.

