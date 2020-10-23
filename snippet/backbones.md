# Method order in a class

```python
class Event(models.Model):
    # Private attributes
    _name = 'event.event'
    _description = 'Event'

    # Default methods
    def _default_name(self):
        ...

    # Fields declaration
    name = fields.Char(string='Name', default=_default_name)
    seats_reserved = fields.Integer(oldname='register_current', string='Reserved Seats',
        store=True, readonly=True, compute='_compute_seats')
    seats_available = fields.Integer(oldname='register_avail', string='Available Seats',
        store=True, readonly=True, compute='_compute_seats')
    price = fields.Integer(string='Price')
    event_type = fields.Selection(string="Type", selection='_selection_type')

    # compute and search fields, in the same order of fields declaration
    @api.depends('seats_max', 'registration_ids.state', 'registration_ids.nb_register')
    def _compute_seats(self):
        ...

    @api.model
    def _selection_type(self):
        return []

    # Constraints and onchanges
    @api.constrains('seats_max', 'seats_available')
    def _check_seats_limit(self):
        ...

    @api.onchange('date_begin')
    def _onchange_date_begin(self):
        ...

    # CRUD methods (and name_get, name_search, ...) overrides
    def create(self, values):
        ...

    # Action methods
    def action_validate(self):
        self.ensure_one()
        ...

    # Business methods
    def mail_user_confirm(self):
        ...
```

# Commit message structure

```shell
[TAG] module: describe your change in a short sentence (ideally < 50 chars)

Long version of the change description, including the rationale for the change,
or a summary of the feature being introduced.

Please spend a lot more time describing WHY the change is being done rather
than WHAT is being changed. This is usually easy to grasp by actually reading
the diff. WHAT should be explained only if there are technical choices
or decision involved. In that case explain WHY this decision was taken.

End the message with references, such as task or bug numbers, PR numbers, and
OPW tickets, following the suggested format:
task-123 (related to task)
Fixes #123  (close related issue on Github)
Closes #123  (close related PR on Github)
opw-123 (related to ticket)
```

# The complete tree of Odoo module

```
addons/plant_nursery/
|-- __init__.py
|-- __manifest__.py
|-- controllers/
|   |-- __init__.py
|   |-- plant_nursery.py
|   |-- portal.py
|-- data/
|   |-- plant_nursery_data.xml
|   |-- plant_nursery_demo.xml
|   |-- mail_data.xml
|-- models/
|   |-- __init__.py
|   |-- plant_nursery.py
|   |-- plant_order.py
|   |-- res_partner.py
|-- report/
|   |-- __init__.py
|   |-- plant_order_report.py
|   |-- plant_order_report_views.xml
|   |-- plant_order_reports.xml (report actions, paperformat, ...)
|   |-- plant_order_templates.xml (xml report templates)
|-- security/
|   |-- ir.model.access.csv
|   |-- plant_nursery_groups.xml
|   |-- plant_nursery_security.xml
|   |-- plant_order_security.xml
|-- static/
|   |-- img/
|   |   |-- my_little_kitten.png
|   |   |-- troll.jpg
|   |-- lib/
|   |   |-- external_lib/
|   |-- src/
|   |   |-- js/
|   |   |   |-- widget_a.js
|   |   |   |-- widget_b.js
|   |   |-- scss/
|   |   |   |-- widget_a.scss
|   |   |   |-- widget_b.scss
|   |   |-- xml/
|   |   |   |-- widget_a.xml
|   |   |   |-- widget_a.xml
|-- views/
|   |-- assets.xml
|   |-- plant_nursery_menus.xml
|   |-- plant_nursery_views.xml
|   |-- plant_nursery_templates.xml
|   |-- plant_order_views.xml
|   |-- plant_order_templates.xml
|   |-- res_partner_views.xml
|-- wizard/
|   |--plant_order_make.py
|   |--plant_order_make_views.xml
```

# Tag name in commit

- [FIX] for bug fixes: mostly used in stable version but also valid if you are fixing a recent bug in development version;
- [REF] for refactoring: when a feature is heavily rewritten;
- [ADD] for adding new modules;
- [REM] for removing resources: removing dead code, removing views, removing modules, …;
- [REV] for reverting commits: if a commit causes issues or is not wanted reverting it is done using this tag;
- [MOV] for moving files: use git move and do not change content of moved file otherwise Git may loose track and history of the file; also used when moving code from one file to another;
- [REL] for release commits: new major or minor stable versions;
- [IMP] for improvements: most of the changes done in development version are incremental improvements not related to another tag;
- [MERGE] for merge commits: used in forward port of bug fixes but also as main commit for feature involving several separated commits;
- [CLA] for signing the Odoo Individual Contributor License;
- [I18N] for changes in translation files;

