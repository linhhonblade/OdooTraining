# Deploying Odoo

## dbfilter

- Consider this if the instance is multi-companies

## Builtin Server

For production use, it is recommended to use the multiprocessing server
- Multiprocessing is enabled by configuring a `non-zero number of worker processes`
- Worker limits can be configured based on the hardware configuration to avoid resources exhaustion

### Worker number calculation

- Max workers that server can handle: (#CPU * 2) + 1
- Cron workers need CPU
- 1 worker ~ 6 concurrent users

### Memory size calculation

- heavy requests: 20%, 1G RAM
- light requests: 80%, 150MB

Needed RAM = #worker * ((light_worker_ratio * light_worker_ram) + (heavy_worker_raitio * heavy_worker_ram)) = #worker * 324.8MB

sample in `/etc/odoo.conf`

```shell
[options]
limit_memory_hard = 1677721600
limit_memory_soft = 629145600
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200
max_cron_threads = 1
workers = 8
```

### Live Chat

In multiprocessing, config nginx

### HTTPS

