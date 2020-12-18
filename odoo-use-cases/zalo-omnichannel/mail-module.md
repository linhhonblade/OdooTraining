# mail.thread

## Overview

> mail_thread model is meant to be inherited by any model that needs to act as a discussion topic on which messages can be attached. Public methods are prefixed with ``message_`` in order to avoid name collisions with methods of the models that will inherit from this class.

> ``mail.thread`` defines fields used to handle and display the communication history. ``mail.thread`` also manages followers of inheriting classes. All features and expected behavior are managed by mail.thread. Widgets has been designed for the 7.0 and following versions of Odoo.

> Inheriting classes are not required to implement any method, as the default implementation will work for any model. However it is common to override at least the ``message_new`` and ``message_update`` methods (calling ``super``) to add model-specific behavior at creation and update of a thread when processing incoming emails.id

## API

### CRUD

- create(self, vals_list):
  - Chatter override :
    - subscribe uid
    - subscribe followers of parent
    - log a creation message

- write(self, values)
- unlink(self)
  - Override unlink to delete messages and followers. This cannot be cascaded, because link is done through (res_model, res_id)
- copy_data(self, default=None)

### Model / CRUDs helper

- _createion_message(self)
  - Get the creation message to log into the chatter at the record's creation. :returns: The message's body to log.
- _get_mail_message_access(self, res_ids, operators, modename=None)

### Wrapper snd no tool

- message_change_thread(self, new_thread)

### Tracking / Logs

- _prepare_tracking(self, fields)
  - Prepare the tracking of ``fields`` for ``self``.
  - :param fields: iterable of fields names to potentially track
- _discard_trackinig
- _finalize tranfer
  - Generate the tracking messages for the records that have been prepared with ``_prepare_tracking
- _get_tranked_fields self(self)
  - Return the set of trancked fields name

### Mail Gateway

- _routing_handle_bounce(self, email_message, message_dic)
  - Handle bounce of incoming email. Based on values of the bounce (email and related partner, send message and its messageID)
  - :param email_message: incoming email;
  - :type email_message: email.message;
  - :param message_dict: dictionary holding already-parsed values and in which bounce-related values will be added;
  - :type message_dict: dictionary;

- _routing_check_route(self, message, message_dict, route, raise_exception=True)
  - Verify route validity. Check and rules:
    - 1 - if thread_id -> check that document effectively exists; otherwise fallback on a message_new by resetting thread_id
    - 2 - check that message_update exists if thread_id is set; or at least that message_new exist
    - 3 - if there is an alias, check alias_contact:
      - 'followers' and thread_id: check on target document that the author is in the followers
      - 'followers' and alias_parent_thread_id: check on alias parent document that the author is in the followers
      - 'partners': check that author_id id set

  - :param message: an email.message instance
  - :param message_dict: dictionary of values that will be given to mail_message.create()
  - :param route: route to check which is a tuple (model, thread_id, custom_values, uid, alias)
  - :param raise_exception: if an error occurs, tell whether to raise an error or just log a warning and try other processing or invalidate route

- message_route(self, message, message_dict, model=None, thread_id=None, custom_values=None)
  - Attempt to figure out the correct target model, thread_id, custom_values and user_id to use for an incoming message. Multiple values may be returned, if a message had multiple recipients matching existing mail.aliases, for example.
  - The following heuristics are used, in this order:
    -  if the message replies to an existing thread by having a Message-Id that matches an existing mail_message.message_id, we take the original message model/thread_id pair and ignore custom_value as no creation will take place;
    -  look for a mail.alias entry matching the message recipients and use the corresponding model, thread_id, custom_values and user_id. This could lead to a thread update or creation depending on the alias;
    - fallback on provided ``model``, ``thread_id`` and ``custom_values``;
    - raise an exception as no route has been found
  - :param string message: an email.message instance
  - :param dict message_dict: dictionary holding parsed message variables
  - :param string model: the fallback model to use if the message does not match any of the currently configured mail aliases (may be None if a matching alias is supposed to be present)
  - :type dict custom_values: optional dictionary of default field values to pass to ``message_new`` if a new record needs to be created. Ignored if the thread record already exists, and also if a matching mail.alias was found (aliases define their own defaults)
  - :param int thread_id: optional ID of the record/thread from ``model`` to which this mail should be attached. Only used if the message does not reply to an existing thread and does not match any mail alias.
  :return: list of routes [(model, thread_id, custom_values, user_id, alias)]
  :raises: ValueError, TypeError

- message_process(self, model, message, custom_values=None, save_original=False, strip_attachments=False, thread_id=None)
  - Process an incoming RFC2822 email message, relying on ``mail.message.parse()`` for the parsing operation, and ``message_route()`` to figure out the target model.
  - Once the target model is known, its ``message_new`` method is called with the new message (if the thread record did not exist) or its ``message_update`` method (if it did).
  - :param string model: the fallback model to use if the message does not match any of the currently configured mail aliases (may be None if a matching alias is supposed to be present)
  - :param message: source of the RFC2822 message
  - :type message: string or xmlrpclib.Binary
  - :type dict custom_values: optional dictionary of field values to pass to ``message_new`` if a new record needs to be created. Ignored if the thread record already exists, and also if a matching mail.alias was found (aliases define their own defaults)
  - :param bool save_original: whether to keep a copy of the original email source attached to the message after it is imported.
  - :param bool strip_attachments: whether to strip all attachments before processing the message, in order to save some space.
  - :param int thread_id: optional ID of the record/thread from ``model`` to which this mail should be attached. When provided, this overrides the automatic detection based on the message headers.