# A commit example

```
[TAG] module: describe your change in a short sentence (ideally < 50 chars)

Long version of the change description, including the rationale for the change,
or a summary of the feature being introduced.

Please spend a lot more time describing WHY the change is being done rather
than WHAT is being changed. This is usually easy to grasp by actually reading
the diff. WHAT should be explained only if there are technical choices
or decision involved. In that case explain WHY this decision was taken.

End the message with references, such as task or bug numbers, PR numbers, and
OPW tickets, following the suggested format:
task-123 (related to task)
Fixes #123  (close related issue on Github)
Closes #123  (close related PR on Github)
opw-123 (related to ticket)
```

# Main Directories in Linux

- **/bin** is a place for most commonly used terminal commands, like ls, mount, rm, etc.

- **/boot** contains files needed to start up the system, including the Linux kernel, a RAM disk image and bootloader configuration files.

- **/dev** contains all device files, which are not regular files but instead refer to various hardware devices on the system, including hard drives.

- **/etc** contains system-global configuration files, which affect the system's behavior for all users.

- **/home** home sweet home, this is the place for users' home directories.

- **/lib** contains very important dynamic libraries and kernel modules

- **/media** is intended as a mount point for external devices, such as hard drives or removable media (floppies, CDs, DVDs).

- **/mnt** is also a place for mount points, but dedicated specifically to "temporarily mounted" devices, such as network filesystems.

- **/opt** can be used to store additional software for your system, which is not handled by the package manager.

- **/proc** is a virtual filesystem that provides a mechanism for kernel to send information to processes.

- **/root** is the superuser's home directory, not in /home/ to allow for booting the system even if /home/ is not available.

- **/run** is a tmpfs (temporary file system) available early in the boot process where ephemeral run-time data is stored. Files under this directory are removed or truncated at the beginning of the boot process.
(It deprecates various legacy locations such as /var/run, /var/lock, /lib/init/rw in otherwise non-ephemeral directory trees as well as /dev/.* and /dev/shm  which are not device files.)

- **/sbin** contains important administrative commands that should generally only be employed by the superuser.

- **/srv** can contain data directories of services such as HTTP (/srv/www/) or FTP.

- **/sys** is a virtual filesystem that can be accessed to set or obtain information about the kernel's view of the system.

- **/tmp** is a place for temporary files used by applications.

- **/usr** contains the majority of user utilities and applications, and partly replicates the root directory structure, containing for instance, among others, /usr/bin/ and /usr/lib.

- **/var** is dedicated to variable data, such as logs, databases, websites, and temporary spool (e-mail etc.) files that persist from one boot to the next. A notable directory it contains is /var/log where system log files are kept.

# Odoo.sh in a Container

```shell
.
├── home
│    └── odoo
│         ├── src
│         │    ├── odoo                Odoo Community source code
│         │    │    └── odoo-bin       Odoo server executable
│         │    ├── enterprise          Odoo Enterprise source code
│         │    ├── themes              Odoo Themes source code
│         │    └── user                Your repository branch source code
│         ├── data
│         │    ├── filestore           database attachments, as well as the files of binary fields
│         │    └── sessions            visitors and users sessions
│         └── logs
│              ├── install.log         Database installation logs
│              ├── odoo.log            Running server logs
│              ├── update.log          Database updates logs
│              └── pip.log             Python packages installation logs
└── usr
     ├── lib
     │    ├── python2.7
     │         └── dist-packages       Python 2.7 standard libraries
     │    ├── python3
     │         └── dist-packages       Python 3 standard libraries
     │    └── python3.5
     │         └── dist-packages       Python 3.5 standard libraries
     ├── local
     │    └── lib
     │         ├── python2.7
     │         │    └── dist-packages  Python 2.7 third-party libraries
     │         └── python3.5
     │              └── dist-packages  Python 3.5 third-party libraries
     └── usr
          └── bin
               ├── python2.7           Python 2.7 executable
               └── python3.5           Python 3.5 executable
```
