# In order to better understand odoo performance

## Thanks to

- odoo-development.readthedocs.io
- [odony](https://github.com/odoo/odoo/issues/39825#issuecomment-555175814)

## Database connections

**--db_maxconn**

specify the the maximum number of physical connections to posgresql - *odoo/tools/config.py*

specify the the maximum number of physical connections to posgresql 

### How many processes does odoo run?

- In Odoo
  - longpolling: no more than 1 process
  - workers
  - max_cron_threads
- In Postgres
  - max_connections

```sql
(1 + workers + max_cron_threads) * db_maxconn < max_connections
```

**limit_memory_soft**

Applies per process, in both modes (multi-process and multi-thread). Should be large enough to hold the VM size between requests. It is also used to determine the size of the registry LRU (assuming 15MB per db), so 15 * 80MB should allow you to hold 80 dbs. Some registries may be larger so YMMV, you might want to reserve 30MB per db.

If it's not correctly set it will cause faster worker recycling, and possibly poor perf, but should not block the system.

You do not want to set it higher than `server_ram / workers`, and probably less than that as you should reserve some amount of memory on the side for the system cache/buffers (and for the DB if your PG server is on the same machine).

On macOS this setting needs to be set exaggeratedly high because the OS allocates 4GB of virtual memory for each process, making it more or less useless as a limit.
