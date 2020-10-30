# hunter-dkim

This project validates that the "smoking gun" email from that NYPost story
actually was a valid email sent 6 years ago. We know this because GMail
cryptographically signed it with "DKIM".

This repository contains the original email, plus Google's DKIM key at the 
time the email was sent. This key is no longer provided by GMail's DNS
servers, so you have to hack up a server yourself, such as using BIND9
as a resolver with a Response Policy Zone (RPC).

Remember that while the email is validated, the context isn't. It's possible this
reflects a secret meeting to conspire with Vice President Biden. Or, it's possible the
guy attended one of the many Washington D.C. social functions whereby people
shake hands with politicians and exchange pleasantries. As Richelieu is claimed to have
said "Give me six words by the most honest of men and I'll find something to hang him by".
Give me an email dump from the most honest of persons, and I'll pull one out of context
to hang them by.
