> You should neither add incoming/out going email per user/employee nor add personal emails as incoming/outgoing email.

**The right and simple way of email integration is as follows:**

1. Set up a catch-all email at your email server, I assume it would be catchall@yourcompany.com. This catch all feature in the email server is a must-have requirement.
2. Go to General Settings to set yourcompany.com as the domain alias.
3. Configure the catchall@yourcompany.com as both incoming and outgoing email server within Odoo
4. For each user, Messaging Alias must be specified in the user form. For example, John Doe may have john.doe as his messaging alias and Jane Roe may have jane.roe as her messaging alias which will "create" their business email as john.doe@yourcompany.com and janeroe@yourcompany.com corresponding.
5. Let your employees know that their working email are john.doe@yourcompany.com and jan.roe@yourcompany.com. If business cards areprinted, the working email for them should be john.doe@yourcompany.com / jan.roe@yourcompany.com
6. Ensure that john.doe@yourcompany.com and jan.roe@yourcompany.com do NOT exist in your email server.
7. Each user document is linked/related to a partner document which should be declared with a real email address. You have to definethe real email address for each user in his/her related partner profile. It is usually a personal email address (e.g. john.doe@gmailcom or john.doe@yahoo.com, etc)

**How the above setting works and could help your company?**
1. When people send a message to an email address that does not exist in your email server, the message will be forwarded to catchall@yourcompany.com thanks to catch-all feature of your email server
2. Every 5 minutes (or more/less which can be configured within Odoo fetchmail action), Odoo will login your incoming email server (i.e. catchall@yourcompany.com) to fetch all email messages there.
3. During the fetching process, Odoo check header of each email message which contains information about sender, recipient, message id, etc. If the Odoo found that the message is send to one of email alias (e.g. john.doe@yourcompany.com) it will deliever the message to the right people at the right place, e.g. deliver to inbox of John Doe, attach message to the related document (sale order, invoice, manufacturing order, etc)
4. The related people (including your employees and partners) will be notified about the new coming message with a copy sent to their personal mail box.