- message(sefl, msg_dict, custom_values):
  - Called by ``message_process`` when a new message is received for a given thread model, if the message did not belong to an existing thread.
  - The default behavior is to create a new record of the corresponding model (based on some very basic info extracted from the message). Additional behavior may be implemented by overriding this method.
  - :param dict msg_dict: a map containing the email details and attachments. See ``message_process`` and ``mail.message.parse`` for details.
  - :param dict custom_values: optional dictionary of additional field values to pass to create() when creating the new thread record. Be careful, these values may override any other values coming from the message.
  - :rtype: int
  - :return: the id of the newly created thread object

- message updateself, msg_iic):
  - Called by ``message_process`` when a new message is received for an existing thread. The default behavior is to update the record with update_vals taken from the incoming email.
  - Additional behavior may be implemented by overriding this method.
  - :param dict msg_dict: a map containing the email details and attachments. See ``message_process`` and ``mail.message.parse()`` for details.
  - :param dict update_vals: a dict containing values to update records given their ids; if the dict is None or is void, no write operation is performed.

- message_parse(self, message, save_original=False):
  - Parses an email.message.Message representing an RFC-2822 email and returns a generic dict holding the message details.
  - :param message: email to parse
  - :type message: email.message.Message
  - :param bool save_original: whether the returned dict should include an ``original`` attachment containing the source of the message
  - :rtype: dict
  - :return: A dict with the following structure, where each field may not be present if missing in original message::
    - { 'message_id': msg_id,
              'subject': subject,
              'email_from': from,
              'to': to + delivered-to,
              'cc': cc,
              'recipients': delivered-to + to + cc + resent-to + resent-cc,
              'partner_ids': partners found based on recipients emails,
              'body': unified_body,
              'references': references,
              'in_reply_to': in-reply-to,
              'parent_id': parent mail.message based on in_reply_to or references,
              'is_internal': answer to an internal message (note),
              'date': date,
              'attachments': [('file1', 'bytes'),
                              ('file2', 'bytes')}
            }

- message_post(self, *, body='', subject=None, message_type='notification', email_from=None, author_id=None, parent_id=False, subtype_xmlid=None, subtype_id=False, partner_ids=None, channel_ids=None, attachments=None, attachment_ids=None, add_sign=True, record_name=False, **kwargs):
  - Post a new message in an existing thread, returning the new mail.message ID.
  - :param str body: body of the message, usually raw HTML that will be sanitized
  - :param str subject: subject of the message
  - :param str message_type: see mail_message.message_type field. Can be anything but user_notification, reserved for message_notify
  - :param int parent_id: handle thread formation
  - :param int subtype_id: subtype_id of the message, mainly use fore followers mechanism
  - :param list(int) partner_ids: partner_ids to notify
  - :param list(int) channel_ids: channel_ids to notify
  - :param list(tuple(str,str), tuple(str,str, dict) or int) attachments : list of attachment tuples in the form ``(name,content)`` or ``(name,content, info)``, where content is NOT base64 encoded
  - :param list id attachment_ids: list of existing attachement to link to this message
  - Should only be setted by chatter
  - Attachement object attached to mail.compose.message(0) will be attached to the related document.
  - Extra keyword arguments will be used as default column values for the new mail.message record.
  - :return int: ID of newly created mail.message

### Notify API

- _notify_thread(self, message, msg_vals=False, notify_by_email=True, **kwargs):
  > Được gọi ra trong hàm message_post và message_notify
  - Main notification method. This method basically does two things:
    - call ``_notify_compute_recipients`` that computes recipients to notify based on message record or message creation values if given (to optimize performance if we already have data computed);
    - performs the notification process by calling the various notification methods implemented;
  - This method cnn be overridden to intercept and postpone notification mechanism like mail.channel moderation.channel_get
  - :param message: mail.message record to notify;
  - :param msg_vals: dictionary of values used to create the message. If given it is used instead of accessing ``self`` to lessen query count in some simple cases where no notification is actually required;
  - Kwargs allow to pass various parameters that are given to sub notification methods. See those methods for more details about the additional parameters. Parameters used for email-style notifications

- message_notify(self, *, partner_ids=False, parent_id=False, model=False, res_id=False, author_id=None, email_from=None, body='', subject=False, **kwargs):
  - Shortcut allowing to notify partners of messages that shouldn't be  displayed on a document. It pushes notifications on inbox or by email depending on the user configuration, like other notifications.

- _notify_record_by_inbox(self, message, recipients_data, msg_vals=False, **kwargs):
  - Notification method: inbox. Do two main things:
    - create an inbox notification for users;
    - create channel / message link (channel_ids field of mail.message);
    - send bus notifications;

# mail.channel

