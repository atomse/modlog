import modlog



logger = modlog.getLogger(__name__, 'color')


for level in ['debug', 'info', 'warn', 'error', 'critical']:
    getattr(logger, level)(level)
